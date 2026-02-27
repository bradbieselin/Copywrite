"""SQLite helpers for Copywrite."""

import os
import sqlite3

from werkzeug.security import generate_password_hash

DB_PATH = os.environ.get(
    "DB_PATH",
    os.path.join(os.path.dirname(os.path.abspath(__file__)), "copywrite.db"),
)

# ── anonymous intake tool ─────────────────────────────────────────────────────

def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        conn.executescript("""
            CREATE TABLE IF NOT EXISTS submissions (
                id                  INTEGER PRIMARY KEY AUTOINCREMENT,
                created_at          TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                product_name        TEXT NOT NULL,
                product_description TEXT NOT NULL,
                target_audience     TEXT NOT NULL,
                main_benefit        TEXT NOT NULL,
                biggest_objection   TEXT NOT NULL,
                tone                TEXT NOT NULL,
                copy_type           TEXT NOT NULL,
                variation_1         TEXT NOT NULL,
                variation_2         TEXT NOT NULL,
                variation_3         TEXT NOT NULL
            );

            CREATE TABLE IF NOT EXISTS contact_submissions (
                id         INTEGER PRIMARY KEY AUTOINCREMENT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                name       TEXT NOT NULL,
                email      TEXT NOT NULL,
                message    TEXT NOT NULL
            );
        """)


def save_contact(name: str, email: str, message: str) -> int:
    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.execute(
            "INSERT INTO contact_submissions (name, email, message) VALUES (?,?,?)",
            (name.strip(), email.strip(), message.strip()),
        )
        return cur.lastrowid


def save_submission(data: dict) -> int:
    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.execute(
            """
            INSERT INTO submissions
              (product_name, product_description, target_audience, main_benefit,
               biggest_objection, tone, copy_type, variation_1, variation_2, variation_3)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                data["product_name"],
                data["product_description"],
                data["target_audience"],
                data["main_benefit"],
                data["biggest_objection"],
                data["tone"],
                data["copy_type"],
                data["variation_1"],
                data["variation_2"],
                data["variation_3"],
            ),
        )
        return cur.lastrowid


# ── client portal ─────────────────────────────────────────────────────────────

def init_portal_db():
    """Create portal tables and seed the default admin account if missing."""
    with sqlite3.connect(DB_PATH) as conn:
        conn.executescript("""
            CREATE TABLE IF NOT EXISTS portal_users (
                id            INTEGER PRIMARY KEY AUTOINCREMENT,
                created_at    TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                name          TEXT NOT NULL,
                email         TEXT UNIQUE NOT NULL,
                password_hash TEXT NOT NULL,
                role          TEXT NOT NULL CHECK(role IN ('client', 'admin'))
            );

            CREATE TABLE IF NOT EXISTS briefs (
                id                  INTEGER PRIMARY KEY AUTOINCREMENT,
                created_at          TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                client_id           INTEGER NOT NULL REFERENCES portal_users(id),
                title               TEXT NOT NULL,
                product_name        TEXT NOT NULL,
                product_description TEXT NOT NULL,
                target_audience     TEXT NOT NULL,
                main_benefit        TEXT NOT NULL,
                biggest_objection   TEXT NOT NULL,
                tone                TEXT NOT NULL,
                copy_type           TEXT NOT NULL,
                notes               TEXT NOT NULL DEFAULT '',
                status              TEXT NOT NULL DEFAULT 'pending'
                                    CHECK(status IN ('pending','in_progress','completed')),
                completed_at        TIMESTAMP
            );

            CREATE TABLE IF NOT EXISTS copy_files (
                id                INTEGER PRIMARY KEY AUTOINCREMENT,
                uploaded_at       TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                brief_id          INTEGER NOT NULL REFERENCES briefs(id),
                original_filename TEXT NOT NULL,
                storage_filename  TEXT NOT NULL,
                uploaded_by       INTEGER NOT NULL REFERENCES portal_users(id)
            );
        """)

        # Migrate: add `draft` column to briefs for existing databases.
        existing_cols = {
            row[1]
            for row in conn.execute("PRAGMA table_info(briefs)").fetchall()
        }
        if "draft" not in existing_cols:
            conn.execute("ALTER TABLE briefs ADD COLUMN draft TEXT")

        # Migrate: add `file_type` column to copy_files for existing databases.
        file_cols = {
            row[1]
            for row in conn.execute("PRAGMA table_info(copy_files)").fetchall()
        }
        if "file_type" not in file_cols:
            conn.execute(
                "ALTER TABLE copy_files ADD COLUMN file_type TEXT NOT NULL DEFAULT 'delivery'"
            )

        admin = conn.execute(
            "SELECT id FROM portal_users WHERE role='admin' LIMIT 1"
        ).fetchone()

        if not admin:
            conn.execute(
                "INSERT INTO portal_users (name, email, password_hash, role) VALUES (?,?,?,?)",
                ("Admin", "admin@copywrite.io",
                 generate_password_hash("admin123"), "admin"),
            )
            print(
                "\n[Portal] Default admin created — "
                "email: admin@copywrite.io  password: admin123\n"
                "Change this password after first login.\n"
            )


# ── users ─────────────────────────────────────────────────────────────────────

def _row_to_dict(row):
    return dict(row) if row else None


def get_user_by_email(email: str) -> dict | None:
    with sqlite3.connect(DB_PATH) as conn:
        conn.row_factory = sqlite3.Row
        row = conn.execute(
            "SELECT * FROM portal_users WHERE email = ?", (email.lower().strip(),)
        ).fetchone()
        return _row_to_dict(row)


def create_user(name: str, email: str, password: str, role: str) -> int:
    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.execute(
            "INSERT INTO portal_users (name, email, password_hash, role) VALUES (?,?,?,?)",
            (name.strip(), email.lower().strip(),
             generate_password_hash(password), role),
        )
        return cur.lastrowid


def update_password(user_id: int, new_password: str) -> None:
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute(
            "UPDATE portal_users SET password_hash = ? WHERE id = ?",
            (generate_password_hash(new_password), user_id),
        )


def get_all_clients() -> list[dict]:
    with sqlite3.connect(DB_PATH) as conn:
        conn.row_factory = sqlite3.Row
        rows = conn.execute(
            "SELECT id, name, email, created_at FROM portal_users "
            "WHERE role='client' ORDER BY name"
        ).fetchall()
        return [dict(r) for r in rows]


def get_client(client_id: int) -> dict | None:
    with sqlite3.connect(DB_PATH) as conn:
        conn.row_factory = sqlite3.Row
        row = conn.execute(
            "SELECT id, name, email, created_at FROM portal_users "
            "WHERE id = ? AND role = 'client'",
            (client_id,),
        ).fetchone()
        return _row_to_dict(row)


def get_clients_with_stats() -> list[dict]:
    """Return all clients with their brief counts broken down by status."""
    with sqlite3.connect(DB_PATH) as conn:
        conn.row_factory = sqlite3.Row
        rows = conn.execute(
            """
            SELECT
                u.id, u.name, u.email, u.created_at,
                COUNT(b.id) AS total_briefs,
                SUM(CASE WHEN b.status = 'pending'     THEN 1 ELSE 0 END) AS pending,
                SUM(CASE WHEN b.status = 'in_progress' THEN 1 ELSE 0 END) AS in_progress,
                SUM(CASE WHEN b.status = 'completed'   THEN 1 ELSE 0 END) AS completed
            FROM   portal_users u
            LEFT JOIN briefs b ON b.client_id = u.id
            WHERE  u.role = 'client'
            GROUP BY u.id
            ORDER BY u.name
            """
        ).fetchall()
        return [dict(r) for r in rows]


# ── briefs ────────────────────────────────────────────────────────────────────

def create_brief(client_id: int, form_data: dict) -> int:
    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.execute(
            """
            INSERT INTO briefs
              (client_id, title, product_name, product_description, target_audience,
               main_benefit, biggest_objection, tone, copy_type, notes)
            VALUES (?,?,?,?,?,?,?,?,?,?)
            """,
            (
                client_id,
                form_data["title"],
                form_data["product_name"],
                form_data["product_description"],
                form_data["target_audience"],
                form_data["main_benefit"],
                form_data["biggest_objection"],
                form_data["tone"],
                form_data["copy_type"],
                form_data.get("notes", ""),
            ),
        )
        return cur.lastrowid


def get_brief(brief_id: int) -> dict | None:
    with sqlite3.connect(DB_PATH) as conn:
        conn.row_factory = sqlite3.Row
        row = conn.execute(
            """
            SELECT b.*, u.name AS client_name, u.email AS client_email
            FROM   briefs b
            JOIN   portal_users u ON b.client_id = u.id
            WHERE  b.id = ?
            """,
            (brief_id,),
        ).fetchone()
        return _row_to_dict(row)


def get_client_briefs(client_id: int) -> list[dict]:
    with sqlite3.connect(DB_PATH) as conn:
        conn.row_factory = sqlite3.Row
        rows = conn.execute(
            "SELECT * FROM briefs WHERE client_id = ? ORDER BY created_at DESC",
            (client_id,),
        ).fetchall()
        return [dict(r) for r in rows]


def get_all_briefs() -> list[dict]:
    with sqlite3.connect(DB_PATH) as conn:
        conn.row_factory = sqlite3.Row
        rows = conn.execute(
            """
            SELECT b.*, u.name AS client_name, u.email AS client_email
            FROM   briefs b
            JOIN   portal_users u ON b.client_id = u.id
            ORDER BY
                CASE b.status
                    WHEN 'pending'     THEN 0
                    WHEN 'in_progress' THEN 1
                    WHEN 'completed'   THEN 2
                END,
                b.created_at DESC
            """
        ).fetchall()
        return [dict(r) for r in rows]


def update_brief_status(brief_id: int, status: str) -> None:
    with sqlite3.connect(DB_PATH) as conn:
        if status == "completed":
            conn.execute(
                "UPDATE briefs SET status=?, completed_at=CURRENT_TIMESTAMP WHERE id=?",
                (status, brief_id),
            )
        else:
            conn.execute(
                "UPDATE briefs SET status=?, completed_at=NULL WHERE id=?",
                (status, brief_id),
            )


def mark_brief_complete(brief_id: int) -> None:
    update_brief_status(brief_id, "completed")


# ── copy files ────────────────────────────────────────────────────────────────

def save_copy_file(
    brief_id: int,
    original_filename: str,
    storage_filename: str,
    uploaded_by: int,
    file_type: str = "delivery",
) -> int:
    with sqlite3.connect(DB_PATH) as conn:
        if file_type == "delivery":
            # Replace any existing delivery file
            conn.execute(
                "DELETE FROM copy_files WHERE brief_id = ? AND file_type = 'delivery'",
                (brief_id,),
            )
        cur = conn.execute(
            """
            INSERT INTO copy_files
              (brief_id, original_filename, storage_filename, uploaded_by, file_type)
            VALUES (?,?,?,?,?)
            """,
            (brief_id, original_filename, storage_filename, uploaded_by, file_type),
        )
        return cur.lastrowid


def get_copy_file(brief_id: int) -> dict | None:
    """Return the latest delivery file for a brief."""
    with sqlite3.connect(DB_PATH) as conn:
        conn.row_factory = sqlite3.Row
        row = conn.execute(
            "SELECT * FROM copy_files WHERE brief_id = ? AND file_type = 'delivery' "
            "ORDER BY uploaded_at DESC LIMIT 1",
            (brief_id,),
        ).fetchone()
        return _row_to_dict(row)


def get_reference_files(brief_id: int) -> list[dict]:
    """Return all reference files uploaded by the client for a brief."""
    with sqlite3.connect(DB_PATH) as conn:
        conn.row_factory = sqlite3.Row
        rows = conn.execute(
            "SELECT * FROM copy_files WHERE brief_id = ? AND file_type = 'reference' "
            "ORDER BY uploaded_at ASC",
            (brief_id,),
        ).fetchall()
        return [dict(r) for r in rows]


# ── drafts ────────────────────────────────────────────────────────────────────

def save_draft(brief_id: int, draft: str) -> None:
    """Persist an auto-generated draft against a brief."""
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute(
            "UPDATE briefs SET draft = ? WHERE id = ?", (draft, brief_id)
        )


# ── admin dashboard stats ─────────────────────────────────────────────────────

def get_dashboard_stats() -> dict:
    """
    Returns:
      total_clients       — count of client accounts
      briefs_this_month   — briefs submitted in the current calendar month
      avg_turnaround_days — mean days from created_at → completed_at
                            (completed briefs only; None if no data)
    """
    with sqlite3.connect(DB_PATH) as conn:
        total_clients = conn.execute(
            "SELECT COUNT(*) FROM portal_users WHERE role = 'client'"
        ).fetchone()[0]

        briefs_this_month = conn.execute(
            """
            SELECT COUNT(*) FROM briefs
            WHERE strftime('%Y-%m', created_at) = strftime('%Y-%m', 'now')
            """
        ).fetchone()[0]

        avg_row = conn.execute(
            """
            SELECT AVG(JULIANDAY(completed_at) - JULIANDAY(created_at))
            FROM   briefs
            WHERE  status = 'completed' AND completed_at IS NOT NULL
            """
        ).fetchone()
        raw_avg = avg_row[0]
        avg_turnaround_days = round(raw_avg, 1) if raw_avg is not None else None

    return {
        "total_clients": total_clients,
        "briefs_this_month": briefs_this_month,
        "avg_turnaround_days": avg_turnaround_days,
    }
