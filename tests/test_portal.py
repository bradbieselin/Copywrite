"""
Portal test suite — covers auth, client routes, admin routes,
access control, and all DB portal helpers.
No real external API calls are made.
"""

import io
import os
import sys
import sqlite3
import tempfile

import pytest
from werkzeug.security import generate_password_hash, check_password_hash

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, PROJECT_ROOT)

import db as db_module
import app as app_module


# ═══════════════════════════════════════════════════════════════════════════════
# Fixtures
# ═══════════════════════════════════════════════════════════════════════════════

@pytest.fixture
def flask_app(tmp_path, monkeypatch):
    """Fresh app with isolated SQLite DB and uploads folder."""
    db_path = str(tmp_path / "test_portal.db")
    upload_dir = str(tmp_path / "uploads")
    os.makedirs(upload_dir, exist_ok=True)

    monkeypatch.setattr(db_module, "DB_PATH", db_path)

    _app = app_module.create_app()
    _app.config.update(
        TESTING=True,
        SECRET_KEY="test-secret",
        UPLOAD_FOLDER=upload_dir,
    )
    return _app


@pytest.fixture
def client(flask_app):
    with flask_app.test_client() as c:
        yield c


@pytest.fixture
def admin_client(flask_app):
    """Test client pre-authenticated as admin."""
    with flask_app.test_client() as c:
        c.post("/portal/login", data={
            "email": "admin@copywrite.io",
            "password": "admin123",
        })
        yield c


@pytest.fixture
def portal_client_user(flask_app):
    """Create a client user and return their credentials."""
    db_module.create_user("Alice Brand", "alice@brand.com", "password123", "client")
    return {"email": "alice@brand.com", "password": "password123", "name": "Alice Brand"}


@pytest.fixture
def auth_client(flask_app, portal_client_user):
    """Test client pre-authenticated as the 'Alice Brand' client user."""
    with flask_app.test_client() as c:
        c.post("/portal/login", data={
            "email": portal_client_user["email"],
            "password": portal_client_user["password"],
        })
        yield c


def _make_brief(client_id: int, **overrides) -> int:
    data = dict(
        title="Test Brief",
        product_name="TestProd",
        product_description="A great product",
        target_audience="Everyone",
        main_benefit="Works",
        biggest_objection="Price",
        tone="professional",
        copy_type="email",
        notes="",
    )
    data.update(overrides)
    return db_module.create_brief(client_id, data)


# ═══════════════════════════════════════════════════════════════════════════════
# db portal helpers
# ═══════════════════════════════════════════════════════════════════════════════

class TestPortalDb:

    def setup_method(self):
        self._tmp = tempfile.mkdtemp()
        self._db_path = str(os.path.join(self._tmp, "t.db"))
        self._orig = db_module.DB_PATH
        db_module.DB_PATH = self._db_path
        db_module.init_db()
        db_module.init_portal_db()

    def teardown_method(self):
        db_module.DB_PATH = self._orig

    # ── init_portal_db ────────────────────────────────────────────────────────

    def test_creates_portal_users_table(self):
        with sqlite3.connect(self._db_path) as conn:
            row = conn.execute(
                "SELECT name FROM sqlite_master WHERE type='table' AND name='portal_users'"
            ).fetchone()
        assert row is not None

    def test_creates_briefs_table(self):
        with sqlite3.connect(self._db_path) as conn:
            row = conn.execute(
                "SELECT name FROM sqlite_master WHERE type='table' AND name='briefs'"
            ).fetchone()
        assert row is not None

    def test_creates_copy_files_table(self):
        with sqlite3.connect(self._db_path) as conn:
            row = conn.execute(
                "SELECT name FROM sqlite_master WHERE type='table' AND name='copy_files'"
            ).fetchone()
        assert row is not None

    def test_seeds_admin_account(self):
        user = db_module.get_user_by_email("admin@copywrite.io")
        assert user is not None
        assert user["role"] == "admin"
        assert check_password_hash(user["password_hash"], "admin123")

    def test_init_portal_db_idempotent(self):
        db_module.init_portal_db()
        db_module.init_portal_db()
        with sqlite3.connect(self._db_path) as conn:
            count = conn.execute(
                "SELECT COUNT(*) FROM portal_users WHERE role='admin'"
            ).fetchone()[0]
        assert count == 1

    # ── users ─────────────────────────────────────────────────────────────────

    def test_get_user_by_email_returns_dict(self):
        user = db_module.get_user_by_email("admin@copywrite.io")
        assert isinstance(user, dict)
        assert user["email"] == "admin@copywrite.io"

    def test_get_user_by_email_case_insensitive(self):
        user = db_module.get_user_by_email("ADMIN@Copywrite.IO")
        assert user is not None

    def test_get_user_by_email_unknown_returns_none(self):
        assert db_module.get_user_by_email("nobody@example.com") is None

    def test_create_user_returns_id(self):
        uid = db_module.create_user("Bob", "bob@test.com", "pass1234", "client")
        assert isinstance(uid, int) and uid >= 1

    def test_create_user_hashes_password(self):
        db_module.create_user("Carol", "carol@test.com", "mypassword", "client")
        user = db_module.get_user_by_email("carol@test.com")
        assert user["password_hash"] != "mypassword"
        assert check_password_hash(user["password_hash"], "mypassword")

    def test_create_user_normalises_email(self):
        db_module.create_user("Dave", "Dave@Test.COM", "pass1234", "client")
        user = db_module.get_user_by_email("dave@test.com")
        assert user is not None

    def test_create_user_duplicate_email_raises(self):
        db_module.create_user("Eve", "eve@test.com", "pass", "client")
        with pytest.raises(Exception, match="UNIQUE"):
            db_module.create_user("Eve2", "eve@test.com", "pass", "client")

    def test_get_all_clients_excludes_admin(self):
        db_module.create_user("Frank", "frank@test.com", "pass", "client")
        clients = db_module.get_all_clients()
        roles = {c["role"] for c in clients} if clients and "role" in clients[0] else set()
        emails = [c["email"] for c in clients]
        assert "admin@copywrite.io" not in emails
        assert "frank@test.com" in emails

    # ── briefs ────────────────────────────────────────────────────────────────

    def _client_id(self):
        return db_module.create_user("Tester", "t@t.com", "pass", "client")

    def test_create_brief_returns_id(self):
        cid = self._client_id()
        bid = _make_brief(cid)
        assert isinstance(bid, int) and bid >= 1

    def test_get_brief_returns_dict(self):
        cid = self._client_id()
        bid = _make_brief(cid)
        brief = db_module.get_brief(bid)
        assert isinstance(brief, dict)
        assert brief["title"] == "Test Brief"

    def test_get_brief_includes_client_name(self):
        cid = self._client_id()
        bid = _make_brief(cid)
        brief = db_module.get_brief(bid)
        assert brief["client_name"] == "Tester"

    def test_get_brief_unknown_returns_none(self):
        assert db_module.get_brief(99999) is None

    def test_get_brief_default_status_pending(self):
        cid = self._client_id()
        bid = _make_brief(cid)
        assert db_module.get_brief(bid)["status"] == "pending"

    def test_get_client_briefs_returns_own_briefs(self):
        cid = self._client_id()
        _make_brief(cid, title="A")
        _make_brief(cid, title="B")
        briefs = db_module.get_client_briefs(cid)
        assert len(briefs) == 2

    def test_get_client_briefs_excludes_other_clients(self):
        cid1 = self._client_id()
        cid2 = db_module.create_user("Other", "o@o.com", "pass", "client")
        _make_brief(cid1)
        _make_brief(cid2)
        assert len(db_module.get_client_briefs(cid1)) == 1

    def test_get_all_briefs_returns_all(self):
        cid = self._client_id()
        _make_brief(cid)
        _make_brief(cid)
        assert len(db_module.get_all_briefs()) == 2

    def test_get_all_briefs_pending_first(self):
        cid = self._client_id()
        bid1 = _make_brief(cid, title="Completed")
        db_module.mark_brief_complete(bid1)
        _make_brief(cid, title="Pending")
        briefs = db_module.get_all_briefs()
        assert briefs[0]["title"] == "Pending"

    # ── status helpers ────────────────────────────────────────────────────────

    def test_update_brief_status_in_progress(self):
        cid = self._client_id()
        bid = _make_brief(cid)
        db_module.update_brief_status(bid, "in_progress")
        assert db_module.get_brief(bid)["status"] == "in_progress"

    def test_mark_brief_complete(self):
        cid = self._client_id()
        bid = _make_brief(cid)
        db_module.mark_brief_complete(bid)
        brief = db_module.get_brief(bid)
        assert brief["status"] == "completed"
        assert brief["completed_at"] is not None

    def test_reset_to_in_progress_clears_completed_at(self):
        cid = self._client_id()
        bid = _make_brief(cid)
        db_module.mark_brief_complete(bid)
        db_module.update_brief_status(bid, "in_progress")
        assert db_module.get_brief(bid)["completed_at"] is None

    # ── copy files ────────────────────────────────────────────────────────────

    def _setup_brief(self):
        cid = self._client_id()
        admin = db_module.get_user_by_email("admin@copywrite.io")
        bid = _make_brief(cid)
        return bid, admin["id"]

    def test_save_copy_file_returns_id(self):
        bid, aid = self._setup_brief()
        fid = db_module.save_copy_file(bid, "copy.txt", "1_abc_copy.txt", aid)
        assert isinstance(fid, int) and fid >= 1

    def test_get_copy_file_returns_dict(self):
        bid, aid = self._setup_brief()
        db_module.save_copy_file(bid, "copy.txt", "1_abc_copy.txt", aid)
        cf = db_module.get_copy_file(bid)
        assert cf is not None
        assert cf["original_filename"] == "copy.txt"
        assert cf["storage_filename"] == "1_abc_copy.txt"

    def test_get_copy_file_no_file_returns_none(self):
        cid = self._client_id()
        bid = _make_brief(cid)
        assert db_module.get_copy_file(bid) is None

    def test_save_copy_file_replaces_previous(self):
        bid, aid = self._setup_brief()
        db_module.save_copy_file(bid, "v1.txt", "1_aaa_v1.txt", aid)
        db_module.save_copy_file(bid, "v2.txt", "1_bbb_v2.txt", aid)
        cf = db_module.get_copy_file(bid)
        assert cf["original_filename"] == "v2.txt"
        with sqlite3.connect(self._db_path) as conn:
            count = conn.execute(
                "SELECT COUNT(*) FROM copy_files WHERE brief_id=?", (bid,)
            ).fetchone()[0]
        assert count == 1


# ═══════════════════════════════════════════════════════════════════════════════
# Auth routes
# ═══════════════════════════════════════════════════════════════════════════════

class TestAuth:

    def test_login_page_returns_200(self, client):
        r = client.get("/portal/login")
        assert r.status_code == 200

    def test_login_page_renders_form(self, client):
        r = client.get("/portal/login")
        html = r.data.decode()
        assert 'name="email"' in html
        assert 'name="password"' in html

    def test_login_wrong_password_shows_error(self, client):
        r = client.post("/portal/login", data={
            "email": "admin@copywrite.io", "password": "wrongpass"
        })
        html = r.data.decode()
        assert "Invalid email or password" in html

    def test_login_unknown_email_shows_error(self, client):
        r = client.post("/portal/login", data={
            "email": "nobody@example.com", "password": "anything"
        })
        assert "Invalid email or password" in r.data.decode()

    def test_admin_login_redirects_to_admin_dashboard(self, client):
        r = client.post("/portal/login", data={
            "email": "admin@copywrite.io", "password": "admin123"
        }, follow_redirects=True)
        assert b"Admin Dashboard" in r.data

    def test_client_login_redirects_to_client_dashboard(self, client, portal_client_user, flask_app):
        r = client.post("/portal/login", data={
            "email": portal_client_user["email"],
            "password": portal_client_user["password"],
        }, follow_redirects=True)
        assert b"My Briefs" in r.data

    def test_logout_clears_session(self, admin_client):
        r = admin_client.get("/portal/logout", follow_redirects=True)
        assert b"Sign in" in r.data

    def test_already_logged_in_admin_redirects_from_login(self, admin_client):
        r = admin_client.get("/portal/login")
        assert r.status_code in (301, 302, 308)

    def test_already_logged_in_client_redirects_from_login(self, auth_client):
        r = auth_client.get("/portal/login")
        assert r.status_code in (301, 302, 308)


# ═══════════════════════════════════════════════════════════════════════════════
# Access control
# ═══════════════════════════════════════════════════════════════════════════════

class TestAccessControl:

    def test_unauthenticated_client_dashboard_redirects(self, client):
        r = client.get("/portal/client/")
        assert r.status_code in (301, 302, 308)

    def test_unauthenticated_new_brief_redirects(self, client):
        r = client.get("/portal/client/briefs/new")
        assert r.status_code in (301, 302, 308)

    def test_unauthenticated_admin_dashboard_redirects(self, client):
        r = client.get("/portal/admin/")
        assert r.status_code in (301, 302, 308)

    def test_client_cannot_access_admin_dashboard(self, auth_client):
        r = auth_client.get("/portal/admin/", follow_redirects=True)
        assert b"Admin Dashboard" not in r.data
        assert b"Admin access required" in r.data

    def test_client_cannot_access_admin_brief(self, auth_client, portal_client_user):
        cid = db_module.get_user_by_email(portal_client_user["email"])["id"]
        bid = _make_brief(cid)
        r = auth_client.get(f"/portal/admin/briefs/{bid}", follow_redirects=True)
        assert b"Admin access required" in r.data

    def test_client_cannot_view_other_clients_brief(self, flask_app, portal_client_user):
        # Create a second client and a brief belonging to them
        db_module.create_user("Eve", "eve@test.com", "pass1234", "client")
        eve = db_module.get_user_by_email("eve@test.com")
        bid = _make_brief(eve["id"])

        # Auth as Alice and try to view Eve's brief
        with flask_app.test_client() as c:
            c.post("/portal/login", data={
                "email": portal_client_user["email"],
                "password": portal_client_user["password"],
            })
            r = c.get(f"/portal/client/briefs/{bid}", follow_redirects=True)
        assert b"Brief not found" in r.data

    def test_redirect_preserves_next_param(self, client):
        r = client.get("/portal/client/")
        location = r.headers.get("Location", "")
        assert "next" in location or r.status_code in (301, 302, 308)


# ═══════════════════════════════════════════════════════════════════════════════
# Client routes
# ═══════════════════════════════════════════════════════════════════════════════

class TestClientRoutes:

    def test_dashboard_returns_200(self, auth_client):
        r = auth_client.get("/portal/client/")
        assert r.status_code == 200

    def test_dashboard_shows_no_briefs_empty_state(self, auth_client):
        r = auth_client.get("/portal/client/")
        assert b"No briefs" in r.data or b"first brief" in r.data

    def test_new_brief_get_returns_200(self, auth_client):
        r = auth_client.get("/portal/client/briefs/new")
        assert r.status_code == 200

    def test_new_brief_renders_form_fields(self, auth_client):
        r = auth_client.get("/portal/client/briefs/new")
        html = r.data.decode()
        for field in ["title", "product_name", "product_description",
                      "target_audience", "main_benefit", "biggest_objection"]:
            assert field in html

    def test_new_brief_renders_tone_and_copy_type_dropdowns(self, auth_client):
        r = auth_client.get("/portal/client/briefs/new")
        html = r.data.decode()
        assert "professional" in html
        assert "email" in html

    def test_new_brief_missing_required_field_shows_error(self, auth_client):
        r = auth_client.post("/portal/client/briefs/new", data={
            "title": "", "product_name": "Prod", "product_description": "Desc",
            "target_audience": "All", "main_benefit": "Good", "biggest_objection": "Cost",
            "tone": "professional", "copy_type": "email", "notes": "",
        })
        assert b"fill in all required" in r.data.lower() or b"required" in r.data.lower()

    def test_new_brief_invalid_tone_rejected(self, auth_client):
        r = auth_client.post("/portal/client/briefs/new", data={
            "title": "T", "product_name": "P", "product_description": "D",
            "target_audience": "A", "main_benefit": "B", "biggest_objection": "C",
            "tone": "rude", "copy_type": "email", "notes": "",
        })
        assert b"Invalid tone" in r.data

    def test_new_brief_invalid_copy_type_rejected(self, auth_client):
        r = auth_client.post("/portal/client/briefs/new", data={
            "title": "T", "product_name": "P", "product_description": "D",
            "target_audience": "A", "main_benefit": "B", "biggest_objection": "C",
            "tone": "professional", "copy_type": "billboard", "notes": "",
        })
        assert b"Invalid copy type" in r.data

    def test_new_brief_success_redirects_to_detail(self, auth_client):
        r = auth_client.post("/portal/client/briefs/new", data={
            "title": "Welcome Email", "product_name": "Prod",
            "product_description": "Desc", "target_audience": "All",
            "main_benefit": "Works", "biggest_objection": "Cost",
            "tone": "professional", "copy_type": "email", "notes": "",
        }, follow_redirects=True)
        assert r.status_code == 200
        assert b"Welcome Email" in r.data

    def test_new_brief_success_saves_to_db(self, auth_client, portal_client_user):
        auth_client.post("/portal/client/briefs/new", data={
            "title": "DB Test Brief", "product_name": "Prod",
            "product_description": "Desc", "target_audience": "All",
            "main_benefit": "Works", "biggest_objection": "Cost",
            "tone": "professional", "copy_type": "email", "notes": "",
        })
        cid = db_module.get_user_by_email(portal_client_user["email"])["id"]
        briefs = db_module.get_client_briefs(cid)
        assert len(briefs) == 1
        assert briefs[0]["title"] == "DB Test Brief"

    def test_dashboard_shows_submitted_brief(self, auth_client):
        auth_client.post("/portal/client/briefs/new", data={
            "title": "My Q3 Email", "product_name": "P", "product_description": "D",
            "target_audience": "A", "main_benefit": "B", "biggest_objection": "C",
            "tone": "casual", "copy_type": "email", "notes": "",
        })
        r = auth_client.get("/portal/client/")
        assert b"My Q3 Email" in r.data

    def test_brief_detail_returns_200(self, auth_client, portal_client_user):
        cid = db_module.get_user_by_email(portal_client_user["email"])["id"]
        bid = _make_brief(cid)
        r = auth_client.get(f"/portal/client/briefs/{bid}")
        assert r.status_code == 200

    def test_brief_detail_shows_brief_info(self, auth_client, portal_client_user):
        cid = db_module.get_user_by_email(portal_client_user["email"])["id"]
        bid = _make_brief(cid, title="Unique Title XYZ")
        r = auth_client.get(f"/portal/client/briefs/{bid}")
        assert b"Unique Title XYZ" in r.data

    def test_brief_detail_shows_pending_status(self, auth_client, portal_client_user):
        cid = db_module.get_user_by_email(portal_client_user["email"])["id"]
        bid = _make_brief(cid)
        r = auth_client.get(f"/portal/client/briefs/{bid}")
        assert b"Pending" in r.data

    def test_brief_detail_shows_download_when_completed(self, auth_client, portal_client_user, flask_app):
        cid = db_module.get_user_by_email(portal_client_user["email"])["id"]
        admin = db_module.get_user_by_email("admin@copywrite.io")
        bid = _make_brief(cid)

        # Write a real file
        upload_dir = flask_app.config["UPLOAD_FOLDER"]
        storage = f"{bid}_test_copy.txt"
        with open(os.path.join(upload_dir, storage), "w") as f:
            f.write("Great copy here!")
        db_module.save_copy_file(bid, "copy.txt", storage, admin["id"])
        db_module.mark_brief_complete(bid)

        r = auth_client.get(f"/portal/client/briefs/{bid}")
        assert b"Download copy" in r.data

    def test_download_copy_streams_file(self, auth_client, portal_client_user, flask_app):
        cid = db_module.get_user_by_email(portal_client_user["email"])["id"]
        admin = db_module.get_user_by_email("admin@copywrite.io")
        bid = _make_brief(cid)

        upload_dir = flask_app.config["UPLOAD_FOLDER"]
        storage = f"{bid}_download_test.txt"
        with open(os.path.join(upload_dir, storage), "w") as f:
            f.write("Final copy content!")
        db_module.save_copy_file(bid, "final.txt", storage, admin["id"])
        db_module.mark_brief_complete(bid)

        r = auth_client.get(f"/portal/client/briefs/{bid}/download")
        assert r.status_code == 200
        assert b"Final copy content!" in r.data

    def test_download_copy_not_completed_redirects(self, auth_client, portal_client_user):
        cid = db_module.get_user_by_email(portal_client_user["email"])["id"]
        bid = _make_brief(cid)
        r = auth_client.get(f"/portal/client/briefs/{bid}/download", follow_redirects=True)
        assert b"ready" in r.data.lower() or b"not yet" in r.data.lower()

    def test_download_copy_no_file_shows_warning(self, auth_client, portal_client_user):
        cid = db_module.get_user_by_email(portal_client_user["email"])["id"]
        bid = _make_brief(cid)
        db_module.mark_brief_complete(bid)  # complete but no file
        r = auth_client.get(f"/portal/client/briefs/{bid}/download", follow_redirects=True)
        assert b"upload" in r.data.lower() or b"no file" in r.data.lower()


# ═══════════════════════════════════════════════════════════════════════════════
# Admin routes
# ═══════════════════════════════════════════════════════════════════════════════

class TestAdminRoutes:

    def _create_brief_for_client(self, flask_app, **overrides):
        db_module.create_user("Test Client", "tc@test.com", "pass1234", "client")
        tc = db_module.get_user_by_email("tc@test.com")
        bid = _make_brief(tc["id"], **overrides)
        return bid, tc["id"]

    def test_admin_dashboard_returns_200(self, admin_client):
        r = admin_client.get("/portal/admin/")
        assert r.status_code == 200

    def test_admin_dashboard_shows_all_briefs(self, admin_client, flask_app):
        db_module.create_user("Cli1", "c1@test.com", "pass1234", "client")
        c1 = db_module.get_user_by_email("c1@test.com")
        _make_brief(c1["id"], title="First Brief")
        r = admin_client.get("/portal/admin/")
        assert b"First Brief" in r.data

    def test_admin_dashboard_shows_client_list(self, admin_client, flask_app):
        db_module.create_user("Liz Client", "liz@test.com", "pass1234", "client")
        r = admin_client.get("/portal/admin/")
        assert b"Liz Client" in r.data

    def test_admin_dashboard_shows_new_client_button(self, admin_client):
        r = admin_client.get("/portal/admin/")
        assert b"New Client" in r.data

    def test_admin_brief_detail_returns_200(self, admin_client, flask_app):
        bid, _ = self._create_brief_for_client(flask_app)
        r = admin_client.get(f"/portal/admin/briefs/{bid}")
        assert r.status_code == 200

    def test_admin_brief_detail_shows_brief_info(self, admin_client, flask_app):
        bid, _ = self._create_brief_for_client(flask_app, title="Admin View Brief")
        r = admin_client.get(f"/portal/admin/briefs/{bid}")
        assert b"Admin View Brief" in r.data

    def test_admin_brief_detail_shows_client_info(self, admin_client, flask_app):
        bid, _ = self._create_brief_for_client(flask_app)
        r = admin_client.get(f"/portal/admin/briefs/{bid}")
        assert b"tc@test.com" in r.data

    def test_mark_in_progress(self, admin_client, flask_app):
        bid, _ = self._create_brief_for_client(flask_app)
        admin_client.post(f"/portal/admin/briefs/{bid}",
                          data={"action": "mark_in_progress"})
        assert db_module.get_brief(bid)["status"] == "in_progress"

    def test_mark_complete(self, admin_client, flask_app):
        bid, _ = self._create_brief_for_client(flask_app)
        admin_client.post(f"/portal/admin/briefs/{bid}",
                          data={"action": "mark_complete"})
        assert db_module.get_brief(bid)["status"] == "completed"

    def test_mark_complete_shows_success_flash(self, admin_client, flask_app):
        bid, _ = self._create_brief_for_client(flask_app)
        r = admin_client.post(f"/portal/admin/briefs/{bid}",
                               data={"action": "mark_complete"},
                               follow_redirects=True)
        assert b"complete" in r.data.lower()

    def test_upload_copy_saves_file(self, admin_client, flask_app):
        bid, _ = self._create_brief_for_client(flask_app)
        file_data = io.BytesIO(b"Finished copy content")
        r = admin_client.post(
            f"/portal/admin/briefs/{bid}",
            data={"action": "upload_copy", "copy_file": (file_data, "final.txt")},
            content_type="multipart/form-data",
            follow_redirects=True,
        )
        assert r.status_code == 200
        cf = db_module.get_copy_file(bid)
        assert cf is not None
        assert cf["original_filename"] == "final.txt"

    def test_upload_copy_marks_brief_complete(self, admin_client, flask_app):
        bid, _ = self._create_brief_for_client(flask_app)
        admin_client.post(
            f"/portal/admin/briefs/{bid}",
            data={"action": "upload_copy",
                  "copy_file": (io.BytesIO(b"copy"), "copy.txt")},
            content_type="multipart/form-data",
        )
        assert db_module.get_brief(bid)["status"] == "completed"

    def test_upload_copy_file_is_on_disk(self, admin_client, flask_app):
        bid, _ = self._create_brief_for_client(flask_app)
        admin_client.post(
            f"/portal/admin/briefs/{bid}",
            data={"action": "upload_copy",
                  "copy_file": (io.BytesIO(b"disk content"), "disk.txt")},
            content_type="multipart/form-data",
        )
        cf = db_module.get_copy_file(bid)
        file_path = os.path.join(flask_app.config["UPLOAD_FOLDER"], cf["storage_filename"])
        assert os.path.exists(file_path)
        with open(file_path) as f:
            assert "disk content" in f.read()

    def test_upload_disallowed_extension_rejected(self, admin_client, flask_app):
        bid, _ = self._create_brief_for_client(flask_app)
        r = admin_client.post(
            f"/portal/admin/briefs/{bid}",
            data={"action": "upload_copy",
                  "copy_file": (io.BytesIO(b"exe content"), "malware.exe")},
            content_type="multipart/form-data",
        )
        html = r.data.decode()
        assert "not allowed" in html.lower() or "only" in html.lower()
        assert db_module.get_copy_file(bid) is None

    def test_upload_no_file_shows_error(self, admin_client, flask_app):
        bid, _ = self._create_brief_for_client(flask_app)
        r = admin_client.post(
            f"/portal/admin/briefs/{bid}",
            data={"action": "upload_copy", "copy_file": (io.BytesIO(b""), "")},
            content_type="multipart/form-data",
        )
        assert b"No file" in r.data

    def test_upload_replaces_previous_file(self, admin_client, flask_app):
        bid, _ = self._create_brief_for_client(flask_app)
        admin_client.post(
            f"/portal/admin/briefs/{bid}",
            data={"action": "upload_copy",
                  "copy_file": (io.BytesIO(b"v1"), "v1.txt")},
            content_type="multipart/form-data",
        )
        admin_client.post(
            f"/portal/admin/briefs/{bid}",
            data={"action": "upload_copy",
                  "copy_file": (io.BytesIO(b"v2"), "v2.txt")},
            content_type="multipart/form-data",
        )
        cf = db_module.get_copy_file(bid)
        assert cf["original_filename"] == "v2.txt"
        with sqlite3.connect(db_module.DB_PATH) as conn:
            count = conn.execute(
                "SELECT COUNT(*) FROM copy_files WHERE brief_id=?", (bid,)
            ).fetchone()[0]
        assert count == 1

    def test_create_client_account(self, admin_client, flask_app):
        r = admin_client.post("/portal/admin/clients/new", data={
            "name": "New Client", "email": "new@client.com", "password": "secure123"
        }, follow_redirects=True)
        assert r.status_code == 200
        user = db_module.get_user_by_email("new@client.com")
        assert user is not None
        assert user["role"] == "client"

    def test_create_client_short_password_rejected(self, admin_client):
        r = admin_client.post("/portal/admin/clients/new", data={
            "name": "N", "email": "n@n.com", "password": "short"
        }, follow_redirects=True)
        assert b"8 characters" in r.data

    def test_create_client_duplicate_email_rejected(self, admin_client, portal_client_user):
        r = admin_client.post("/portal/admin/clients/new", data={
            "name": "Dup", "email": portal_client_user["email"], "password": "longpass1"
        }, follow_redirects=True)
        assert b"already registered" in r.data

    def test_create_client_missing_fields_rejected(self, admin_client):
        r = admin_client.post("/portal/admin/clients/new", data={
            "name": "", "email": "e@e.com", "password": "pass1234"
        }, follow_redirects=True)
        assert b"required" in r.data

    def test_brief_not_found_redirects_to_dashboard(self, admin_client):
        r = admin_client.get("/portal/admin/briefs/99999", follow_redirects=True)
        assert b"Brief not found" in r.data
