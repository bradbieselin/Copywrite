"""
Copywrite — Flask web app suite
  /              → Cold DM Generator
  /intake        → Anonymous Copy Generator
  /portal/login  → Client Portal (login, client dashboard, admin dashboard)
"""

import os
from flask import Flask

from db import init_db, init_portal_db


def create_app() -> Flask:
    app = Flask(__name__)

    app.config["ANTHROPIC_API_KEY"] = os.environ.get("ANTHROPIC_API_KEY", "")
    app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "dev-secret-change-in-prod")
    app.config["UPLOAD_FOLDER"] = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "uploads"
    )
    # Limit uploaded files to 16 MB
    app.config["MAX_CONTENT_LENGTH"] = 16 * 1024 * 1024

    # SendGrid email notifications (optional — automation skips if unset)
    app.config["SENDGRID_API_KEY"]    = os.environ.get("SENDGRID_API_KEY", "")
    app.config["SENDGRID_FROM_EMAIL"] = os.environ.get("SENDGRID_FROM_EMAIL", "")
    app.config["ADMIN_EMAIL"]         = os.environ.get("ADMIN_EMAIL", "")
    # Base URL used to build deep-links in emails, e.g. https://yourapp.com
    app.config["APP_BASE_URL"]        = os.environ.get("APP_BASE_URL", "http://localhost:5000")

    # Public tools
    from dm import dm_bp
    from intake import intake_bp
    app.register_blueprint(dm_bp)
    app.register_blueprint(intake_bp, url_prefix="/intake")

    # Client portal
    from portal.auth import auth_bp
    from portal.client import client_bp
    from portal.admin import admin_bp
    app.register_blueprint(auth_bp, url_prefix="/portal")
    app.register_blueprint(client_bp, url_prefix="/portal/client")
    app.register_blueprint(admin_bp, url_prefix="/portal/admin")

    with app.app_context():
        init_db()
        init_portal_db()

    return app


app = create_app()

if __name__ == "__main__":
    if not app.config["ANTHROPIC_API_KEY"]:
        print(
            "WARNING: ANTHROPIC_API_KEY is not set.\n"
            "Export your key before running:\n"
            "  export ANTHROPIC_API_KEY='your_key_here'"
        )
    app.run(debug=True, port=5000)
