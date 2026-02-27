"""
Proposal Generator test suite.

Covers:
  - _parse_json: raw JSON, markdown-fenced JSON, JSON in surrounding text, failure
  - _build_user_message: field inclusion, optional pain_3
  - generate_proposal_data: Anthropic call pattern, JSON returned
  - /proposal/ form route: GET, POST validation errors, error types
  - /proposal/ result rendering: all sections present and correct
No real API or network calls are made.
"""

import json
import os
import sys
import urllib.error
from io import BytesIO
from unittest.mock import MagicMock, patch

import pytest

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, PROJECT_ROOT)

import db as db_module
import app as app_module
import proposal as proposal_module
from proposal import _parse_json, _build_user_message, generate_proposal_data


# ── shared fixtures ───────────────────────────────────────────────────────────

@pytest.fixture
def flask_app(tmp_path, monkeypatch):
    monkeypatch.setattr(db_module, "DB_PATH", str(tmp_path / "test.db"))
    _app = app_module.create_app()
    _app.config.update(TESTING=True, ANTHROPIC_API_KEY="sk-test")
    return _app


@pytest.fixture
def client(flask_app):
    with flask_app.test_client() as c:
        yield c


_VALID_FORM = {
    "your_name": "Jane Smith Copy",
    "brand_name": "GlowSerum Co.",
    "niche": "DTC skincare",
    "service": "5-email welcome sequence",
    "price": "$1,500",
    "pain_1": "No value prop above the fold",
    "pain_2": "Cart email ignores objections",
    "pain_3": "",
}

_VALID_PROPOSAL = {
    "overview": "GlowSerum has a strong product with weak copy.",
    "pain_points": [
        {"headline": "No value prop visible", "detail": "Visitors leave before understanding the product."},
        {"headline": "Cart email skips objections", "detail": "The email shows the product but never addresses price concerns."},
    ],
    "deliverables_intro": "Here is what this engagement includes.",
    "deliverables": ["5-email welcome sequence", "Abandoned cart email rewrite", "Subject line guide"],
    "investment_note": "One strong sequence pays for itself in a single campaign.",
    "next_steps": [
        {"action": "Review this proposal", "detail": "Read through and note questions."},
        {"action": "Book a 20-min call", "detail": "We align on scope."},
        {"action": "Sign off and kick off", "detail": "Work starts within 48 hours."},
    ],
}


# ═══════════════════════════════════════════════════════════════════════════════
# _parse_json
# ═══════════════════════════════════════════════════════════════════════════════

class TestParseJson:

    def test_parses_raw_json(self):
        data = {"key": "value", "num": 42}
        assert _parse_json(json.dumps(data)) == data

    def test_parses_markdown_fenced_json(self):
        data = {"a": 1}
        text = f"```json\n{json.dumps(data)}\n```"
        assert _parse_json(text) == data

    def test_parses_markdown_fenced_no_lang(self):
        data = {"a": 1}
        text = f"```\n{json.dumps(data)}\n```"
        assert _parse_json(text) == data

    def test_parses_json_with_surrounding_prose(self):
        data = {"overview": "Great copy"}
        text = f"Here is your JSON:\n{json.dumps(data)}\nLet me know!"
        assert _parse_json(text) == data

    def test_parses_nested_json(self):
        data = _VALID_PROPOSAL.copy()
        assert _parse_json(json.dumps(data)) == data

    def test_raises_on_unparseable_text(self):
        with pytest.raises(ValueError, match="Could not extract JSON"):
            _parse_json("This is just a sentence with no JSON at all.")

    def test_raises_on_empty_string(self):
        with pytest.raises((ValueError, json.JSONDecodeError)):
            _parse_json("")

    def test_raises_on_broken_fenced_json(self):
        with pytest.raises(ValueError):
            _parse_json("```json\n{bad json\n```")


# ═══════════════════════════════════════════════════════════════════════════════
# _build_user_message
# ═══════════════════════════════════════════════════════════════════════════════

class TestBuildUserMessage:

    def test_contains_all_required_fields(self):
        msg = _build_user_message(_VALID_FORM)
        assert "Jane Smith Copy" in msg
        assert "GlowSerum Co." in msg
        assert "DTC skincare" in msg
        assert "5-email welcome sequence" in msg
        assert "$1,500" in msg
        assert "No value prop above the fold" in msg
        assert "Cart email ignores objections" in msg

    def test_excludes_empty_pain_3(self):
        msg = _build_user_message({**_VALID_FORM, "pain_3": ""})
        lines = msg.strip().splitlines()
        pain_lines = [l for l in lines if l.startswith("- ")]
        assert len(pain_lines) == 2

    def test_includes_pain_3_when_provided(self):
        form = {**_VALID_FORM, "pain_3": "Instagram captions lead with features"}
        msg = _build_user_message(form)
        assert "Instagram captions lead with features" in msg
        pain_lines = [l for l in msg.splitlines() if l.startswith("- ")]
        assert len(pain_lines) == 3

    def test_pain_points_formatted_as_bullets(self):
        msg = _build_user_message(_VALID_FORM)
        assert "- No value prop above the fold" in msg
        assert "- Cart email ignores objections" in msg

    def test_fields_labelled(self):
        msg = _build_user_message(_VALID_FORM)
        assert "brand" in msg.lower() or "client" in msg.lower()
        assert "niche" in msg.lower()


# ═══════════════════════════════════════════════════════════════════════════════
# generate_proposal_data
# ═══════════════════════════════════════════════════════════════════════════════

class TestGenerateProposalData:

    def _mock_anthropic(self, payload):
        msg = MagicMock()
        msg.content = [MagicMock(text=json.dumps(payload))]
        client = MagicMock()
        client.messages.create.return_value = msg
        return client

    def test_returns_parsed_dict(self, flask_app):
        with flask_app.app_context():
            with patch("anthropic.Anthropic", return_value=self._mock_anthropic(_VALID_PROPOSAL)):
                result = generate_proposal_data(_VALID_FORM)
        assert result["overview"] == _VALID_PROPOSAL["overview"]
        assert len(result["pain_points"]) == 2
        assert len(result["next_steps"]) == 3

    def test_passes_api_key(self, flask_app):
        with flask_app.app_context():
            with patch("anthropic.Anthropic") as mock_cls:
                mock_cls.return_value = self._mock_anthropic(_VALID_PROPOSAL)
                generate_proposal_data(_VALID_FORM)
        mock_cls.assert_called_once_with(api_key="sk-test")

    def test_uses_correct_model(self, flask_app):
        with flask_app.app_context():
            client = self._mock_anthropic(_VALID_PROPOSAL)
            with patch("anthropic.Anthropic", return_value=client):
                generate_proposal_data(_VALID_FORM)
        _, kwargs = client.messages.create.call_args
        assert kwargs["model"] == "claude-sonnet-4-6"

    def test_user_message_sent(self, flask_app):
        with flask_app.app_context():
            client = self._mock_anthropic(_VALID_PROPOSAL)
            with patch("anthropic.Anthropic", return_value=client):
                generate_proposal_data(_VALID_FORM)
        _, kwargs = client.messages.create.call_args
        user_content = kwargs["messages"][0]["content"]
        assert "GlowSerum Co." in user_content

    def test_raises_on_empty_content(self, flask_app):
        msg = MagicMock()
        msg.content = []
        client = MagicMock()
        client.messages.create.return_value = msg
        with flask_app.app_context():
            with patch("anthropic.Anthropic", return_value=client):
                with pytest.raises(RuntimeError, match="empty response"):
                    generate_proposal_data(_VALID_FORM)

    def test_handles_markdown_fenced_response(self, flask_app):
        fenced = f"```json\n{json.dumps(_VALID_PROPOSAL)}\n```"
        msg = MagicMock()
        msg.content = [MagicMock(text=fenced)]
        client = MagicMock()
        client.messages.create.return_value = msg
        with flask_app.app_context():
            with patch("anthropic.Anthropic", return_value=client):
                result = generate_proposal_data(_VALID_FORM)
        assert result["overview"] == _VALID_PROPOSAL["overview"]


# ═══════════════════════════════════════════════════════════════════════════════
# /proposal/ form route — GET
# ═══════════════════════════════════════════════════════════════════════════════

class TestFormGet:

    def test_returns_200(self, client):
        r = client.get("/proposal/")
        assert r.status_code == 200

    def test_renders_all_input_fields(self, client):
        html = client.get("/proposal/").data.decode()
        for name in ("your_name", "brand_name", "niche", "service", "price",
                     "pain_1", "pain_2", "pain_3"):
            assert f'name="{name}"' in html

    def test_no_error_on_fresh_load(self, client):
        html = client.get("/proposal/").data.decode()
        assert "error" not in html.lower() or "class=\"error\"" not in html

    def test_nav_links_present(self, client):
        html = client.get("/proposal/").data.decode()
        assert "/intake/" in html
        assert "/" in html

    def test_pain_3_marked_optional(self, client):
        html = client.get("/proposal/").data.decode()
        assert "optional" in html.lower()


# ═══════════════════════════════════════════════════════════════════════════════
# /proposal/ form route — POST validation
# ═══════════════════════════════════════════════════════════════════════════════

class TestFormPostValidation:

    def _post(self, c, overrides=None):
        data = {**_VALID_FORM, **(overrides or {})}
        return c.post("/proposal/", data=data)

    def test_missing_your_name_shows_error(self, client):
        r = self._post(client, {"your_name": ""})
        assert b"required" in r.data.lower()

    def test_missing_brand_name_shows_error(self, client):
        r = self._post(client, {"brand_name": ""})
        assert b"required" in r.data.lower()

    def test_missing_niche_shows_error(self, client):
        r = self._post(client, {"niche": ""})
        assert b"required" in r.data.lower()

    def test_missing_service_shows_error(self, client):
        r = self._post(client, {"service": ""})
        assert b"required" in r.data.lower()

    def test_missing_price_shows_error(self, client):
        r = self._post(client, {"price": ""})
        assert b"required" in r.data.lower()

    def test_missing_pain_1_shows_error(self, client):
        r = self._post(client, {"pain_1": ""})
        assert b"required" in r.data.lower()

    def test_missing_pain_2_shows_error(self, client):
        r = self._post(client, {"pain_2": ""})
        assert b"required" in r.data.lower()

    def test_pain_3_is_optional(self, flask_app):
        """Omitting pain_3 should not trigger a validation error."""
        with flask_app.test_client() as c:
            with patch("proposal.generate_proposal_data", return_value=_VALID_PROPOSAL):
                r = c.post("/proposal/", data={**_VALID_FORM, "pain_3": ""},
                           follow_redirects=True)
        assert b"required" not in r.data.lower()

    def test_form_repopulates_on_error(self, client):
        r = self._post(client, {"brand_name": ""})
        html = r.data.decode()
        assert "Jane Smith Copy" in html   # your_name preserved

    def test_no_api_key_shows_error(self, flask_app):
        flask_app.config["ANTHROPIC_API_KEY"] = ""
        with flask_app.test_client() as c:
            r = c.post("/proposal/", data=_VALID_FORM)
        assert b"ANTHROPIC_API_KEY" in r.data

    def test_auth_error_shows_friendly_message(self, flask_app):
        import anthropic as anthropic_mod
        with flask_app.test_client() as c:
            with patch("proposal.generate_proposal_data",
                       side_effect=anthropic_mod.AuthenticationError(
                           message="bad key", response=MagicMock(), body={})):
                r = c.post("/proposal/", data=_VALID_FORM)
        assert b"Invalid API key" in r.data

    def test_connection_error_shows_friendly_message(self, flask_app):
        import anthropic as anthropic_mod
        with flask_app.test_client() as c:
            with patch("proposal.generate_proposal_data",
                       side_effect=anthropic_mod.APIConnectionError(request=MagicMock())):
                r = c.post("/proposal/", data=_VALID_FORM)
        assert b"Anthropic API" in r.data

    def test_json_parse_error_shows_friendly_message(self, flask_app):
        with flask_app.test_client() as c:
            with patch("proposal.generate_proposal_data",
                       side_effect=ValueError("bad json")):
                r = c.post("/proposal/", data=_VALID_FORM)
        assert b"parse error" in r.data.lower() or b"JSON" in r.data


# ═══════════════════════════════════════════════════════════════════════════════
# /proposal/ result page
# ═══════════════════════════════════════════════════════════════════════════════

class TestResultPage:

    @pytest.fixture
    def result_html(self, flask_app):
        with flask_app.test_client() as c:
            with patch("proposal.generate_proposal_data", return_value=_VALID_PROPOSAL):
                r = c.post("/proposal/", data=_VALID_FORM)
        return r.data.decode()

    # ── HTTP / content type ───────────────────────────────────────────────────

    def test_returns_200(self, flask_app):
        with flask_app.test_client() as c:
            with patch("proposal.generate_proposal_data", return_value=_VALID_PROPOSAL):
                r = c.post("/proposal/", data=_VALID_FORM)
        assert r.status_code == 200

    # ── header section ────────────────────────────────────────────────────────

    def test_shows_business_name(self, result_html):
        assert "Jane Smith Copy" in result_html

    def test_shows_brand_name(self, result_html):
        assert "GlowSerum Co." in result_html

    def test_shows_date(self, result_html):
        # Date is dynamic but should contain year
        assert "2026" in result_html or "202" in result_html

    def test_shows_proposal_badge(self, result_html):
        assert "Proposal" in result_html

    def test_shows_niche(self, result_html):
        assert "DTC skincare" in result_html

    # ── overview section ──────────────────────────────────────────────────────

    def test_shows_section_01(self, result_html):
        assert "01" in result_html
        assert "Overview" in result_html

    def test_shows_overview_text(self, result_html):
        assert "GlowSerum has a strong product with weak copy." in result_html

    # ── pain points section ───────────────────────────────────────────────────

    def test_shows_section_02(self, result_html):
        assert "02" in result_html

    def test_shows_pain_point_headlines(self, result_html):
        assert "No value prop visible" in result_html
        assert "Cart email skips objections" in result_html

    def test_shows_pain_point_details(self, result_html):
        assert "Visitors leave before understanding the product." in result_html

    def test_shows_all_pain_points(self, result_html):
        assert result_html.count("pain-point") >= 2

    # ── deliverables section ──────────────────────────────────────────────────

    def test_shows_section_03(self, result_html):
        assert "03" in result_html
        assert "What You Get" in result_html

    def test_shows_deliverables_intro(self, result_html):
        assert "Here is what this engagement includes." in result_html

    def test_shows_all_deliverables(self, result_html):
        assert "5-email welcome sequence" in result_html
        assert "Abandoned cart email rewrite" in result_html
        assert "Subject line guide" in result_html

    def test_deliverables_use_checkmark(self, result_html):
        assert "✓" in result_html

    # ── investment section ────────────────────────────────────────────────────

    def test_shows_section_04(self, result_html):
        assert "04" in result_html
        assert "Investment" in result_html

    def test_shows_price(self, result_html):
        assert "$1,500" in result_html

    def test_shows_investment_note(self, result_html):
        assert "One strong sequence pays for itself" in result_html

    # ── next steps section ────────────────────────────────────────────────────

    def test_shows_section_05(self, result_html):
        assert "05" in result_html
        assert "Next Steps" in result_html

    def test_shows_all_step_actions(self, result_html):
        assert "Review this proposal" in result_html
        assert "Book a 20-min call" in result_html
        assert "Sign off and kick off" in result_html

    def test_shows_step_details(self, result_html):
        assert "Read through and note questions." in result_html

    def test_shows_three_step_numbers(self, result_html):
        assert "01" in result_html
        assert "02" in result_html
        assert "03" in result_html

    # ── footer ────────────────────────────────────────────────────────────────

    def test_footer_shows_business_name(self, result_html):
        assert result_html.count("Jane Smith Copy") >= 2  # header + footer

    # ── print / screen controls ───────────────────────────────────────────────

    def test_has_print_button(self, result_html):
        assert "window.print()" in result_html

    def test_has_back_link(self, result_html):
        assert "/proposal/" in result_html
        assert "New Proposal" in result_html

    def test_has_print_media_query(self, result_html):
        assert "@media print" in result_html

    def test_toolbar_hidden_on_print(self, result_html):
        assert "toolbar" in result_html
        # toolbar has display:none in @media print block
        assert "display: none" in result_html or "display:none" in result_html

    # ── with three pain points ────────────────────────────────────────────────

    def test_three_pain_points_rendered(self, flask_app):
        proposal_3pp = {
            **_VALID_PROPOSAL,
            "pain_points": [
                {"headline": "PP one headline", "detail": "Detail one."},
                {"headline": "PP two headline", "detail": "Detail two."},
                {"headline": "PP three headline", "detail": "Detail three."},
            ],
        }
        form_3pp = {**_VALID_FORM, "pain_3": "Instagram captions lead with features"}
        with flask_app.test_client() as c:
            with patch("proposal.generate_proposal_data", return_value=proposal_3pp):
                r = c.post("/proposal/", data=form_3pp)
        html = r.data.decode()
        assert "PP one headline" in html
        assert "PP two headline" in html
        assert "PP three headline" in html
