"""Cold DM Generator — Flask Blueprint (admin only)."""

import anthropic
from flask import Blueprint, render_template, request, current_app, session, redirect, url_for

dm_bp = Blueprint("dm", __name__)


@dm_bp.before_request
def _require_admin():
    if "user_id" not in session:
        return redirect(url_for("portal_auth.login", next=request.path))
    if session.get("user_role") != "admin":
        return redirect(url_for("portal_auth.login"))

SYSTEM_PROMPT = """\
You are an expert DTC copywriter and outreach specialist.
Given an Instagram brand's bio and a sample caption, write a cold DM that:
1. Compliments ONE specific, concrete thing about their content or brand voice.
2. Identifies ONE specific weakness in their copy (vague CTAs, passive voice, no hook, etc.).
3. Teases that you can fix it — without over-explaining how.
4. Ends with a soft call to action: ask if they're open to a quick chat.

Rules:
- Stay under 150 words. No exceptions.
- Sound human, not salesy. No buzzword soup.
- Be specific — generic compliments are worse than none.
- Do not use bullet points or headers in the DM itself.
- Output ONLY the DM text. No preamble, no quotes around it.\
"""


def generate_dm(bio: str, caption: str) -> str:
    client = anthropic.Anthropic(api_key=current_app.config["ANTHROPIC_API_KEY"])
    user_message = f"Brand bio:\n{bio.strip()}\n\nSample caption:\n{caption.strip()}"
    message = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=300,
        system=SYSTEM_PROMPT,
        messages=[{"role": "user", "content": user_message}],
    )
    if not message.content:
        raise RuntimeError("Claude returned an empty response.")
    return message.content[0].text.strip()


@dm_bp.route("/dm", methods=["GET", "POST"])
def index():
    dm = None
    error = None
    # Allow pre-filling from the lead scraper via GET params
    bio = request.args.get("bio", "")
    caption = request.args.get("caption", "")

    if request.method == "POST":
        bio = request.form.get("bio", "").strip()
        caption = request.form.get("caption", "").strip()

        if not bio and not caption:
            error = "Paste at least a bio or a caption before submitting."
        elif not current_app.config["ANTHROPIC_API_KEY"]:
            error = (
                "ANTHROPIC_API_KEY is not set. "
                "Export it before starting the server:\n"
                "  export ANTHROPIC_API_KEY='your_key_here'"
            )
        else:
            try:
                dm = generate_dm(bio, caption)
            except anthropic.AuthenticationError:
                error = "Invalid API key. Check your ANTHROPIC_API_KEY."
            except anthropic.APIConnectionError:
                error = "Could not reach the Anthropic API. Check your network."
            except Exception as exc:
                error = f"Unexpected error: {exc}"

    return render_template("index.html", dm=dm, error=error, bio=bio, caption=caption)
