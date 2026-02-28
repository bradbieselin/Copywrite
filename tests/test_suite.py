"""
Copywrite — comprehensive test suite.
Covers db.py, dm.py (Blueprint), intake.py (Blueprint), app.py, and
instagram_dtc_scraper.py helpers — without hitting any real external API.
"""

import os
import sys
import sqlite3
import tempfile
import importlib

import pytest
from unittest.mock import MagicMock, patch, call

# ── ensure project root is importable ────────────────────────────────────────
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, PROJECT_ROOT)

import db as db_module
import app as app_module
import instagram_dtc_scraper as scraper

# ── shared test fixtures / data ───────────────────────────────────────────────

VALID_FORM = {
    "product_name": "GlowSerum",
    "product_description": "A daily vitamin-C serum for radiant skin.",
    "target_audience": "Women 25–40 with dull skin",
    "main_benefit": "Visible glow in 7 days",
    "biggest_objection": "Price feels high for daily use",
    "tone": "professional",
    "copy_type": "email",
}

THREE_VARIATIONS_RAW = (
    "First email copy.\n"
    "---VARIATION---\n"
    "Second email copy.\n"
    "---VARIATION---\n"
    "Third email copy."
)


def _mock_message(text: str):
    """Build a minimal mock that looks like an anthropic Message."""
    block = MagicMock()
    block.text = text
    msg = MagicMock()
    msg.content = [block]
    return msg


# ═══════════════════════════════════════════════════════════════════════════════
# db.py
# ═══════════════════════════════════════════════════════════════════════════════

class TestDb:
    """Tests for db.init_db() and db.save_submission()."""

    def setup_method(self):
        self._tmp = tempfile.mkdtemp()
        self._db_path = os.path.join(self._tmp, "test.db")
        self._orig_path = db_module.DB_PATH
        db_module.DB_PATH = self._db_path
        db_module.init_db()

    def teardown_method(self):
        db_module.DB_PATH = self._orig_path

    def _data(self, **overrides):
        d = dict(VALID_FORM, variation_1="V1", variation_2="V2", variation_3="V3")
        d.update(overrides)
        return d

    # ── init_db ──────────────────────────────────────────────────────────────

    def test_init_creates_submissions_table(self):
        with sqlite3.connect(self._db_path) as conn:
            row = conn.execute(
                "SELECT name FROM sqlite_master WHERE type='table' AND name='submissions'"
            ).fetchone()
        assert row is not None

    def test_init_is_idempotent(self):
        """Calling init_db() twice must not raise."""
        db_module.init_db()
        db_module.init_db()

    def test_table_has_expected_columns(self):
        with sqlite3.connect(self._db_path) as conn:
            cols = {row[1] for row in conn.execute("PRAGMA table_info(submissions)")}
        expected = {
            "id", "created_at", "product_name", "product_description",
            "target_audience", "main_benefit", "biggest_objection",
            "tone", "copy_type", "variation_1", "variation_2", "variation_3",
        }
        assert expected <= cols

    # ── save_submission ───────────────────────────────────────────────────────

    def test_save_submission_returns_integer_id(self):
        row_id = db_module.save_submission(self._data())
        assert isinstance(row_id, int) and row_id >= 1

    def test_save_submission_ids_increment(self):
        id1 = db_module.save_submission(self._data())
        id2 = db_module.save_submission(self._data())
        assert id2 == id1 + 1

    def test_save_submission_round_trip(self):
        data = self._data(variation_1="Alpha", variation_2="Beta", variation_3="Gamma")
        db_module.save_submission(data)
        with sqlite3.connect(self._db_path) as conn:
            row = conn.execute(
                "SELECT product_name, tone, copy_type, variation_1, variation_2, variation_3 "
                "FROM submissions WHERE id=1"
            ).fetchone()
        assert row is not None
        assert row[0] == "GlowSerum"
        assert row[1] == "professional"
        assert row[2] == "email"
        assert row[3] == "Alpha"
        assert row[4] == "Beta"
        assert row[5] == "Gamma"

    def test_save_submission_created_at_populated(self):
        db_module.save_submission(self._data())
        with sqlite3.connect(self._db_path) as conn:
            created_at = conn.execute(
                "SELECT created_at FROM submissions WHERE id=1"
            ).fetchone()[0]
        assert created_at is not None and created_at != ""


# ═══════════════════════════════════════════════════════════════════════════════
# Flask app — shared fixture
# ═══════════════════════════════════════════════════════════════════════════════

@pytest.fixture
def flask_test_client(tmp_path, monkeypatch):
    """
    Returns a Flask test client with:
      - TESTING=True
      - WTF_CSRF_ENABLED=False (so tests can POST without CSRF tokens)
      - a fresh temp SQLite DB (avoids polluting copywrite.db)
      - ANTHROPIC_API_KEY='fake-key' (real calls are mocked per-test)
      - Logged in as admin (required by dm, intake, and proposal blueprints)
    """
    db_path = str(tmp_path / "test.db")
    monkeypatch.setattr(db_module, "DB_PATH", db_path)

    _app = app_module.create_app()
    _app.config["TESTING"] = True
    _app.config["WTF_CSRF_ENABLED"] = False
    _app.config["ANTHROPIC_API_KEY"] = "fake-key"

    with _app.test_client() as client:
        # Log in as admin so blueprint before_request checks pass
        with client.session_transaction() as sess:
            sess["user_id"] = 1
            sess["user_name"] = "Admin"
            sess["user_role"] = "admin"
            sess["user_email"] = "admin@copydtc.com"
        yield client


# ═══════════════════════════════════════════════════════════════════════════════
# app.py — factory / wiring
# ═══════════════════════════════════════════════════════════════════════════════

class TestAppFactory:
    def test_blueprints_registered(self):
        rules = {str(r) for r in app_module.app.url_map.iter_rules()}
        assert "/" in rules
        assert "/tools/intake" in rules

    def test_api_key_loaded_from_env(self, monkeypatch):
        monkeypatch.setenv("ANTHROPIC_API_KEY", "sentinel-value")
        _app = app_module.create_app()
        assert _app.config["ANTHROPIC_API_KEY"] == "sentinel-value"

    def test_missing_env_key_defaults_to_empty(self, monkeypatch):
        monkeypatch.delenv("ANTHROPIC_API_KEY", raising=False)
        _app = app_module.create_app()
        assert _app.config["ANTHROPIC_API_KEY"] == ""


# ═══════════════════════════════════════════════════════════════════════════════
# dm.py — GET /
# ═══════════════════════════════════════════════════════════════════════════════

class TestDmGet:
    def test_get_returns_200(self, flask_test_client):
        r = flask_test_client.get("/tools/dm")
        assert r.status_code == 200

    def test_get_renders_form_fields(self, flask_test_client):
        r = flask_test_client.get("/tools/dm")
        html = r.data.decode()
        assert "Cold DM Generator" in html
        assert 'name="bio"' in html
        assert 'name="caption"' in html

    def test_get_renders_nav_links(self, flask_test_client):
        r = flask_test_client.get("/tools/dm")
        html = r.data.decode()
        assert "/intake" in html or "/tools/intake" in html

    def test_get_no_dm_section_initially(self, flask_test_client):
        r = flask_test_client.get("/tools/dm")
        html = r.data.decode()
        assert "Your DM" not in html


# ═══════════════════════════════════════════════════════════════════════════════
# dm.py — POST / validation
# ═══════════════════════════════════════════════════════════════════════════════

class TestDmPostValidation:
    def test_empty_bio_and_caption_shows_error(self, flask_test_client):
        r = flask_test_client.post("/tools/dm", data={"bio": "", "caption": ""})
        html = r.data.decode()
        assert r.status_code == 200
        assert "at least" in html.lower()

    def test_whitespace_only_treated_as_empty(self, flask_test_client):
        r = flask_test_client.post("/tools/dm", data={"bio": "   ", "caption": "\t"})
        html = r.data.decode()
        assert "at least" in html.lower()

    def test_missing_api_key_shows_error(self, flask_test_client):
        flask_test_client.application.config["ANTHROPIC_API_KEY"] = ""
        r = flask_test_client.post("/tools/dm", data={"bio": "test bio", "caption": "test"})
        html = r.data.decode()
        assert "ANTHROPIC_API_KEY" in html
        # restore
        flask_test_client.application.config["ANTHROPIC_API_KEY"] = "fake-key"

    def test_bio_only_allowed(self, flask_test_client):
        """Submitting with only a bio (no caption) should not show 'at least' error."""
        with patch("dm.anthropic.Anthropic") as mock_cls:
            mock_cls.return_value.messages.create.return_value = _mock_message("Hey there!")
            r = flask_test_client.post("/tools/dm", data={"bio": "A great brand.", "caption": ""})
        html = r.data.decode()
        assert "at least" not in html.lower()

    def test_caption_only_allowed(self, flask_test_client):
        """Submitting with only a caption (no bio) should not show 'at least' error."""
        with patch("dm.anthropic.Anthropic") as mock_cls:
            mock_cls.return_value.messages.create.return_value = _mock_message("Hey there!")
            r = flask_test_client.post("/tools/dm", data={"bio": "", "caption": "Great caption here."})
        html = r.data.decode()
        assert "at least" not in html.lower()


# ═══════════════════════════════════════════════════════════════════════════════
# dm.py — POST / happy path and error branches
# ═══════════════════════════════════════════════════════════════════════════════

class TestDmPostHappyPath:
    def test_successful_generation_shows_dm(self, flask_test_client):
        with patch("dm.anthropic.Anthropic") as mock_cls:
            mock_cls.return_value.messages.create.return_value = _mock_message(
                "Hey, loved your skincare content!"
            )
            r = flask_test_client.post(
                "/tools/dm", data={"bio": "Clean skincare", "caption": "Our new drop is live."}
            )
        html = r.data.decode()
        assert r.status_code == 200
        assert "Hey, loved your skincare content!" in html

    def test_successful_generation_shows_copy_button(self, flask_test_client):
        with patch("dm.anthropic.Anthropic") as mock_cls:
            mock_cls.return_value.messages.create.return_value = _mock_message("DM text")
            r = flask_test_client.post(
                "/tools/dm", data={"bio": "Bio", "caption": "Caption"}
            )
        assert b"copy-btn" in r.data

    def test_successful_generation_shows_word_count_script(self, flask_test_client):
        with patch("dm.anthropic.Anthropic") as mock_cls:
            mock_cls.return_value.messages.create.return_value = _mock_message("DM text")
            r = flask_test_client.post("/tools/dm", data={"bio": "Bio", "caption": "Cap"})
        assert b"wordCount" in r.data

    def test_form_repopulates_bio_on_success(self, flask_test_client):
        with patch("dm.anthropic.Anthropic") as mock_cls:
            mock_cls.return_value.messages.create.return_value = _mock_message("DM")
            r = flask_test_client.post(
                "/tools/dm", data={"bio": "UniqueB1o", "caption": "Cap"}
            )
        assert b"UniqueB1o" in r.data

    def test_form_repopulates_caption_on_success(self, flask_test_client):
        with patch("dm.anthropic.Anthropic") as mock_cls:
            mock_cls.return_value.messages.create.return_value = _mock_message("DM")
            r = flask_test_client.post(
                "/tools/dm", data={"bio": "Bio", "caption": "Unique_Caption_987"}
            )
        assert b"Unique_Caption_987" in r.data

    def test_form_repopulates_on_validation_error(self, flask_test_client):
        r = flask_test_client.post("/tools/dm", data={"bio": "", "caption": ""})
        assert r.status_code == 200  # stays on same page, no redirect

    def test_anthropic_auth_error_shows_message(self, flask_test_client):
        import anthropic as ant
        with patch("dm.anthropic.Anthropic") as mock_cls:
            mock_cls.return_value.messages.create.side_effect = ant.AuthenticationError(
                message="bad key", response=MagicMock(), body={}
            )
            r = flask_test_client.post("/tools/dm", data={"bio": "Bio", "caption": "Cap"})
        html = r.data.decode()
        assert "Invalid API key" in html

    def test_anthropic_connection_error_shows_message(self, flask_test_client):
        import anthropic as ant
        with patch("dm.anthropic.Anthropic") as mock_cls:
            mock_cls.return_value.messages.create.side_effect = ant.APIConnectionError(
                request=MagicMock()
            )
            r = flask_test_client.post("/tools/dm", data={"bio": "Bio", "caption": "Cap"})
        html = r.data.decode()
        assert "network" in html.lower() or "connect" in html.lower() or "api" in html.lower()

    def test_generic_exception_shows_message(self, flask_test_client):
        with patch("dm.anthropic.Anthropic") as mock_cls:
            mock_cls.return_value.messages.create.side_effect = RuntimeError("boom")
            r = flask_test_client.post("/tools/dm", data={"bio": "Bio", "caption": "Cap"})
        html = r.data.decode()
        assert "Something went wrong" in html

    def test_empty_content_from_claude_shows_error(self, flask_test_client):
        with patch("dm.anthropic.Anthropic") as mock_cls:
            empty_msg = MagicMock()
            empty_msg.content = []
            mock_cls.return_value.messages.create.return_value = empty_msg
            r = flask_test_client.post("/tools/dm", data={"bio": "Bio", "caption": "Cap"})
        html = r.data.decode()
        assert r.status_code == 200
        assert "error" in html.lower() or "wrong" in html.lower()

    def test_claude_called_with_correct_model(self, flask_test_client):
        with patch("dm.anthropic.Anthropic") as mock_cls:
            mock_instance = mock_cls.return_value
            mock_instance.messages.create.return_value = _mock_message("DM")
            flask_test_client.post("/tools/dm", data={"bio": "Bio", "caption": "Cap"})
        call_kwargs = mock_instance.messages.create.call_args
        assert call_kwargs.kwargs.get("model") == "claude-sonnet-4-6"


# ═══════════════════════════════════════════════════════════════════════════════
# intake.py — GET /intake/
# ═══════════════════════════════════════════════════════════════════════════════

class TestIntakeGet:
    def test_get_returns_200(self, flask_test_client):
        r = flask_test_client.get("/tools/intake")
        assert r.status_code == 200

    def test_get_slash_intake_returns_200(self, flask_test_client):
        """GET /tools/intake should return the intake form."""
        r = flask_test_client.get("/tools/intake")
        assert r.status_code == 200

    def test_get_renders_all_form_fields(self, flask_test_client):
        r = flask_test_client.get("/tools/intake")
        html = r.data.decode()
        for field in [
            "product_name", "product_description", "target_audience",
            "main_benefit", "biggest_objection", "tone", "copy_type",
        ]:
            assert field in html, f"Field '{field}' missing from intake form"

    def test_get_renders_tone_options(self, flask_test_client):
        r = flask_test_client.get("/tools/intake")
        html = r.data.decode()
        for tone in ["professional", "casual", "bold", "friendly"]:
            assert tone in html

    def test_get_renders_copy_type_options(self, flask_test_client):
        r = flask_test_client.get("/tools/intake")
        html = r.data.decode()
        for ct in ["email", "Instagram caption", "Facebook ad", "landing page headline"]:
            assert ct in html

    def test_get_renders_nav_links(self, flask_test_client):
        r = flask_test_client.get("/tools/intake")
        html = r.data.decode()
        assert "Cold DM Generator" in html
        assert "Copy Generator" in html

    def test_get_no_error_initially(self, flask_test_client):
        r = flask_test_client.get("/tools/intake")
        html = r.data.decode()
        assert 'class="error"' not in html


# ═══════════════════════════════════════════════════════════════════════════════
# intake.py — POST /intake/ validation
# ═══════════════════════════════════════════════════════════════════════════════

class TestIntakePostValidation:
    def _post(self, client, overrides=None):
        data = dict(VALID_FORM)
        if overrides:
            data.update(overrides)
        return client.post("/tools/intake", data=data)

    def test_missing_product_name_shows_error(self, flask_test_client):
        r = self._post(flask_test_client, {"product_name": ""})
        html = r.data.decode()
        assert r.status_code == 200
        assert "fill in all fields" in html.lower()

    def test_missing_description_shows_error(self, flask_test_client):
        r = self._post(flask_test_client, {"product_description": ""})
        html = r.data.decode()
        assert "fill in all fields" in html.lower()

    def test_missing_target_audience_shows_error(self, flask_test_client):
        r = self._post(flask_test_client, {"target_audience": ""})
        html = r.data.decode()
        assert "fill in all fields" in html.lower()

    def test_missing_main_benefit_shows_error(self, flask_test_client):
        r = self._post(flask_test_client, {"main_benefit": ""})
        html = r.data.decode()
        assert "fill in all fields" in html.lower()

    def test_missing_objection_shows_error(self, flask_test_client):
        r = self._post(flask_test_client, {"biggest_objection": ""})
        html = r.data.decode()
        assert "fill in all fields" in html.lower()

    def test_invalid_tone_rejected(self, flask_test_client):
        r = self._post(flask_test_client, {"tone": "angry"})
        html = r.data.decode()
        assert "Invalid tone" in html

    def test_invalid_copy_type_rejected(self, flask_test_client):
        r = self._post(flask_test_client, {"copy_type": "billboard"})
        html = r.data.decode()
        assert "Invalid copy type" in html

    def test_missing_api_key_shows_error(self, flask_test_client):
        flask_test_client.application.config["ANTHROPIC_API_KEY"] = ""
        r = self._post(flask_test_client)
        html = r.data.decode()
        assert "ANTHROPIC_API_KEY" in html
        # restore
        flask_test_client.application.config["ANTHROPIC_API_KEY"] = "fake-key"

    def test_form_repopulates_on_validation_error(self, flask_test_client):
        r = self._post(flask_test_client, {"product_name": ""})
        html = r.data.decode()
        # product_name input should have an empty value attribute
        assert 'value="GlowSerum"' not in html
        # description textarea should be repopulated (placeholder≠value for textareas)
        assert "A daily vitamin-C serum" in html

    def test_whitespace_only_field_treated_as_empty(self, flask_test_client):
        r = self._post(flask_test_client, {"product_name": "   "})
        html = r.data.decode()
        assert "fill in all fields" in html.lower()


# ═══════════════════════════════════════════════════════════════════════════════
# intake.py — POST /intake/ happy path
# ═══════════════════════════════════════════════════════════════════════════════

class TestIntakePostHappyPath:
    def _post(self, client):
        with patch("intake.anthropic.Anthropic") as mock_cls:
            mock_cls.return_value.messages.create.return_value = _mock_message(
                THREE_VARIATIONS_RAW
            )
            return client.post("/tools/intake", data=VALID_FORM)

    def test_success_returns_200(self, flask_test_client):
        r = self._post(flask_test_client)
        assert r.status_code == 200

    def test_success_renders_three_variations(self, flask_test_client):
        r = self._post(flask_test_client)
        html = r.data.decode()
        assert "First email copy." in html
        assert "Second email copy." in html
        assert "Third email copy." in html

    def test_success_renders_variation_labels(self, flask_test_client):
        r = self._post(flask_test_client)
        html = r.data.decode()
        assert "Variation 1" in html
        assert "Variation 2" in html
        assert "Variation 3" in html

    def test_success_renders_product_name_in_meta(self, flask_test_client):
        r = self._post(flask_test_client)
        assert b"GlowSerum" in r.data

    def test_success_renders_copy_buttons(self, flask_test_client):
        r = self._post(flask_test_client)
        html = r.data.decode()
        # count only HTML attribute occurrences, not CSS class selectors
        assert html.count('class="copy-btn"') == 3

    def test_success_saves_to_db(self, flask_test_client, tmp_path):
        """Verify that a successful generation writes a row to SQLite."""
        db_path = db_module.DB_PATH
        self._post(flask_test_client)
        with sqlite3.connect(db_path) as conn:
            rows = conn.execute("SELECT * FROM submissions").fetchall()
        assert len(rows) == 1
        assert rows[0][2] == "GlowSerum"  # product_name column

    def test_success_renders_generate_new_link(self, flask_test_client):
        r = self._post(flask_test_client)
        assert b"/intake" in r.data

    def test_success_delimiter_stripped_from_output(self, flask_test_client):
        r = self._post(flask_test_client)
        assert b"---VARIATION---" not in r.data

    def test_claude_called_with_correct_model(self, flask_test_client):
        with patch("intake.anthropic.Anthropic") as mock_cls:
            mock_cls.return_value.messages.create.return_value = _mock_message(
                THREE_VARIATIONS_RAW
            )
            flask_test_client.post("/tools/intake", data=VALID_FORM)
        call_kwargs = mock_cls.return_value.messages.create.call_args
        assert call_kwargs.kwargs.get("model") == "claude-sonnet-4-6"

    def test_extra_variations_truncated_to_three(self, flask_test_client):
        four_var = (
            "V1\n---VARIATION---\nV2\n---VARIATION---\nV3\n---VARIATION---\nV4"
        )
        with patch("intake.anthropic.Anthropic") as mock_cls:
            mock_cls.return_value.messages.create.return_value = _mock_message(four_var)
            r = flask_test_client.post("/tools/intake", data=VALID_FORM)
        html = r.data.decode()
        assert "Variation 4" not in html
        assert "Variation 3" in html


# ═══════════════════════════════════════════════════════════════════════════════
# intake.py — POST /intake/ error branches
# ═══════════════════════════════════════════════════════════════════════════════

class TestIntakePostErrors:
    def test_auth_error_shows_message(self, flask_test_client):
        import anthropic as ant
        with patch("intake.anthropic.Anthropic") as mock_cls:
            mock_cls.return_value.messages.create.side_effect = ant.AuthenticationError(
                message="bad key", response=MagicMock(), body={}
            )
            r = flask_test_client.post("/tools/intake", data=VALID_FORM)
        assert b"Invalid API key" in r.data

    def test_connection_error_shows_message(self, flask_test_client):
        import anthropic as ant
        with patch("intake.anthropic.Anthropic") as mock_cls:
            mock_cls.return_value.messages.create.side_effect = ant.APIConnectionError(
                request=MagicMock()
            )
            r = flask_test_client.post("/tools/intake", data=VALID_FORM)
        html = r.data.decode()
        assert "connect" in html.lower() or "network" in html.lower() or "api" in html.lower()

    def test_insufficient_variations_shows_error(self, flask_test_client):
        """Claude returning fewer than 3 separated parts → error shown on form."""
        with patch("intake.anthropic.Anthropic") as mock_cls:
            mock_cls.return_value.messages.create.return_value = _mock_message(
                "Only one variation, no delimiter."
            )
            r = flask_test_client.post("/tools/intake", data=VALID_FORM)
        html = r.data.decode()
        assert r.status_code == 200
        assert "error" in html.lower() or "wrong" in html.lower()

    def test_generic_exception_shows_message(self, flask_test_client):
        with patch("intake.anthropic.Anthropic") as mock_cls:
            mock_cls.return_value.messages.create.side_effect = RuntimeError("kaboom")
            r = flask_test_client.post("/tools/intake", data=VALID_FORM)
        html = r.data.decode()
        assert "Something went wrong" in html

    def test_empty_response_from_claude_shows_error(self, flask_test_client):
        with patch("intake.anthropic.Anthropic") as mock_cls:
            empty = MagicMock()
            empty.content = []
            mock_cls.return_value.messages.create.return_value = empty
            r = flask_test_client.post("/tools/intake", data=VALID_FORM)
        assert r.status_code == 200
        html = r.data.decode()
        assert "error" in html.lower() or "empty" in html.lower()

    def test_error_does_not_save_to_db(self, flask_test_client):
        db_path = db_module.DB_PATH
        with patch("intake.anthropic.Anthropic") as mock_cls:
            mock_cls.return_value.messages.create.side_effect = RuntimeError("fail")
            flask_test_client.post("/tools/intake", data=VALID_FORM)
        with sqlite3.connect(db_path) as conn:
            count = conn.execute("SELECT COUNT(*) FROM submissions").fetchone()[0]
        assert count == 0


# ═══════════════════════════════════════════════════════════════════════════════
# instagram_dtc_scraper.py — pure-function tests (no Apify calls)
# ═══════════════════════════════════════════════════════════════════════════════

class TestScraperHelpers:

    # ── safe_int ─────────────────────────────────────────────────────────────

    def test_safe_int_converts_int(self):
        assert scraper.safe_int(42) == 42

    def test_safe_int_converts_string_int(self):
        assert scraper.safe_int("1234") == 1234

    def test_safe_int_converts_float_string(self):
        # int("3.5") raises ValueError; safe_int should return 0
        assert scraper.safe_int("3.5") == 0

    def test_safe_int_handles_none(self):
        assert scraper.safe_int(None) == 0

    def test_safe_int_handles_empty_string(self):
        assert scraper.safe_int("") == 0

    def test_safe_int_handles_non_numeric_string(self):
        assert scraper.safe_int("abc") == 0

    def test_safe_int_handles_zero(self):
        assert scraper.safe_int(0) == 0

    # ── extract_profile ───────────────────────────────────────────────────────

    def _item(self, **kwargs):
        base = {
            "username": "testbrand",
            "fullName": "Test Brand",
            "followersCount": 10000,
            "biography": "We make great stuff.",
        }
        base.update(kwargs)
        return base

    def test_extract_profile_returns_dict(self):
        result = scraper.extract_profile(self._item(), "dtcbrand")
        assert isinstance(result, dict)

    def test_extract_profile_username_stripped(self):
        result = scraper.extract_profile(self._item(username="@testbrand"), "dtcbrand")
        assert result["username"] == "testbrand"

    def test_extract_profile_follower_count(self):
        result = scraper.extract_profile(self._item(followersCount=50000), "dtcbrand")
        assert result["follower_count"] == 50000

    def test_extract_profile_follower_count_zero_when_none(self):
        result = scraper.extract_profile(self._item(followersCount=None), "dtcbrand")
        assert result["follower_count"] == 0

    def test_extract_profile_full_name(self):
        result = scraper.extract_profile(self._item(fullName="Cool Brand"), "dtcbrand")
        assert result["full_name"] == "Cool Brand"

    def test_extract_profile_profile_url(self):
        result = scraper.extract_profile(self._item(), "dtcbrand")
        assert result["profile_url"] == "https://www.instagram.com/testbrand/"

    def test_extract_profile_biography_newlines_replaced(self):
        result = scraper.extract_profile(self._item(biography="Line one.\nLine two."), "dtcbrand")
        assert "\n" not in result["bio"]
        assert "Line one." in result["bio"]

    def test_extract_profile_hashtag_stored(self):
        result = scraper.extract_profile(self._item(), "shopify")
        assert result["hashtag"] == "shopify"

    def test_extract_profile_returns_none_when_no_username(self):
        item = self._item(username="", ownerUsername="")
        item.pop("username", None)
        item.pop("ownerUsername", None)
        result = scraper.extract_profile(item, "dtcbrand")
        assert result is None

    def test_extract_profile_falls_back_to_ownerUsername(self):
        item = self._item()
        item["username"] = ""
        item["ownerUsername"] = "fallbackbrand"
        result = scraper.extract_profile(item, "dtcbrand")
        assert result["username"] == "fallbackbrand"

    # ── in_follower_range ─────────────────────────────────────────────────────

    def test_in_range_returns_true(self):
        p = {"follower_count": 50_000}
        assert scraper.in_follower_range(p) is True

    def test_at_min_boundary(self):
        p = {"follower_count": scraper.MIN_FOLLOWERS}
        assert scraper.in_follower_range(p) is True

    def test_at_max_boundary(self):
        p = {"follower_count": scraper.MAX_FOLLOWERS}
        assert scraper.in_follower_range(p) is True

    def test_below_min_returns_false(self):
        p = {"follower_count": scraper.MIN_FOLLOWERS - 1}
        assert scraper.in_follower_range(p) is False

    def test_above_max_returns_false(self):
        p = {"follower_count": scraper.MAX_FOLLOWERS + 1}
        assert scraper.in_follower_range(p) is False

    def test_zero_followers_filtered_out(self):
        assert scraper.in_follower_range({"follower_count": 0}) is False

    # ── validate_token ────────────────────────────────────────────────────────

    def test_validate_token_empty_calls_sys_exit(self):
        with pytest.raises(SystemExit):
            scraper.validate_token("")

    def test_validate_token_none_calls_sys_exit(self):
        with pytest.raises(SystemExit):
            scraper.validate_token(None)

    def test_validate_token_valid_does_not_raise(self):
        scraper.validate_token("valid-token-here")  # must not raise

    # ── save_to_csv ───────────────────────────────────────────────────────────

    def test_save_to_csv_creates_file(self, tmp_path):
        filepath = str(tmp_path / "out.csv")
        scraper.save_to_csv([], filepath)
        assert os.path.exists(filepath)

    def test_save_to_csv_writes_header(self, tmp_path):
        filepath = str(tmp_path / "out.csv")
        scraper.save_to_csv([], filepath)
        with open(filepath) as f:
            header = f.readline()
        assert "username" in header
        assert "follower_count" in header

    def test_save_to_csv_writes_rows(self, tmp_path):
        filepath = str(tmp_path / "out.csv")
        profiles = [
            {"username": "brand1", "full_name": "Brand One",
             "follower_count": 10000, "bio": "B1",
             "profile_url": "https://www.instagram.com/brand1/",
             "hashtag": "dtcbrand"},
        ]
        scraper.save_to_csv(profiles, filepath)
        with open(filepath) as f:
            content = f.read()
        assert "brand1" in content
        assert "10000" in content
