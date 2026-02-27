"""Portal authentication — login, logout, and route decorators."""

from functools import wraps
from urllib.parse import urlparse, urljoin

from flask import (
    Blueprint, render_template, request, redirect,
    url_for, session, flash,
)
from werkzeug.security import check_password_hash

import db as db_module

auth_bp = Blueprint("portal_auth", __name__)


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
        user = db_module.get_user_by_email(email)

        if user and check_password_hash(user["password_hash"], password):
            session.clear()
            session["user_id"] = user["id"]
            session["user_name"] = user["name"]
            session["user_role"] = user["role"]
            session["user_email"] = user["email"]
            if user["role"] == "admin":
                return redirect(_next_url(url_for("portal_admin.dashboard")))
            return redirect(_next_url(url_for("portal_client.dashboard")))

        error = "Invalid email or password."

    return render_template("portal/login.html", error=error)


@auth_bp.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("portal_auth.login"))
