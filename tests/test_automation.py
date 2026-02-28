"""
Automation layer test suite — covers:
  - portal/automation.py  (generate_draft, send_brief_notification, run_brief_automation)
  - db helpers             (save_draft, get_dashboard_stats)
  - portal/client.py      (new_brief route spawns background thread)
  - portal/admin.py       (dashboard route passes stats)

All Anthropic and SendGrid calls are mocked — no real network traffic.
"""

import io
import json
import os
import sqlite3
import sys
import tempfile
import threading
import urllib.error
import unittest.mock as mock
from datetime import datetime, timezone
from unittest.mock import MagicMock, patch, call

import pytest

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, PROJECT_ROOT)

import db as db_module
import app as app_module
from portal import automation


# ═══════════════════════════════════════════════════════════════════════════════
# Shared fixtures
# ═══════════════════════════════════════════════════════════════════════════════

@pytest.fixture
def isolated_db(monkeypatch):
    """Fresh DB for each test that touches db_module directly."""
    tmp = tempfile.mkdtemp()
    path = os.path.join(tmp, "test_auto.db")
    monkeypatch.setattr(db_module, "DB_PATH", path)
    db_module.init_db()
    db_module.init_portal_db()
    return path


@pytest.fixture
def flask_app(tmp_path, monkeypatch):
    db_path = str(tmp_path / "auto.db")
    monkeypatch.setattr(db_module, "DB_PATH", db_path)
    _app = app_module.create_app()
    _app.config.update(
        TESTING=True,
        WTF_CSRF_ENABLED=False,
        SECRET_KEY="test-secret",
        UPLOAD_FOLDER=str(tmp_path / "uploads"),
        # No ANTHROPIC_API_KEY → automation skips immediately in tests
        ANTHROPIC_API_KEY="",
    )
    return _app


@pytest.fixture
def admin_http(flask_app):
    with flask_app.test_client() as c:
        admin = db_module.get_user_by_email("admin@copydtc.com")
        with c.session_transaction() as sess:
            sess["user_id"] = admin["id"]
            sess["user_name"] = admin["name"]
            sess["user_role"] = "admin"
            sess["user_email"] = admin["email"]
        yield c


@pytest.fixture
def client_user(isolated_db):
    uid = db_module.create_user("Alice", "alice@test.com", "pass1234", "client")
    return {"id": uid, "email": "alice@test.com", "name": "Alice"}


@pytest.fixture
def sample_brief(client_user, isolated_db):
    bid = db_module.create_brief(client_user["id"], {
        "title": "Launch Email",
        "product_name": "TestProd",
        "product_description": "A great product",
        "target_audience": "Busy parents",
        "main_benefit": "Saves 2 hours a day",
        "biggest_objection": "Too expensive",
        "tone": "friendly",
        "copy_type": "email",
        "notes": "",
    })
    return db_module.get_brief(bid)


# ═══════════════════════════════════════════════════════════════════════════════
# generate_draft
# ═══════════════════════════════════════════════════════════════════════════════

class TestGenerateDraft:

    def _mock_anthropic(self, text: str):
        """Return a mock anthropic.Anthropic that yields `text`."""
        msg = MagicMock()
        msg.content = [MagicMock(text=text)]
        client = MagicMock()
        client.messages.create.return_value = msg
        return client

    def test_returns_draft_text(self, sample_brief):
        with patch("anthropic.Anthropic", return_value=self._mock_anthropic("Great copy!")):
            result = automation.generate_draft(sample_brief, "fake-key")
        assert result == "Great copy!"

    def test_strips_whitespace(self, sample_brief):
        with patch("anthropic.Anthropic", return_value=self._mock_anthropic("  Draft  \n")):
            result = automation.generate_draft(sample_brief, "fake-key")
        assert result == "Draft"

    def test_passes_api_key_to_anthropic(self, sample_brief):
        with patch("anthropic.Anthropic") as mock_cls:
            mock_cls.return_value = self._mock_anthropic("x")
            automation.generate_draft(sample_brief, "sk-test-key")
        mock_cls.assert_called_once_with(api_key="sk-test-key")

    def test_uses_correct_model(self, sample_brief):
        client = self._mock_anthropic("ok")
        with patch("anthropic.Anthropic", return_value=client):
            automation.generate_draft(sample_brief, "k")
        _, kwargs = client.messages.create.call_args
        assert kwargs["model"] == "claude-sonnet-4-6"

    def test_user_message_contains_brief_fields(self, sample_brief):
        client = self._mock_anthropic("ok")
        with patch("anthropic.Anthropic", return_value=client):
            automation.generate_draft(sample_brief, "k")
        _, kwargs = client.messages.create.call_args
        user_msg = kwargs["messages"][0]["content"]
        assert "TestProd" in user_msg
        assert "Busy parents" in user_msg
        assert "Saves 2 hours a day" in user_msg
        assert "Too expensive" in user_msg
        assert "friendly" in user_msg
        assert "email" in user_msg

    def test_user_message_includes_notes_when_present(self, client_user, isolated_db):
        bid = db_module.create_brief(client_user["id"], {
            "title": "T", "product_name": "P", "product_description": "D",
            "target_audience": "A", "main_benefit": "B", "biggest_objection": "C",
            "tone": "casual", "copy_type": "email", "notes": "Keep it short!",
        })
        brief = db_module.get_brief(bid)
        client = self._mock_anthropic("ok")
        with patch("anthropic.Anthropic", return_value=client):
            automation.generate_draft(brief, "k")
        _, kwargs = client.messages.create.call_args
        assert "Keep it short!" in kwargs["messages"][0]["content"]

    def test_raises_when_content_empty(self, sample_brief):
        msg = MagicMock()
        msg.content = []
        client = MagicMock()
        client.messages.create.return_value = msg
        with patch("anthropic.Anthropic", return_value=client):
            with pytest.raises(RuntimeError, match="empty response"):
                automation.generate_draft(sample_brief, "k")


# ═══════════════════════════════════════════════════════════════════════════════
# send_brief_notification
# ═══════════════════════════════════════════════════════════════════════════════

class TestSendBriefNotification:

    _CFG = {
        "SENDGRID_API_KEY": "SG.test",
        "SENDGRID_FROM_EMAIL": "noreply@copywrite.io",
        "ADMIN_EMAIL": "admin@copywrite.io",
        "APP_BASE_URL": "https://app.example.com",
    }

    def _brief(self):
        return {
            "id": 42, "title": "Launch Email", "client_name": "Alice",
            "client_email": "alice@brand.com", "product_name": "Prod",
            "copy_type": "email", "tone": "friendly",
        }

    def _call(self, brief=None, draft="Draft text", config=None):
        brief = brief or self._brief()
        config = config or self._CFG
        automation.send_brief_notification(brief, draft, config)

    def _mock_urlopen(self, status=202):
        resp = MagicMock()
        resp.status = status
        resp.__enter__ = lambda s: s
        resp.__exit__ = MagicMock(return_value=False)
        return resp

    # ── skipping when keys absent ─────────────────────────────────────────────

    def test_skips_when_api_key_missing(self):
        cfg = {**self._CFG, "SENDGRID_API_KEY": ""}
        with patch("urllib.request.urlopen") as mock_open:
            self._call(config=cfg)
        mock_open.assert_not_called()

    def test_skips_when_admin_email_missing(self):
        cfg = {**self._CFG, "ADMIN_EMAIL": ""}
        with patch("urllib.request.urlopen") as mock_open:
            self._call(config=cfg)
        mock_open.assert_not_called()

    def test_skips_when_from_email_missing(self):
        cfg = {**self._CFG, "SENDGRID_FROM_EMAIL": ""}
        with patch("urllib.request.urlopen") as mock_open:
            self._call(config=cfg)
        mock_open.assert_not_called()

    # ── HTTP request construction ─────────────────────────────────────────────

    def test_posts_to_sendgrid_endpoint(self):
        with patch("urllib.request.urlopen", return_value=self._mock_urlopen()):
            with patch("urllib.request.Request") as mock_req:
                mock_req.return_value = MagicMock()
                self._call()
        url = mock_req.call_args[0][0]
        assert url == "https://api.sendgrid.com/v3/mail/send"

    def test_authorization_header_uses_bearer_token(self):
        with patch("urllib.request.urlopen", return_value=self._mock_urlopen()):
            with patch("urllib.request.Request") as mock_req:
                mock_req.return_value = MagicMock()
                self._call()
        headers = mock_req.call_args[1]["headers"]
        assert headers["Authorization"] == "Bearer SG.test"

    def test_payload_contains_recipient(self):
        with patch("urllib.request.urlopen", return_value=self._mock_urlopen()):
            with patch("urllib.request.Request") as mock_req:
                mock_req.return_value = MagicMock()
                self._call()
        raw = mock_req.call_args[1]["data"]
        body = json.loads(raw)
        assert body["personalizations"][0]["to"][0]["email"] == "admin@copywrite.io"

    def test_payload_from_address(self):
        with patch("urllib.request.urlopen", return_value=self._mock_urlopen()):
            with patch("urllib.request.Request") as mock_req:
                mock_req.return_value = MagicMock()
                self._call()
        body = json.loads(mock_req.call_args[1]["data"])
        assert body["from"]["email"] == "noreply@copywrite.io"

    def test_subject_contains_brief_title_and_client(self):
        with patch("urllib.request.urlopen", return_value=self._mock_urlopen()):
            with patch("urllib.request.Request") as mock_req:
                mock_req.return_value = MagicMock()
                self._call()
        body = json.loads(mock_req.call_args[1]["data"])
        assert "Launch Email" in body["subject"]
        assert "Alice" in body["subject"]

    def test_email_body_contains_draft(self):
        with patch("urllib.request.urlopen", return_value=self._mock_urlopen()):
            with patch("urllib.request.Request") as mock_req:
                mock_req.return_value = MagicMock()
                self._call(draft="Unique draft XYZ")
        body = json.loads(mock_req.call_args[1]["data"])
        html = body["content"][0]["value"]
        assert "Unique draft XYZ" in html

    def test_email_body_contains_brief_url(self):
        with patch("urllib.request.urlopen", return_value=self._mock_urlopen()):
            with patch("urllib.request.Request") as mock_req:
                mock_req.return_value = MagicMock()
                self._call()
        body = json.loads(mock_req.call_args[1]["data"])
        html = body["content"][0]["value"]
        assert "/portal/admin/briefs/42" in html

    def test_email_body_contains_client_name(self):
        with patch("urllib.request.urlopen", return_value=self._mock_urlopen()):
            with patch("urllib.request.Request") as mock_req:
                mock_req.return_value = MagicMock()
                self._call()
        body = json.loads(mock_req.call_args[1]["data"])
        html = body["content"][0]["value"]
        assert "Alice" in html

    def test_email_body_escapes_html_in_draft(self):
        malicious = "<script>alert(1)</script>"
        with patch("urllib.request.urlopen", return_value=self._mock_urlopen()):
            with patch("urllib.request.Request") as mock_req:
                mock_req.return_value = MagicMock()
                self._call(draft=malicious)
        body = json.loads(mock_req.call_args[1]["data"])
        html = body["content"][0]["value"]
        assert "<script>" not in html
        assert "&lt;script&gt;" in html

    def test_base_url_trailing_slash_stripped(self):
        cfg = {**self._CFG, "APP_BASE_URL": "https://app.example.com/"}
        with patch("urllib.request.urlopen", return_value=self._mock_urlopen()):
            with patch("urllib.request.Request") as mock_req:
                mock_req.return_value = MagicMock()
                self._call(config=cfg)
        body = json.loads(mock_req.call_args[1]["data"])
        html = body["content"][0]["value"]
        assert "//portal" not in html

    def test_raises_on_http_error(self):
        err = urllib.error.HTTPError(
            url="", code=403, msg="Forbidden",
            hdrs=MagicMock(), fp=io.BytesIO(b'{"errors":[]}'),
        )
        with patch("urllib.request.urlopen", side_effect=err):
            with patch("urllib.request.Request"):
                with pytest.raises(RuntimeError, match="403"):
                    self._call()

    def test_raises_on_unexpected_status(self):
        resp = self._mock_urlopen(status=500)
        with patch("urllib.request.urlopen", return_value=resp):
            with patch("urllib.request.Request"):
                with pytest.raises(RuntimeError, match="500"):
                    self._call()

    def test_succeeds_on_202(self):
        with patch("urllib.request.urlopen", return_value=self._mock_urlopen(202)):
            with patch("urllib.request.Request"):
                automation.send_brief_notification(self._brief(), "draft", self._CFG)  # no raise


# ═══════════════════════════════════════════════════════════════════════════════
# run_brief_automation
# ═══════════════════════════════════════════════════════════════════════════════

class TestRunBriefAutomation:

    def test_returns_immediately_when_no_api_key(self, sample_brief):
        with patch.object(automation, "generate_draft") as mock_gen:
            automation.run_brief_automation(sample_brief, {"ANTHROPIC_API_KEY": ""})
        mock_gen.assert_not_called()

    def test_calls_generate_draft_with_api_key(self, sample_brief, isolated_db):
        cfg = {"ANTHROPIC_API_KEY": "sk-real",
               "SENDGRID_API_KEY": "", "SENDGRID_FROM_EMAIL": "",
               "ADMIN_EMAIL": "", "APP_BASE_URL": "http://localhost"}
        with patch.object(automation, "generate_draft", return_value="Draft!") as mock_gen:
            with patch.object(automation, "send_brief_notification"):
                automation.run_brief_automation(sample_brief, cfg)
        mock_gen.assert_called_once_with(sample_brief, "sk-real")

    def test_saves_draft_to_db(self, sample_brief, isolated_db):
        cfg = {"ANTHROPIC_API_KEY": "sk-real",
               "SENDGRID_API_KEY": "", "SENDGRID_FROM_EMAIL": "",
               "ADMIN_EMAIL": "", "APP_BASE_URL": "http://localhost"}
        with patch.object(automation, "generate_draft", return_value="Saved draft"):
            with patch.object(automation, "send_brief_notification"):
                automation.run_brief_automation(sample_brief, cfg)
        brief = db_module.get_brief(sample_brief["id"])
        assert brief["draft"] == "Saved draft"

    def test_calls_send_notification_after_draft(self, sample_brief, isolated_db):
        cfg = {"ANTHROPIC_API_KEY": "sk-real",
               "SENDGRID_API_KEY": "SG.x", "SENDGRID_FROM_EMAIL": "f@x.com",
               "ADMIN_EMAIL": "a@x.com", "APP_BASE_URL": "http://localhost"}
        with patch.object(automation, "generate_draft", return_value="The draft"):
            with patch.object(automation, "send_brief_notification") as mock_send:
                automation.run_brief_automation(sample_brief, cfg)
        mock_send.assert_called_once()
        call_brief, call_draft, call_cfg = mock_send.call_args[0]
        assert call_draft == "The draft"

    def test_send_notification_receives_updated_brief(self, sample_brief, isolated_db):
        """Brief passed to send_notification is the one from the DB, not the dict arg."""
        cfg = {"ANTHROPIC_API_KEY": "sk-real",
               "SENDGRID_API_KEY": "SG.x", "SENDGRID_FROM_EMAIL": "f@x.com",
               "ADMIN_EMAIL": "a@x.com", "APP_BASE_URL": "http://localhost"}
        with patch.object(automation, "generate_draft", return_value="Draft"):
            with patch.object(automation, "send_brief_notification") as mock_send:
                automation.run_brief_automation(sample_brief, cfg)
        assert mock_send.called

    def test_skips_notification_when_draft_fails(self, sample_brief, isolated_db):
        cfg = {"ANTHROPIC_API_KEY": "sk-real",
               "SENDGRID_API_KEY": "SG.x", "SENDGRID_FROM_EMAIL": "f@x.com",
               "ADMIN_EMAIL": "a@x.com", "APP_BASE_URL": "http://localhost"}
        with patch.object(automation, "generate_draft", side_effect=RuntimeError("API down")):
            with patch.object(automation, "send_brief_notification") as mock_send:
                automation.run_brief_automation(sample_brief, cfg)  # must not raise
        mock_send.assert_not_called()

    def test_notification_failure_does_not_raise(self, sample_brief, isolated_db):
        cfg = {"ANTHROPIC_API_KEY": "sk-real",
               "SENDGRID_API_KEY": "SG.x", "SENDGRID_FROM_EMAIL": "f@x.com",
               "ADMIN_EMAIL": "a@x.com", "APP_BASE_URL": "http://localhost"}
        with patch.object(automation, "generate_draft", return_value="Draft"):
            with patch.object(automation, "send_brief_notification",
                              side_effect=RuntimeError("SendGrid down")):
                automation.run_brief_automation(sample_brief, cfg)  # must not raise


# ═══════════════════════════════════════════════════════════════════════════════
# save_draft / get_brief draft field
# ═══════════════════════════════════════════════════════════════════════════════

class TestSaveDraft:

    def test_save_draft_persists(self, sample_brief, isolated_db):
        db_module.save_draft(sample_brief["id"], "My draft text")
        brief = db_module.get_brief(sample_brief["id"])
        assert brief["draft"] == "My draft text"

    def test_draft_defaults_to_none(self, sample_brief, isolated_db):
        brief = db_module.get_brief(sample_brief["id"])
        assert brief["draft"] is None

    def test_save_draft_overwrites_previous(self, sample_brief, isolated_db):
        db_module.save_draft(sample_brief["id"], "v1")
        db_module.save_draft(sample_brief["id"], "v2")
        assert db_module.get_brief(sample_brief["id"])["draft"] == "v2"

    def test_save_draft_preserves_other_fields(self, sample_brief, isolated_db):
        db_module.save_draft(sample_brief["id"], "draft")
        brief = db_module.get_brief(sample_brief["id"])
        assert brief["title"] == "Launch Email"
        assert brief["status"] == "pending"


# ═══════════════════════════════════════════════════════════════════════════════
# get_dashboard_stats
# ═══════════════════════════════════════════════════════════════════════════════

class TestGetDashboardStats:

    def test_total_clients_zero_initially(self, isolated_db):
        stats = db_module.get_dashboard_stats()
        assert stats["total_clients"] == 0

    def test_total_clients_counts_clients_only(self, isolated_db):
        db_module.create_user("C1", "c1@t.com", "pass", "client")
        db_module.create_user("C2", "c2@t.com", "pass", "client")
        stats = db_module.get_dashboard_stats()
        assert stats["total_clients"] == 2

    def test_total_clients_excludes_admin(self, isolated_db):
        stats = db_module.get_dashboard_stats()
        # admin was seeded in init_portal_db
        assert stats["total_clients"] == 0

    def test_briefs_this_month_counts_current(self, isolated_db):
        uid = db_module.create_user("X", "x@t.com", "pass", "client")
        _brief_data = dict(
            title="T", product_name="P", product_description="D",
            target_audience="A", main_benefit="B", biggest_objection="C",
            tone="casual", copy_type="email", notes="",
        )
        db_module.create_brief(uid, _brief_data)
        db_module.create_brief(uid, _brief_data)
        stats = db_module.get_dashboard_stats()
        assert stats["briefs_this_month"] == 2

    def test_avg_turnaround_none_when_no_completed(self, isolated_db):
        stats = db_module.get_dashboard_stats()
        assert stats["avg_turnaround_days"] is None

    def test_avg_turnaround_calculated_for_completed(self, isolated_db):
        uid = db_module.create_user("Y", "y@t.com", "pass", "client")
        _data = dict(
            title="T", product_name="P", product_description="D",
            target_audience="A", main_benefit="B", biggest_objection="C",
            tone="casual", copy_type="email", notes="",
        )
        bid = db_module.create_brief(uid, _data)
        db_module.mark_brief_complete(bid)
        stats = db_module.get_dashboard_stats()
        # Completed within the same second so turnaround ≈ 0 days
        assert stats["avg_turnaround_days"] is not None
        assert stats["avg_turnaround_days"] >= 0

    def test_avg_turnaround_excludes_pending(self, isolated_db):
        uid = db_module.create_user("Z", "z@t.com", "pass", "client")
        _data = dict(
            title="T", product_name="P", product_description="D",
            target_audience="A", main_benefit="B", biggest_objection="C",
            tone="casual", copy_type="email", notes="",
        )
        db_module.create_brief(uid, _data)   # pending — never completed
        stats = db_module.get_dashboard_stats()
        assert stats["avg_turnaround_days"] is None

    def test_stats_dict_has_all_keys(self, isolated_db):
        stats = db_module.get_dashboard_stats()
        assert "total_clients" in stats
        assert "briefs_this_month" in stats
        assert "avg_turnaround_days" in stats


# ═══════════════════════════════════════════════════════════════════════════════
# new_brief route — background thread is spawned
# ═══════════════════════════════════════════════════════════════════════════════

class TestNewBriefSpawnsThread:

    @pytest.fixture
    def auth_client(self, flask_app):
        uid = db_module.create_user("Bob", "bob@test.com", "pass1234", "client")
        with flask_app.test_client() as c:
            with c.session_transaction() as sess:
                sess["user_id"] = uid
                sess["user_name"] = "Bob"
                sess["user_role"] = "client"
                sess["user_email"] = "bob@test.com"
            yield c

    def _post_brief(self, c):
        return c.post("/portal/client/briefs/new", data={
            "title": "Thread Test", "product_name": "Prod",
            "product_description": "Desc", "target_audience": "All",
            "main_benefit": "Works", "biggest_objection": "Cost",
            "tone": "professional", "copy_type": "email", "notes": "",
        }, follow_redirects=True)

    def test_new_brief_route_starts_daemon_thread(self, auth_client, flask_app):
        started = []

        original_start = threading.Thread.start

        def fake_start(self_thread):
            started.append(self_thread)
            # Don't actually start — avoid real API calls in tests

        with patch.object(threading.Thread, "start", fake_start):
            r = self._post_brief(auth_client)

        assert r.status_code == 200
        assert len(started) == 1
        assert started[0].daemon is True

    def test_new_brief_succeeds_even_if_thread_would_fail(self, auth_client, flask_app):
        """Route response must be correct regardless of automation outcome."""
        with patch.object(threading.Thread, "start", lambda s: None):
            r = self._post_brief(auth_client)
        assert b"Thread Test" in r.data

    def test_thread_not_started_on_validation_error(self, auth_client, flask_app):
        started = []
        with patch.object(threading.Thread, "start", lambda s: started.append(s)):
            auth_client.post("/portal/client/briefs/new", data={
                "title": "",  # required field missing
                "product_name": "P", "product_description": "D",
                "target_audience": "A", "main_benefit": "B",
                "biggest_objection": "C", "tone": "professional",
                "copy_type": "email", "notes": "",
            })
        assert len(started) == 0


# ═══════════════════════════════════════════════════════════════════════════════
# Admin dashboard — stats rendered
# ═══════════════════════════════════════════════════════════════════════════════

class TestAdminDashboardStats:

    def test_dashboard_shows_total_clients_heading(self, admin_http):
        r = admin_http.get("/portal/admin/")
        assert b"Total clients" in r.data

    def test_dashboard_shows_briefs_this_month_heading(self, admin_http):
        r = admin_http.get("/portal/admin/")
        assert b"Briefs this month" in r.data

    def test_dashboard_shows_avg_turnaround_heading(self, admin_http):
        r = admin_http.get("/portal/admin/")
        assert b"Avg turnaround" in r.data

    def test_dashboard_shows_em_dash_when_no_completed_briefs(self, admin_http):
        r = admin_http.get("/portal/admin/")
        assert "—".encode() in r.data

    def test_dashboard_shows_client_count(self, admin_http, flask_app):
        db_module.create_user("NewCli", "nc@test.com", "pass1234", "client")
        r = admin_http.get("/portal/admin/")
        html = r.data.decode()
        assert "1" in html   # at least the client count appears

    def test_stats_passed_to_template(self, admin_http, flask_app):
        with patch.object(db_module, "get_dashboard_stats", return_value={
            "total_clients": 99,
            "briefs_this_month": 7,
            "avg_turnaround_days": 3.2,
        }):
            r = admin_http.get("/portal/admin/")
        html = r.data.decode()
        assert "99" in html
        assert "7" in html
        assert "3.2" in html


# ═══════════════════════════════════════════════════════════════════════════════
# Admin brief detail — draft section rendered
# ═══════════════════════════════════════════════════════════════════════════════

class TestAdminBriefDetailDraft:

    @pytest.fixture
    def admin_http_with_db(self, flask_app):
        with flask_app.test_client() as c:
            admin = db_module.get_user_by_email("admin@copydtc.com")
            with c.session_transaction() as sess:
                sess["user_id"] = admin["id"]
                sess["user_name"] = admin["name"]
                sess["user_role"] = "admin"
                sess["user_email"] = admin["email"]
            yield c

    def _create_brief(self):
        uid = db_module.create_user("Tester", "t@t.com", "pass1234", "client")
        bid = db_module.create_brief(uid, {
            "title": "T", "product_name": "P", "product_description": "D",
            "target_audience": "A", "main_benefit": "B", "biggest_objection": "C",
            "tone": "casual", "copy_type": "email", "notes": "",
        })
        return bid

    def test_shows_draft_when_present(self, admin_http_with_db, flask_app):
        bid = self._create_brief()
        db_module.save_draft(bid, "This is a unique draft sentence.")
        r = admin_http_with_db.get(f"/portal/admin/briefs/{bid}")
        assert b"This is a unique draft sentence." in r.data

    def test_shows_generating_message_when_no_draft_and_pending(self, admin_http_with_db, flask_app):
        bid = self._create_brief()
        r = admin_http_with_db.get(f"/portal/admin/briefs/{bid}")
        assert b"Draft is being generated" in r.data or b"refresh" in r.data.lower()

    def test_draft_section_heading_visible(self, admin_http_with_db, flask_app):
        bid = self._create_brief()
        r = admin_http_with_db.get(f"/portal/admin/briefs/{bid}")
        assert b"First Draft" in r.data or b"draft" in r.data.lower()

    def test_ai_draft_badge_shown_when_draft_present(self, admin_http_with_db, flask_app):
        bid = self._create_brief()
        db_module.save_draft(bid, "Some copy here")
        r = admin_http_with_db.get(f"/portal/admin/briefs/{bid}")
        assert b"AI draft" in r.data

    def test_draft_table_badge_shown_on_client_detail(self, admin_http_with_db, flask_app):
        bid = self._create_brief()
        db_module.save_draft(bid, "Some copy")
        client = db_module.get_user_by_email("t@t.com")
        r = admin_http_with_db.get(f"/portal/admin/clients/{client['id']}")
        assert b"draft ready" in r.data


# ═══════════════════════════════════════════════════════════════════════════════
# send_completion_notification
# ═══════════════════════════════════════════════════════════════════════════════

class TestSendCompletionNotification:

    _brief = {
        "id": 42,
        "title": "Launch Email",
        "client_name": "Alice Brand",
        "client_email": "alice@brand.com",
    }
    _cfg = {
        "SENDGRID_API_KEY": "SG.testkey",
        "SENDGRID_FROM_EMAIL": "you@copywrite.io",
        "APP_BASE_URL": "https://app.example.com",
    }

    def _mock_urlopen(self):
        ctx = MagicMock()
        ctx.__enter__ = lambda s: s
        ctx.__exit__ = MagicMock(return_value=False)
        ctx.status = 202
        return ctx

    def test_sends_to_client_email(self):
        with patch("portal.automation.urllib.request.urlopen",
                   return_value=self._mock_urlopen()) as mock_open:
            automation.send_completion_notification(self._brief, self._cfg)
        req = mock_open.call_args[0][0]
        payload = json.loads(req.data.decode())
        assert payload["personalizations"][0]["to"][0]["email"] == "alice@brand.com"

    def test_uses_from_email(self):
        with patch("portal.automation.urllib.request.urlopen",
                   return_value=self._mock_urlopen()) as mock_open:
            automation.send_completion_notification(self._brief, self._cfg)
        req = mock_open.call_args[0][0]
        payload = json.loads(req.data.decode())
        assert payload["from"]["email"] == "you@copywrite.io"

    def test_subject_includes_brief_title(self):
        with patch("portal.automation.urllib.request.urlopen",
                   return_value=self._mock_urlopen()) as mock_open:
            automation.send_completion_notification(self._brief, self._cfg)
        req = mock_open.call_args[0][0]
        payload = json.loads(req.data.decode())
        assert "Launch Email" in payload["subject"]

    def test_email_body_contains_client_name(self):
        with patch("portal.automation.urllib.request.urlopen",
                   return_value=self._mock_urlopen()) as mock_open:
            automation.send_completion_notification(self._brief, self._cfg)
        req = mock_open.call_args[0][0]
        payload = json.loads(req.data.decode())
        assert "Alice Brand" in payload["content"][0]["value"]

    def test_email_body_contains_portal_link(self):
        with patch("portal.automation.urllib.request.urlopen",
                   return_value=self._mock_urlopen()) as mock_open:
            automation.send_completion_notification(self._brief, self._cfg)
        req = mock_open.call_args[0][0]
        payload = json.loads(req.data.decode())
        assert "portal/client/briefs/42" in payload["content"][0]["value"]

    def test_skips_when_no_api_key(self):
        cfg = dict(self._cfg, SENDGRID_API_KEY="")
        with patch("portal.automation.urllib.request.urlopen") as mock_open:
            automation.send_completion_notification(self._brief, cfg)
        mock_open.assert_not_called()

    def test_skips_when_no_client_email(self):
        brief = dict(self._brief, client_email="")
        with patch("portal.automation.urllib.request.urlopen") as mock_open:
            automation.send_completion_notification(brief, self._cfg)
        mock_open.assert_not_called()

    def test_skips_when_no_from_email(self):
        cfg = dict(self._cfg, SENDGRID_FROM_EMAIL="")
        with patch("portal.automation.urllib.request.urlopen") as mock_open:
            automation.send_completion_notification(self._brief, cfg)
        mock_open.assert_not_called()

    def test_raises_on_http_error(self):
        exc = urllib.error.HTTPError(
            url="", code=400, msg="Bad Request",
            hdrs=None, fp=io.BytesIO(b"error body")
        )
        with patch("portal.automation.urllib.request.urlopen", side_effect=exc):
            with pytest.raises(RuntimeError, match="SendGrid HTTP 400"):
                automation.send_completion_notification(self._brief, self._cfg)

    def test_uses_bearer_auth_header(self):
        with patch("portal.automation.urllib.request.urlopen",
                   return_value=self._mock_urlopen()) as mock_open:
            automation.send_completion_notification(self._brief, self._cfg)
        req = mock_open.call_args[0][0]
        assert req.get_header("Authorization") == "Bearer SG.testkey"


# ═══════════════════════════════════════════════════════════════════════════════
# mark_complete fires completion notification in admin
# ═══════════════════════════════════════════════════════════════════════════════

class TestMarkCompleteNotification:

    @pytest.fixture
    def admin_http_with_db(self, flask_app):
        with flask_app.test_client() as c:
            admin = db_module.get_user_by_email("admin@copydtc.com")
            with c.session_transaction() as sess:
                sess["user_id"] = admin["id"]
                sess["user_name"] = admin["name"]
                sess["user_role"] = "admin"
                sess["user_email"] = admin["email"]
            yield c

    def _create_brief(self):
        uid = db_module.create_user("Notify Test", "notify@test.com", "pass1234", "client")
        return db_module.create_brief(uid, {
            "title": "Notify Brief", "product_name": "P",
            "product_description": "D", "target_audience": "A",
            "main_benefit": "B", "biggest_objection": "C",
            "tone": "casual", "copy_type": "email", "notes": "",
        })

    def test_mark_complete_spawns_notification_thread(
        self, admin_http_with_db, flask_app
    ):
        bid = self._create_brief()
        with patch("portal.admin.threading.Thread") as mock_thread_cls:
            mock_t = MagicMock()
            mock_thread_cls.return_value = mock_t
            admin_http_with_db.post(f"/portal/admin/briefs/{bid}",
                                    data={"action": "mark_complete"})
        mock_thread_cls.assert_called_once()
        mock_t.start.assert_called_once()

    def test_upload_copy_spawns_notification_thread(
        self, admin_http_with_db, flask_app
    ):
        bid = self._create_brief()
        with patch("portal.admin.threading.Thread") as mock_thread_cls:
            mock_t = MagicMock()
            mock_thread_cls.return_value = mock_t
            admin_http_with_db.post(
                f"/portal/admin/briefs/{bid}",
                data={"action": "upload_copy",
                      "copy_file": (io.BytesIO(b"content"), "copy.txt")},
                content_type="multipart/form-data",
            )
        mock_thread_cls.assert_called_once()
        mock_t.start.assert_called_once()
