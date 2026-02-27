"""
Copywrite — Flask web app suite
  /          → Cold DM Generator
  /intake    → Client Copy Generator
"""

import os
from flask import Flask

from db import init_db


def create_app() -> Flask:
    app = Flask(__name__)
    app.config["ANTHROPIC_API_KEY"] = os.environ.get("ANTHROPIC_API_KEY", "")

    from dm import dm_bp
    from intake import intake_bp

    app.register_blueprint(dm_bp)
    app.register_blueprint(intake_bp, url_prefix="/intake")

    with app.app_context():
        init_db()

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
