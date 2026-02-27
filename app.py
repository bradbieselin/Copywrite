"""
DM Generator — Flask web app
Paste an Instagram brand's bio + a sample caption, get a personalized cold DM.
"""

import os
import anthropic
from flask import Flask, render_template, request

ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY", "")

app = Flask(__name__)

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
    client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)

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


@app.route("/", methods=["GET", "POST"])
def index():
    dm = None
    error = None
    bio = ""
    caption = ""

    if request.method == "POST":
        bio = request.form.get("bio", "").strip()
        caption = request.form.get("caption", "").strip()

        if not bio and not caption:
            error = "Paste at least a bio or a caption before submitting."
        elif not ANTHROPIC_API_KEY:
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


if __name__ == "__main__":
    if not ANTHROPIC_API_KEY:
        print(
            "WARNING: ANTHROPIC_API_KEY is not set.\n"
            "Export your key before running:\n"
            "  export ANTHROPIC_API_KEY='your_key_here'"
        )
    app.run(debug=True, port=5000)
