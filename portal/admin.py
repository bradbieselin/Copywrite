"""Admin portal Blueprint."""

import datetime
import os
import secrets
import threading
import uuid

from flask import (
    Blueprint, render_template, request, redirect,
    url_for, flash, current_app, session as flask_session,
    jsonify, send_file,
)
from werkzeug.security import check_password_hash
from werkzeug.utils import secure_filename

import db as db_module
from portal.auth import admin_required

admin_bp = Blueprint("portal_admin", __name__)

# ── Lead Scraper state (module-level; fine for a single-process deployment) ───

_scraper_state: dict = {
    "status": "idle",   # idle | running | done | error
    "log": [],
    "summary": None,
    "started_at": None,
    "finished_at": None,
}
_scraper_lock = threading.Lock()
_scraper_stop_event = threading.Event()

_ALLOWED = {"txt", "pdf", "doc", "docx"}


def _allowed(filename: str) -> bool:
    return "." in filename and filename.rsplit(".", 1)[1].lower() in _ALLOWED


# ── dashboard ─────────────────────────────────────────────────────────────────

@admin_bp.route("/")
@admin_required
def dashboard():
    clients = db_module.get_clients_with_stats()
    stats = db_module.get_dashboard_stats()
    active_briefs = db_module.get_active_briefs()
    return render_template(
        "portal/admin/dashboard.html",
        clients=clients,
        stats=stats,
        active_briefs=active_briefs,
    )


# ── per-client detail ─────────────────────────────────────────────────────────

@admin_bp.route("/clients/<int:client_id>")
@admin_required
def client_detail(client_id):
    client = db_module.get_client(client_id)
    if not client:
        flash("Client not found.", "danger")
        return redirect(url_for("portal_admin.dashboard"))
    briefs = db_module.get_client_briefs(client_id)
    return render_template(
        "portal/admin/client_detail.html", client=client, briefs=briefs
    )


@admin_bp.route("/clients/<int:client_id>/reset-password", methods=["POST"])
@admin_required
def reset_client_password(client_id):
    client = db_module.get_client(client_id)
    if not client:
        flash("Client not found.", "danger")
        return redirect(url_for("portal_admin.dashboard"))
    new_pw = request.form.get("new_password", "").strip()
    if len(new_pw) < 8:
        flash("Password must be at least 8 characters.", "danger")
    else:
        db_module.update_password(client_id, new_pw)
        flash(f"Password reset for {client['name']}.", "success")
    return redirect(url_for("portal_admin.client_detail", client_id=client_id))


@admin_bp.route("/clients/<int:client_id>/delete", methods=["POST"])
@admin_required
def delete_client(client_id):
    client = db_module.get_client(client_id)
    if not client:
        flash("Client not found.", "danger")
        return redirect(url_for("portal_admin.dashboard"))
    db_module.delete_client(client_id)
    flash(f"{client['name']} and all their briefs have been deleted.", "success")
    return redirect(url_for("portal_admin.dashboard"))


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

        elif action == "save_draft":
            draft_text = request.form.get("draft", "").strip()
            db_module.save_draft(brief_id, draft_text)
            flash("Draft saved.", "success")
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
    name  = request.form.get("name", "").strip()
    email = request.form.get("email", "").strip()

    if not name or not email:
        flash("Name and email are required.", "danger")
        return redirect(url_for("portal_admin.dashboard"))

    temp_pw = secrets.token_urlsafe(10)

    try:
        user_id = db_module.create_user(name, email, temp_pw, "client")
        db_module.set_must_reset_password(user_id, True)

        # Send welcome email in background (fails silently if SendGrid not set up)
        _send_welcome_async(name, email, temp_pw, current_app)

        flash(
            f"Account created for {email}. "
            f"Temp password (shown once): {temp_pw}",
            "success",
        )
    except Exception as exc:
        if "UNIQUE" in str(exc):
            flash(f"{email} is already registered.", "danger")
        else:
            flash(f"Error creating account: {exc}", "danger")

    return redirect(url_for("portal_admin.dashboard"))


def _send_welcome_async(name: str, email: str, temp_pw: str, app) -> None:
    """Fire-and-forget welcome email in a daemon thread."""
    from portal.automation import send_welcome_email
    config = {k: app.config.get(k, "") for k in
              ("SENDGRID_API_KEY", "SENDGRID_FROM_EMAIL", "APP_BASE_URL")}

    def _run():
        try:
            send_welcome_email(name, email, temp_pw, config)
        except Exception:
            import logging
            logging.getLogger(__name__).exception(
                "Failed to send welcome email to %s.", email
            )

    threading.Thread(target=_run, daemon=True).start()


# ── create admin ──────────────────────────────────────────────────────────────

@admin_bp.route("/admins/new", methods=["POST"])
@admin_required
def create_admin():
    name = request.form.get("name", "").strip()
    email = request.form.get("email", "").strip()
    password = request.form.get("password", "").strip()

    if not name or not email or not password:
        flash("All fields are required to create an admin account.", "danger")
        return redirect(url_for("portal_admin.dashboard"))
    if len(password) < 8:
        flash("Password must be at least 8 characters.", "danger")
        return redirect(url_for("portal_admin.dashboard"))

    try:
        db_module.create_user(name, email, password, "admin")
        flash(f"Admin account created for {email}.", "success")
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


# ── Lead Scraper ───────────────────────────────────────────────────────────────

def _leads_csv_path() -> str:
    return os.path.join(current_app.config["UPLOAD_FOLDER"], "leads.csv")


def _run_scraper_thread(hashtags: list[str], max_results: int, output_file: str, token: str) -> None:
    from instagram_dtc_scraper import run_scraper

    def log(msg: str) -> None:
        ts = datetime.datetime.now().strftime("%H:%M:%S")
        with _scraper_lock:
            _scraper_state["log"].append(f"[{ts}] {msg}")

    try:
        summary = run_scraper(
            hashtags=hashtags,
            max_results=max_results,
            output_file=output_file,
            token=token,
            on_status=log,
            stop_event=_scraper_stop_event,
        )
        with _scraper_lock:
            if _scraper_stop_event.is_set():
                _scraper_state["status"] = "stopped"
            else:
                _scraper_state["status"] = "done"
                _scraper_state["summary"] = summary
            _scraper_state["finished_at"] = datetime.datetime.now().isoformat(timespec="seconds")
    except Exception as exc:
        with _scraper_lock:
            _scraper_state["status"] = "error"
            _scraper_state["log"].append(f"[ERROR] {exc}")
            _scraper_state["finished_at"] = datetime.datetime.now().isoformat(timespec="seconds")


@admin_bp.route("/scraper")
@admin_required
def scraper():
    token_set = bool(current_app.config.get("APIFY_API_TOKEN"))
    csv_path = _leads_csv_path()
    has_csv = os.path.exists(csv_path)
    csv_size = None
    if has_csv:
        size_bytes = os.path.getsize(csv_path)
        csv_size = f"{size_bytes / 1024:.1f} KB" if size_bytes >= 1024 else f"{size_bytes} B"
    with _scraper_lock:
        state = dict(_scraper_state)
    return render_template(
        "portal/admin/scraper.html",
        state=state,
        token_set=token_set,
        has_csv=has_csv,
        csv_size=csv_size,
    )


@admin_bp.route("/scraper/run", methods=["POST"])
@admin_required
def scraper_run():
    with _scraper_lock:
        if _scraper_state["status"] == "running":
            flash("A scraper run is already in progress.", "warning")
            return redirect(url_for("portal_admin.scraper"))

    token = current_app.config.get("APIFY_API_TOKEN", "")
    if not token:
        flash("APIFY_API_TOKEN is not configured. Add it to your .env file.", "danger")
        return redirect(url_for("portal_admin.scraper"))

    # Quick pre-flight: verify the token reaches Apify before spawning a thread.
    try:
        from apify_client import ApifyClient as _AC
        user_info = _AC(token).user("me").get()
        if not user_info:
            raise ValueError("Token rejected — Apify returned no user data.")
    except Exception as _e:
        flash(
            f"Apify token validation failed: {_e}. "
            "Check that APIFY_API_TOKEN in your .env is correct and not expired.",
            "danger",
        )
        return redirect(url_for("portal_admin.scraper"))

    raw_tags = request.form.get("hashtags", "").strip()
    hashtags = [t.strip().lstrip("#") for t in raw_tags.replace(",", "\n").splitlines() if t.strip()]
    if not hashtags:
        flash("Enter at least one hashtag.", "danger")
        return redirect(url_for("portal_admin.scraper"))

    try:
        max_results = min(max(int(request.form.get("max_results", 200)), 10), 500)
    except (ValueError, TypeError):
        max_results = 200
    output_file = _leads_csv_path()

    _scraper_stop_event.clear()
    with _scraper_lock:
        _scraper_state["status"] = "running"
        _scraper_state["log"] = []
        _scraper_state["summary"] = None
        _scraper_state["started_at"] = datetime.datetime.now().isoformat(timespec="seconds")
        _scraper_state["finished_at"] = None

    t = threading.Thread(
        target=_run_scraper_thread,
        args=(hashtags, max_results, output_file, token),
        daemon=True,
    )
    t.start()

    return redirect(url_for("portal_admin.scraper"))


@admin_bp.route("/scraper/stop", methods=["POST"])
@admin_required
def scraper_stop():
    with _scraper_lock:
        if _scraper_state["status"] == "running":
            _scraper_stop_event.set()
    return redirect(url_for("portal_admin.scraper"))


@admin_bp.route("/scraper/status")
@admin_required
def scraper_status():
    with _scraper_lock:
        return jsonify(dict(_scraper_state))


@admin_bp.route("/scraper/download")
@admin_required
def scraper_download():
    csv_path = _leads_csv_path()
    if not os.path.exists(csv_path):
        flash("No leads file found. Run the scraper first.", "warning")
        return redirect(url_for("portal_admin.scraper"))
    return send_file(csv_path, as_attachment=True, download_name="leads.csv")


@admin_bp.route("/scraper/leads.json")
@admin_required
def scraper_leads_json():
    import csv as csv_module
    csv_path = _leads_csv_path()
    if not os.path.exists(csv_path):
        return jsonify([])
    rows = []
    with open(csv_path, newline="", encoding="utf-8") as f:
        for row in csv_module.DictReader(f):
            rows.append(row)
    return jsonify(rows)
