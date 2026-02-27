"""SQLite helpers for Copywrite."""

import os
import sqlite3

DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "copywrite.db")


def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("""
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
            )
        """)


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
