"""Marketing landing page — Flask Blueprint."""

from flask import Blueprint, render_template, request, redirect, url_for, flash

import db as db_module

landing_bp = Blueprint("landing", __name__)


@landing_bp.route("/")
def index():
    sent = request.args.get("sent") == "1"
    return render_template("landing.html", sent=sent)


@landing_bp.route("/contact", methods=["POST"])
def contact():
    name = request.form.get("name", "").strip()
    email = request.form.get("email", "").strip()
    message = request.form.get("message", "").strip()

    if not name or not email or not message:
        flash("Please fill in all fields.", "error")
        return redirect(url_for("landing.index") + "#contact")

    db_module.save_contact(name, email, message)
    return redirect(url_for("landing.index") + "?sent=1#contact")
