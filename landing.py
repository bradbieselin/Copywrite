"""Marketing landing page — Flask Blueprint."""

import os
from flask import Blueprint, render_template, request, redirect, url_for, flash, current_app

import db as db_module

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


@landing_bp.route("/contact", methods=["POST"])
def contact():
    # Honeypot: bots fill the hidden "url" field, humans never see it
    if request.form.get("url", "").strip():
        # Silent success — don't tip off the bot
        return redirect(url_for("landing.index") + "?sent=1#contact")

    name = request.form.get("name", "").strip()
    email = request.form.get("email", "").strip()
    message = request.form.get("message", "").strip()

    if not name or not email or not message:
        flash("Please fill in all fields.", "error")
        return redirect(url_for("landing.index") + "#contact")

    db_module.save_contact(name, email, message)
    current_app.logger.info(
        "Contact form submission — name: %r  email: %r  message: %r",
        name, email, message[:200],
    )
    return redirect(url_for("landing.index") + "?sent=1#contact")
