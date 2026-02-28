"""Portal authentication — login, logout, and route decorators."""

import time
from functools import wraps
from urllib.parse import urlparse, urljoin

from flask import (
    Blueprint, render_template, request, redirect,
    url_for, session, flash,
)
from werkzeug.security import check_password_hash

import db as db_module

auth_bp = Blueprint("portal_auth", __name__)

# ── rate limiting ─────────────────────────────────────────────────────────────
# { email_lower: {"count": int, "first_at": float} }
_FAILED_LOGINS: dict = {}
_MAX_ATTEMPTS  = 5
_LOCKOUT_SECS  = 15 * 60   # 15 minutes
_MAX_TRACKED   = 10_000     # cap to prevent memory exhaustion


def _evict_expired() -> None:
    """Remove entries whose lockout window has expired."""
    now = time.time()
    expired = [k for k, v in _FAILED_LOGINS.items()
               if now - v["first_at"] > _LOCKOUT_SECS]
    for k in expired:
        _FAILED_LOGINS.pop(k, None)


def _is_locked_out(email: str) -> bool:
    entry = _FAILED_LOGINS.get(email)
    if not entry:
        return False
    if time.time() - entry["first_at"] > _LOCKOUT_SECS:
        _FAILED_LOGINS.pop(email, None)
        return False
    return entry["count"] >= _MAX_ATTEMPTS


def _record_failure(email: str) -> None:
    # Prevent unbounded growth from brute-force with random emails
    if len(_FAILED_LOGINS) >= _MAX_TRACKED:
        _evict_expired()
    if len(_FAILED_LOGINS) >= _MAX_TRACKED:
        return  # silently refuse to track more; existing lockouts still enforced

    entry = _FAILED_LOGINS.get(email)
    now = time.time()
    if not entry or (now - entry["first_at"] > _LOCKOUT_SECS):
        _FAILED_LOGINS[email] = {"count": 1, "first_at": now}
    else:
        entry["count"] += 1


def _clear_failures(email: str) -> None:
    _FAILED_LOGINS.pop(email, None)


# ── helpers ───────────────────────────────────────────────────────────────────

def _is_safe_redirect(target: str) -> bool:
    """Prevent open-redirect attacks — only allow same-host relative URLs."""
    ref = urlparse(request.host_url)
    test = urlparse(urljoin(request.host_url, target))
    return test.scheme in ("http", "https") and ref.netloc == test.netloc


def _next_url(fallback: str) -> str:
    target = request.form.get("next") or request.args.get("next", "")
    return target if (target and _is_safe_redirect(target)) else fallback


# ── decorators ────────────────────────────────────────────────────────────────

def login_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if "user_id" not in session:
            return redirect(url_for("portal_auth.login", next=request.path))
        return f(*args, **kwargs)
    return decorated


def admin_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if "user_id" not in session:
            return redirect(url_for("portal_auth.login", next=request.path))
        if session.get("user_role") != "admin":
            flash("Admin access required.", "danger")
            return redirect(url_for("portal_client.dashboard"))
        return f(*args, **kwargs)
    return decorated


# ── routes ────────────────────────────────────────────────────────────────────

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if "user_id" in session:
        if session.get("user_role") == "admin":
            return redirect(url_for("portal_admin.dashboard"))
        return redirect(url_for("portal_client.dashboard"))

    error = None

    if request.method == "POST":
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")

        if _is_locked_out(email):
            error = (
                "Too many failed attempts. "
                "Please wait 15 minutes before trying again."
            )
        else:
            user = db_module.get_user_by_email(email)

            if user and check_password_hash(user["password_hash"], password):
                _clear_failures(email)
                session.clear()
                session["user_id"] = user["id"]
                session["user_name"] = user["name"]
                session["user_role"] = user["role"]
                session["user_email"] = user["email"]
                if user["role"] == "admin":
                    return redirect(_next_url(url_for("portal_admin.dashboard")))
                if user.get("must_reset_password"):
                    session["must_reset_password"] = True
                    flash("Welcome! Please set a new password before continuing.", "warning")
                    return redirect(url_for("portal_client.settings"))
                return redirect(_next_url(url_for("portal_client.dashboard")))

            _record_failure(email)
            error = "Invalid email or password."

    return render_template("portal/login.html", error=error)


@auth_bp.route("/logout", methods=["POST"])
def logout():
    session.clear()
    return redirect(url_for("portal_auth.login"))
