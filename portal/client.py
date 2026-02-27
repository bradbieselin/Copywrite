"""Client-facing portal Blueprint."""

import os
import threading
import uuid

from flask import (
    Blueprint, render_template, request, redirect,
    url_for, session, flash, send_file, current_app,
)
from werkzeug.security import check_password_hash
from werkzeug.utils import secure_filename

import db as db_module
from portal.auth import login_required

client_bp = Blueprint("portal_client", __name__)


def _start_automation(brief_id: int, app) -> None:
    """
    Fetch the saved brief and run the full automation pipeline in a
    daemon thread so the client request returns immediately.
    The thread captures everything it needs — no Flask context required.
    """
    from portal.automation import run_brief_automation

    brief = db_module.get_brief(brief_id)
    config = {
        k: app.config.get(k, "")
        for k in ("ANTHROPIC_API_KEY", "SENDGRID_API_KEY",
                  "SENDGRID_FROM_EMAIL", "ADMIN_EMAIL", "APP_BASE_URL")
    }

    def _run():
        run_brief_automation(brief, config)

    t = threading.Thread(target=_run, daemon=True)
    t.start()

TONES = ["professional", "casual", "bold", "friendly"]
COPY_TYPES = ["email", "Instagram caption", "Facebook ad", "landing page headline"]
_REF_ALLOWED = {"jpg", "jpeg", "png", "gif", "webp", "pdf", "doc", "docx", "txt", "zip"}


def _ref_allowed(filename: str) -> bool:
    return "." in filename and filename.rsplit(".", 1)[1].lower() in _REF_ALLOWED


def _save_reference_files(brief_id: int, files, upload_dir: str, uploader_id: int) -> None:
    """Save any uploaded reference files and record them in the DB."""
    os.makedirs(upload_dir, exist_ok=True)
    for f in files:
        if f and f.filename and _ref_allowed(f.filename):
            original = secure_filename(f.filename)
            storage = f"ref_{brief_id}_{uuid.uuid4().hex}_{original}"
            f.save(os.path.join(upload_dir, storage))
            db_module.save_copy_file(brief_id, original, storage, uploader_id, "reference")
_REQUIRED = [
    "title", "product_name", "product_description",
    "target_audience", "main_benefit", "biggest_objection",
    "tone", "copy_type",
]


@client_bp.route("/")
@login_required
def dashboard():
    briefs = db_module.get_client_briefs(session["user_id"])
    return render_template("portal/client/dashboard.html", briefs=briefs)


@client_bp.route("/briefs/new", methods=["GET", "POST"])
@login_required
def new_brief():
    error = None
    form_data = {}

    if request.method == "POST":
        all_fields = _REQUIRED + ["notes"]
        form_data = {f: request.form.get(f, "").strip() for f in all_fields}

        if any(not form_data[f] for f in _REQUIRED):
            error = "Please fill in all required fields."
        elif form_data["tone"] not in TONES:
            error = "Invalid tone selection."
        elif form_data["copy_type"] not in COPY_TYPES:
            error = "Invalid copy type selection."
        else:
            brief_id = db_module.create_brief(session["user_id"], form_data)
            # Save any optional reference files
            ref_files = request.files.getlist("reference_files")
            if ref_files:
                _save_reference_files(
                    brief_id,
                    ref_files,
                    current_app.config["UPLOAD_FOLDER"],
                    session["user_id"],
                )
            _start_automation(brief_id, current_app)
            flash("Brief submitted! We'll be in touch.", "success")
            return redirect(url_for("portal_client.brief_detail", brief_id=brief_id))

    return render_template(
        "portal/client/new_brief.html",
        error=error,
        form_data=form_data,
        tones=TONES,
        copy_types=COPY_TYPES,
    )


@client_bp.route("/briefs/<int:brief_id>")
@login_required
def brief_detail(brief_id):
    brief = db_module.get_brief(brief_id)
    if not brief or brief["client_id"] != session["user_id"]:
        flash("Brief not found.", "danger")
        return redirect(url_for("portal_client.dashboard"))
    copy_file = db_module.get_copy_file(brief_id)
    reference_files = db_module.get_reference_files(brief_id)
    return render_template(
        "portal/client/brief_detail.html",
        brief=brief,
        copy_file=copy_file,
        reference_files=reference_files,
    )


@client_bp.route("/settings", methods=["GET", "POST"])
@login_required
def settings():
    error = None
    success = None

    if request.method == "POST":
        current_pw = request.form.get("current_password", "")
        new_pw     = request.form.get("new_password", "").strip()
        confirm_pw = request.form.get("confirm_password", "").strip()

        user = db_module.get_user_by_email(session["user_email"])

        if not check_password_hash(user["password_hash"], current_pw):
            error = "Current password is incorrect."
        elif len(new_pw) < 8:
            error = "New password must be at least 8 characters."
        elif new_pw != confirm_pw:
            error = "Passwords do not match."
        else:
            db_module.update_password(session["user_id"], new_pw)
            success = "Password updated successfully."

    return render_template("portal/client/settings.html", error=error, success=success)


@client_bp.route("/briefs/<int:brief_id>/download")
@login_required
def download_copy(brief_id):
    brief = db_module.get_brief(brief_id)
    if not brief or brief["client_id"] != session["user_id"]:
        flash("File not found.", "danger")
        return redirect(url_for("portal_client.dashboard"))

    if brief["status"] != "completed":
        flash("Your copy isn't ready yet.", "warning")
        return redirect(url_for("portal_client.brief_detail", brief_id=brief_id))

    copy_file = db_module.get_copy_file(brief_id)
    if not copy_file:
        flash("No file has been uploaded yet.", "warning")
        return redirect(url_for("portal_client.brief_detail", brief_id=brief_id))

    file_path = os.path.join(
        current_app.config["UPLOAD_FOLDER"], copy_file["storage_filename"]
    )
    if not os.path.exists(file_path):
        flash("File not found on server. Please contact us.", "danger")
        return redirect(url_for("portal_client.brief_detail", brief_id=brief_id))

    return send_file(
        file_path,
        as_attachment=True,
        download_name=copy_file["original_filename"],
    )
