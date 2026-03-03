"""Marketing landing page — Flask Blueprint."""

import logging
import os
import re
import threading
from flask import Blueprint, render_template, request, redirect, url_for, flash, current_app

import resend
import db as db_module

_EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")

landing_bp = Blueprint("landing", __name__)

_PHOTO_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "static", "images", "headshot1.jpg")


@landing_bp.route("/")
def index():
    sent = request.args.get("sent") == "1"
    return render_template("landing.html", sent=sent)


@landing_bp.route("/about")
def about():
    photo_exists = os.path.isfile(_PHOTO_PATH)
    return render_template("about.html", photo_exists=photo_exists)


@landing_bp.route("/privacy")
def privacy():
    return render_template("privacy.html")


def _send_email_notification(name, email, interest, message):
    """Send contact form notification via Resend HTTP API in a background thread."""
    api_key = os.environ.get("RESEND_API_KEY", "")
    contact_email = os.environ.get("CONTACT_EMAIL", "")

    if not api_key or not contact_email:
        return

    resend.api_key = api_key

    body = "\n".join([
        f"Name: {name}",
        f"Email: {email}",
        f"Interested in: {interest or 'Not specified'}",
        "",
        "Message:",
        message or "No message provided",
    ])

    log = logging.getLogger("landing.email")

    def _send():
        try:
            resend.Emails.send({
                "from": "CopyDTC Contact Form <contact@copydtc.com>",
                "to": [contact_email],
                "reply_to": email,
                "subject": f"New inquiry from {name}",
                "text": body,
            })
            log.info("Email sent via Resend")
        except Exception as exc:
            log.error("Resend email failed: %s", exc)

    threading.Thread(target=_send, daemon=True).start()


@landing_bp.route("/contact", methods=["POST"])
def contact():
    # Honeypot: bots fill the hidden "url" field, humans never see it
    if request.form.get("url", "").strip():
        # Silent success — don't tip off the bot
        return redirect(url_for("landing.index") + "?sent=1#contact")

    name = request.form.get("name", "").strip()
    email = request.form.get("email", "").strip()
    interest = request.form.get("interest", "").strip()
    message = request.form.get("message", "").strip()

    if not name or not email:
        flash("Please fill in all required fields.", "error")
        return redirect(url_for("landing.index") + "#contact")

    if not _EMAIL_RE.match(email):
        flash("Please enter a valid email address.", "error")
        return redirect(url_for("landing.index") + "#contact")

    db_module.save_contact(name, email, message, services=interest)
    current_app.logger.info(
        "Contact form submission — name: %r  email: %r  interest: %r",
        name, email, interest,
    )

    # Fire-and-forget in background thread — never blocks the response
    _send_email_notification(name, email, interest, message)

    return redirect(url_for("landing.index") + "?sent=1#contact")
