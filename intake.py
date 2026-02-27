"""Client Intake Copy Generator — Flask Blueprint (admin only)."""

import anthropic
from flask import Blueprint, render_template, request, current_app, session, redirect, url_for

from db import save_submission

intake_bp = Blueprint("intake", __name__)


@intake_bp.before_request
def _require_admin():
    if "user_id" not in session:
        return redirect(url_for("portal_auth.login", next=request.path))
    if session.get("user_role") != "admin":
        return redirect(url_for("portal_auth.login"))

TONES = ["professional", "casual", "bold", "friendly"]
COPY_TYPES = ["email", "Instagram caption", "Facebook ad", "landing page headline"]

_DELIM = "---VARIATION---"

SYSTEM_PROMPT = (
    "You are an expert DTC copywriter. Given product details, write exactly 3 distinct "
    "variations of the requested copy type.\n\n"
    "Rules:\n"
    "- Write exactly 3 variations\n"
    f'- Separate each variation with exactly "{_DELIM}" on its own line\n'
    "- Do not label or number the variations\n"
    "- Match the requested tone precisely\n"
    "- Each variation must take a meaningfully different angle or hook\n"
    "- Output ONLY the 3 variations separated by the delimiter. "
    "No preamble, no explanation, no quotes around the variations."
)


def generate_variations(form_data: dict):
    client = anthropic.Anthropic(api_key=current_app.config["ANTHROPIC_API_KEY"])
    user_message = (
        f"Product name: {form_data['product_name']}\n"
        f"Product description: {form_data['product_description']}\n"
        f"Target audience: {form_data['target_audience']}\n"
        f"Main benefit: {form_data['main_benefit']}\n"
        f"Biggest objection: {form_data['biggest_objection']}\n"
        f"Tone of voice: {form_data['tone']}\n"
        f"Type of copy needed: {form_data['copy_type']}"
    )
    message = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1024,
        system=SYSTEM_PROMPT,
        messages=[{"role": "user", "content": user_message}],
    )
    if not message.content:
        raise RuntimeError("Claude returned an empty response.")
    raw = message.content[0].text.strip()
    parts = [p.strip() for p in raw.split(_DELIM) if p.strip()]
    if len(parts) < 3:
        raise RuntimeError(f"Expected 3 variations, got {len(parts)}.")
    return parts[:3]


@intake_bp.route("/intake", methods=["GET", "POST"])
def form():
    error = None
    form_data = {}

    if request.method == "POST":
        fields = [
            "product_name", "product_description", "target_audience",
            "main_benefit", "biggest_objection", "tone", "copy_type",
        ]
        form_data = {f: request.form.get(f, "").strip() for f in fields}

        if any(not form_data[f] for f in fields):
            error = "Please fill in all fields before submitting."
        elif form_data["tone"] not in TONES:
            error = "Invalid tone selection."
        elif form_data["copy_type"] not in COPY_TYPES:
            error = "Invalid copy type selection."
        elif not current_app.config["ANTHROPIC_API_KEY"]:
            error = (
                "ANTHROPIC_API_KEY is not set.\n"
                "  export ANTHROPIC_API_KEY='your_key_here'"
            )
        else:
            try:
                variations = generate_variations(form_data)
                form_data["variation_1"] = variations[0]
                form_data["variation_2"] = variations[1]
                form_data["variation_3"] = variations[2]
                save_submission(form_data)
                return render_template(
                    "intake/results.html",
                    variations=variations,
                    form_data=form_data,
                )
            except anthropic.AuthenticationError:
                error = "Invalid API key. Check your ANTHROPIC_API_KEY."
            except anthropic.APIConnectionError:
                error = "Could not reach the Anthropic API. Check your network."
            except Exception as exc:
                error = f"Unexpected error: {exc}"

    return render_template(
        "intake/form.html",
        tones=TONES,
        copy_types=COPY_TYPES,
        error=error,
        form_data=form_data,
    )
