"""Proposal Generator — Flask Blueprint."""

import json
import re
from datetime import date

import anthropic
from flask import Blueprint, render_template, request, current_app

proposal_bp = Blueprint("proposal", __name__)

# ── prompts ───────────────────────────────────────────────────────────────────

_SYSTEM = """\
You are a professional copywriting consultant writing a client sales proposal.
Return ONLY a JSON object — no markdown code fences, no explanation, no extra text.

Use exactly this structure:
{
  "overview": "<2-3 sentences. Show you understand this brand's market and the real opportunity in front of them. Build intrigue. Write as if you are the copywriter making the pitch.>",
  "pain_points": [
    {
      "headline": "<5-8 word diagnosis headline that names the problem precisely>",
      "detail": "<1-2 sentences expanding on this issue and its real cost to the brand>"
    }
  ],
  "deliverables_intro": "<1 confident sentence introducing what this engagement delivers>",
  "deliverables": [
    "<specific, concrete deliverable>",
    "<specific, concrete deliverable>"
  ],
  "investment_note": "<1-2 sentences framing the ROI or strategic value — not just the cost>",
  "next_steps": [
    {"action": "<short verb phrase, 3-6 words>", "detail": "<one sentence describing what this step involves>"},
    {"action": "<short verb phrase>", "detail": "<one sentence>"},
    {"action": "<short verb phrase>", "detail": "<one sentence>"}
  ]
}

Rules:
- pain_points array must contain one entry per pain point provided
- deliverables should be specific to the service described (expand into logical sub-deliverables if needed)
- next_steps must have exactly 3 items
- Tone: confident, direct, professional — no filler phrases\
"""


def _build_user_message(data: dict) -> str:
    pain_points = [data["pain_1"], data["pain_2"]]
    if data.get("pain_3"):
        pain_points.append(data["pain_3"])
    pain_lines = "\n".join(f"- {p}" for p in pain_points)
    return (
        f"Copywriter / business name: {data['your_name']}\n"
        f"Client brand: {data['brand_name']}\n"
        f"Brand niche: {data['niche']}\n"
        f"Service being proposed: {data['service']}\n"
        f"Proposed investment: {data['price']}\n"
        f"Observed copy pain points:\n{pain_lines}"
    )


def _parse_json(text: str) -> dict:
    """Return parsed JSON from Claude's response, handling markdown fences."""
    # 1. Raw JSON
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        pass
    # 2. Markdown-fenced ```json … ```
    m = re.search(r"```(?:json)?\s*([\s\S]*?)\s*```", text)
    if m:
        try:
            return json.loads(m.group(1))
        except json.JSONDecodeError:
            pass
    # 3. First { … } block in the text
    m = re.search(r"\{[\s\S]*\}", text)
    if m:
        try:
            return json.loads(m.group(0))
        except json.JSONDecodeError:
            pass
    raise ValueError("Could not extract JSON from Claude's response.")


def generate_proposal_data(form_data: dict) -> dict:
    client = anthropic.Anthropic(api_key=current_app.config["ANTHROPIC_API_KEY"])
    message = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=2048,
        system=_SYSTEM,
        messages=[{"role": "user", "content": _build_user_message(form_data)}],
    )
    if not message.content:
        raise RuntimeError("Claude returned an empty response.")
    return _parse_json(message.content[0].text.strip())


# ── routes ────────────────────────────────────────────────────────────────────

@proposal_bp.route("/", methods=["GET", "POST"])
def form():
    error = None
    form_data = {}

    if request.method == "POST":
        required = ["your_name", "brand_name", "niche", "service", "price",
                    "pain_1", "pain_2"]
        form_data = {f: request.form.get(f, "").strip() for f in required}
        form_data["pain_3"] = request.form.get("pain_3", "").strip()

        if any(not form_data[f] for f in required):
            error = "Please fill in all required fields."
        elif not current_app.config.get("ANTHROPIC_API_KEY"):
            error = "ANTHROPIC_API_KEY is not set. Export your key and restart."
        else:
            try:
                proposal = generate_proposal_data(form_data)
                today = date.today().strftime("%B %d, %Y")
                return render_template(
                    "proposal/result.html",
                    proposal=proposal,
                    form=form_data,
                    today=today,
                )
            except anthropic.AuthenticationError:
                error = "Invalid API key. Check your ANTHROPIC_API_KEY."
            except anthropic.APIConnectionError:
                error = "Could not reach the Anthropic API. Check your network."
            except (json.JSONDecodeError, ValueError) as exc:
                error = f"Proposal generation failed (JSON parse error): {exc}"
            except Exception as exc:
                error = f"Unexpected error: {exc}"

    return render_template("proposal/form.html", error=error, form_data=form_data)
