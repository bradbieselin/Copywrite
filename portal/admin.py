"""Admin portal Blueprint."""

import os
import threading
import uuid

from flask import (
    Blueprint, render_template, request, redirect,
    url_for, flash, current_app, session as flask_session,
)
from werkzeug.security import check_password_hash
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
    stats = db_module.get_dashboard_stats()
    return render_template(
        "portal/admin/dashboard.html", briefs=briefs, clients=clients, stats=stats
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
            brief = db_module.get_brief(brief_id)
            _notify_client_completion(brief, current_app.config)
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

                    db_module.save_copy_file(
                        brief_id, original, storage, flask_session["user_id"]
                    )
                    db_module.mark_brief_complete(brief_id)
                    brief = db_module.get_brief(brief_id)
                    _notify_client_completion(brief, current_app.config)
                    flash("Copy uploaded and brief marked as complete.", "success")
                    return redirect(
                        url_for("portal_admin.brief_detail", brief_id=brief_id)
                    )

    brief = db_module.get_brief(brief_id)
    copy_file = db_module.get_copy_file(brief_id)
    reference_files = db_module.get_reference_files(brief_id)
    return render_template(
        "portal/admin/brief_detail.html",
        brief=brief,
        copy_file=copy_file,
        reference_files=reference_files,
        error=error,
    )


# ── completion notification helper ────────────────────────────────────────────

def _notify_client_completion(brief: dict, config: dict) -> None:
    """Fire-and-forget: email the client that their copy is ready."""
    from portal.automation import send_completion_notification
    t = threading.Thread(
        target=send_completion_notification,
        args=(brief, dict(config)),
        daemon=True,
    )
    t.start()


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


# ── settings (change password) ────────────────────────────────────────────────

@admin_bp.route("/settings", methods=["GET", "POST"])
@admin_required
def settings():
    error = None
    success = None

    if request.method == "POST":
        current_pw  = request.form.get("current_password", "")
        new_pw      = request.form.get("new_password", "").strip()
        confirm_pw  = request.form.get("confirm_password", "").strip()

        user = db_module.get_user_by_email(flask_session["user_email"])

        if not check_password_hash(user["password_hash"], current_pw):
            error = "Current password is incorrect."
        elif len(new_pw) < 8:
            error = "New password must be at least 8 characters."
        elif new_pw != confirm_pw:
            error = "New passwords do not match."
        else:
            db_module.update_password(flask_session["user_id"], new_pw)
            success = "Password updated successfully."

    return render_template("portal/admin/settings.html", error=error, success=success)
