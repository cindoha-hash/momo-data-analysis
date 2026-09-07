"""
Creates tables and loads transactions into SQLite.
Implementation to be completed in Phase 3 (Database).
"""
import sqlite3
from etl.config import DATABASE_PATH


def get_connection():
    return sqlite3.connect(DATABASE_PATH)


def create_tables():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            amount REAL,
            date TEXT,
            phone TEXT,
            category TEXT,
            raw_message TEXT
        )
    """)
    conn.commit()
    conn.close()


def load_transactions(transactions: list):
    conn = get_connection()
    cursor = conn.cursor()
    for txn in transactions:
        cursor.execute(
            "INSERT INTO transactions (amount, date, phone, category, raw_message) VALUES (?, ?, ?, ?, ?)",
            (
                txn.get("amount"),
                txn.get("date"),
                txn.get("phone"),
                txn.get("category"),
                txn.get("message"),
            ),
        )
    conn.commit()
    conn.close()
