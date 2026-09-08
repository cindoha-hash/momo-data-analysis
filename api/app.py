"""
Minimal FastAPI app exposing /transactions and /analytics
Optional bonus - to be implemented in Phase 4.
"""
from fastapi import FastAPI
from api.db import get_connection

app = FastAPI(title="MoMo SMS Analytics API")


@app.get("/")
def root():
    return {"message": "MoMo SMS Analytics API is running"}


@app.get("/transactions")
def get_transactions():
    conn = get_connection()
    rows = conn.execute("SELECT * FROM transactions").fetchall()
    conn.close()
    return [dict(row) for row in rows]


@app.get("/analytics")
def get_analytics():
    conn = get_connection()
    total = conn.execute("SELECT COUNT(*) as count FROM transactions").fetchone()
    conn.close()
    return {"total_transactions": total["count"] if total else 0}
