"""Admin portal Blueprint."""

import os
import uuid

from flask import (
    Blueprint, render_template, request, redirect,
    url_for, flash, current_app,
)
from werkzeug.utils import secure_filename

import db as db_module
from portal.auth import admin_required

admin_bp = Blueprint("portal_admin", __name__)

_ALLOWED = {"txt", "pdf", "doc", "docx"}


def _allowed(filename: str) -> bool:
    return "." in filename and filename.rsplit(".", 1)[1].lower() in _ALLOWED


# ── dashboard ─────────────────────────────────────────────────────────────────

@admin_bp.route("/")
@admin_required
def dashboard():
    briefs = db_module.get_all_briefs()
    clients = db_module.get_all_clients()
    return render_template(
        "portal/admin/dashboard.html", briefs=briefs, clients=clients
    )


# ── brief detail / actions ────────────────────────────────────────────────────

@admin_bp.route("/briefs/<int:brief_id>", methods=["GET", "POST"])
@admin_required
def brief_detail(brief_id):
    brief = db_module.get_brief(brief_id)
    if not brief:
        flash("Brief not found.", "danger")
        return redirect(url_for("portal_admin.dashboard"))

    error = None

    if request.method == "POST":
        action = request.form.get("action", "")

        if action == "mark_in_progress":
            db_module.update_brief_status(brief_id, "in_progress")
            flash("Brief marked as in progress.", "success")
            return redirect(url_for("portal_admin.brief_detail", brief_id=brief_id))

        elif action == "mark_complete":
            db_module.mark_brief_complete(brief_id)
            flash("Brief marked as complete.", "success")
            return redirect(url_for("portal_admin.brief_detail", brief_id=brief_id))

        elif action == "upload_copy":
            if "copy_file" not in request.files or request.files["copy_file"].filename == "":
                error = "No file selected."
            else:
                file = request.files["copy_file"]
                if not _allowed(file.filename):
                    error = "Only .txt, .pdf, .doc, and .docx files are allowed."
                else:
                    original = secure_filename(file.filename)
                    storage = f"{brief_id}_{uuid.uuid4().hex}_{original}"
                    upload_dir = current_app.config["UPLOAD_FOLDER"]
                    os.makedirs(upload_dir, exist_ok=True)
                    file.save(os.path.join(upload_dir, storage))

                    from flask import session as flask_session
                    db_module.save_copy_file(
                        brief_id, original, storage, flask_session["user_id"]
                    )
                    db_module.mark_brief_complete(brief_id)
                    flash("Copy uploaded and brief marked as complete.", "success")
                    return redirect(
                        url_for("portal_admin.brief_detail", brief_id=brief_id)
                    )

    brief = db_module.get_brief(brief_id)
    copy_file = db_module.get_copy_file(brief_id)
    return render_template(
        "portal/admin/brief_detail.html",
        brief=brief,
        copy_file=copy_file,
        error=error,
    )


# ── create client ─────────────────────────────────────────────────────────────

@admin_bp.route("/clients/new", methods=["POST"])
@admin_required
def create_client():
    name = request.form.get("name", "").strip()
    email = request.form.get("email", "").strip()
    password = request.form.get("password", "").strip()

    if not name or not email or not password:
        flash("All fields are required to create a client account.", "danger")
        return redirect(url_for("portal_admin.dashboard"))
    if len(password) < 8:
        flash("Password must be at least 8 characters.", "danger")
        return redirect(url_for("portal_admin.dashboard"))

    try:
        db_module.create_user(name, email, password, "client")
        flash(f"Client account created for {email}.", "success")
    except Exception as exc:
        if "UNIQUE" in str(exc):
            flash(f"{email} is already registered.", "danger")
        else:
            flash(f"Error creating account: {exc}", "danger")

    return redirect(url_for("portal_admin.dashboard"))
