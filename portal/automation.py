"""
Automation layer — called in a background thread after a brief is saved.

On every new brief submission:
  1. Generate a first-draft via Claude API and persist it to the DB.
  2. Email the admin via SendGrid (gracefully skipped if keys are absent).

Both steps are wrapped in try/except so a failure in one never blocks the other
or surfaces an error to the client.
"""

import json
import logging
import urllib.error
import urllib.request

import anthropic

import db as db_module

logger = logging.getLogger(__name__)

# ── prompts ───────────────────────────────────────────────────────────────────

_SYSTEM = (
    "You are an expert DTC copywriter. "
    "Based on the client brief below, write one polished first-draft piece of copy.\n\n"
    "Rules:\n"
    "- Write exactly ONE draft — no alternatives, no variations\n"
    "- Match the requested tone precisely\n"
    "- Speak directly to the target audience\n"
    "- Lead with the main benefit\n"
    "- Naturally address the biggest objection\n"
    "- Output ONLY the copy. No preamble, no labels, no closing remarks."
)


def _build_user_message(brief: dict) -> str:
    lines = [
        f"Product name: {brief['product_name']}",
        f"Product description: {brief['product_description']}",
        f"Target audience: {brief['target_audience']}",
        f"Main benefit: {brief['main_benefit']}",
        f"Biggest objection: {brief['biggest_objection']}",
        f"Tone of voice: {brief['tone']}",
        f"Type of copy needed: {brief['copy_type']}",
    ]
    if brief.get("notes"):
        lines.append(f"Additional notes: {brief['notes']}")
    return "\n".join(lines)


# ── draft generation ──────────────────────────────────────────────────────────

def generate_draft(brief: dict, api_key: str) -> str:
    """Call Claude and return the draft text."""
    client = anthropic.Anthropic(api_key=api_key)
    message = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1024,
        system=_SYSTEM,
        messages=[{"role": "user", "content": _build_user_message(brief)}],
    )
    if not message.content:
        raise RuntimeError("Claude returned an empty response.")
    return message.content[0].text.strip()


# ── email notification ────────────────────────────────────────────────────────

def _email_html(brief: dict, draft: str, brief_url: str) -> str:
    escaped_draft = draft.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    draft_html = escaped_draft.replace("\n", "<br>")
    return f"""
<div style="font-family:sans-serif;max-width:600px;color:#111">
  <h2 style="margin-bottom:4px">New brief submitted</h2>
  <p style="color:#666;margin-top:0">Copywrite Client Portal</p>
  <hr style="border:none;border-top:1px solid #e5e5e5">
  <table style="width:100%;border-collapse:collapse">
    <tr><td style="padding:6px 0;color:#666;width:140px">Client</td>
        <td style="padding:6px 0"><strong>{brief['client_name']}</strong>
            &lt;{brief['client_email']}&gt;</td></tr>
    <tr><td style="padding:6px 0;color:#666">Brief title</td>
        <td style="padding:6px 0">{brief['title']}</td></tr>
    <tr><td style="padding:6px 0;color:#666">Product</td>
        <td style="padding:6px 0">{brief['product_name']}</td></tr>
    <tr><td style="padding:6px 0;color:#666">Type</td>
        <td style="padding:6px 0">{brief['copy_type'].capitalize()}</td></tr>
    <tr><td style="padding:6px 0;color:#666">Tone</td>
        <td style="padding:6px 0">{brief['tone'].capitalize()}</td></tr>
  </table>
  <hr style="border:none;border-top:1px solid #e5e5e5">
  <h3 style="margin-bottom:8px">First draft (auto-generated)</h3>
  <div style="background:#f5f5f5;padding:16px;border-radius:6px;
              font-size:15px;line-height:1.6">{draft_html}</div>
  <div style="margin-top:24px">
    <a href="{brief_url}"
       style="background:#111;color:#fff;padding:10px 20px;border-radius:6px;
              text-decoration:none;font-size:14px">
      Review in Admin Portal →
    </a>
  </div>
</div>
""".strip()


def send_brief_notification(brief: dict, draft: str, config: dict) -> None:
    """
    Send an admin notification email via the SendGrid v3 REST API.
    Silently skips if SENDGRID_API_KEY or ADMIN_EMAIL is not configured.
    """
    api_key = config.get("SENDGRID_API_KEY", "")
    from_email = config.get("SENDGRID_FROM_EMAIL", "")
    to_email = config.get("ADMIN_EMAIL", "")
    base_url = config.get("APP_BASE_URL", "http://localhost:5000").rstrip("/")

    if not api_key or not to_email or not from_email:
        logger.info(
            "Email notification skipped — SENDGRID_API_KEY / SENDGRID_FROM_EMAIL "
            "/ ADMIN_EMAIL not configured."
        )
        return

    brief_url = f"{base_url}/portal/admin/briefs/{brief['id']}"
    subject = f"New brief: {brief['title']} — {brief['client_name']}"

    payload = json.dumps({
        "personalizations": [{"to": [{"email": to_email}]}],
        "from": {"email": from_email},
        "subject": subject,
        "content": [{"type": "text/html", "value": _email_html(brief, draft, brief_url)}],
    }).encode()

    req = urllib.request.Request(
        "https://api.sendgrid.com/v3/mail/send",
        data=payload,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            status = resp.status
    except urllib.error.HTTPError as exc:
        body = exc.read().decode(errors="replace")
        raise RuntimeError(f"SendGrid HTTP {exc.code}: {body}") from exc

    if status not in (200, 201, 202):
        raise RuntimeError(f"SendGrid returned unexpected status {status}.")
    logger.info("Admin notification sent for brief %s.", brief["id"])


# ── client completion notification ────────────────────────────────────────────

def _completion_email_html(brief: dict, brief_url: str) -> str:
    return f"""
<div style="font-family:sans-serif;max-width:600px;color:#111">
  <h2 style="margin-bottom:4px">Your copy is ready!</h2>
  <p style="color:#666;margin-top:0">Copywrite Client Portal</p>
  <hr style="border:none;border-top:1px solid #e5e5e5">
  <p style="font-size:15px;line-height:1.6">
    Hi {brief['client_name']},<br><br>
    Great news — your copy for <strong>{brief['title']}</strong> has been
    completed and is ready for download in your client portal.
  </p>
  <div style="margin-top:24px">
    <a href="{brief_url}"
       style="background:#111;color:#fff;padding:10px 20px;border-radius:6px;
              text-decoration:none;font-size:14px">
      View &amp; Download Copy →
    </a>
  </div>
  <p style="font-size:13px;color:#999;margin-top:32px">
    If you have any questions, just reply to this email.
  </p>
</div>
""".strip()


def send_completion_notification(brief: dict, config: dict) -> None:
    """
    Email the client when their copy is marked complete.
    Silently skips if SendGrid is not configured.
    """
    api_key    = config.get("SENDGRID_API_KEY", "")
    from_email = config.get("SENDGRID_FROM_EMAIL", "")
    base_url   = config.get("APP_BASE_URL", "http://localhost:5000").rstrip("/")

    client_email = brief.get("client_email", "")
    if not api_key or not from_email or not client_email:
        logger.info(
            "Completion notification skipped — SendGrid not configured or "
            "client email missing for brief %s.", brief.get("id")
        )
        return

    brief_url = f"{base_url}/portal/client/briefs/{brief['id']}"
    subject   = f"Your copy is ready: {brief['title']}"

    payload = json.dumps({
        "personalizations": [{"to": [{"email": client_email}]}],
        "from": {"email": from_email},
        "subject": subject,
        "content": [{"type": "text/html",
                     "value": _completion_email_html(brief, brief_url)}],
    }).encode()

    req = urllib.request.Request(
        "https://api.sendgrid.com/v3/mail/send",
        data=payload,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            status = resp.status
    except urllib.error.HTTPError as exc:
        body = exc.read().decode(errors="replace")
        raise RuntimeError(f"SendGrid HTTP {exc.code}: {body}") from exc

    if status not in (200, 201, 202):
        raise RuntimeError(f"SendGrid returned unexpected status {status}.")
    logger.info("Completion notification sent to %s for brief %s.",
                client_email, brief["id"])


# ── orchestrator ──────────────────────────────────────────────────────────────

def run_brief_automation(brief: dict, config: dict) -> None:
    """
    Full automation pipeline — safe to call from a daemon thread.
    Exits immediately if the Anthropic key is not set (dev / test environments).
    """
    api_key = config.get("ANTHROPIC_API_KEY", "")
    if not api_key:
        return

    # 1. Generate draft
    try:
        draft = generate_draft(brief, api_key)
        db_module.save_draft(brief["id"], draft)
    except Exception:
        logger.exception("Failed to generate/save draft for brief %s.", brief["id"])
        return  # skip email if draft failed

    # 2. Send notification
    try:
        send_brief_notification(brief, draft, config)
    except Exception:
        logger.exception("Failed to send notification for brief %s.", brief["id"])
