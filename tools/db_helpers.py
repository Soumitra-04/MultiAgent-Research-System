import sqlite3
import json
import uuid
from datetime import datetime

DB_PATH = "Database/research_system.db"

def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA journal_mode=WAL;")
    conn.execute("PRAGMA foreign_keys = ON;")
    conn.row_factory = sqlite3.Row
    return conn

def generate_id():
    return str(uuid.uuid4())

def encode_flags(flags: list) -> str:
    return json.dumps(flags)

def decode_flags(flags_text: str) -> list:
    if not flags_text:
        return []
    return json.loads(flags_text)

def validate_date(date_str: str) -> bool:
    if not date_str:
        return True
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def update_verification_status(claim_id: str, status: str):
    valid = {"unverified", "verified", "disputed", "rejected"}
    if status not in valid:
        raise ValueError(f"Invalid status: {status}")
    conn = get_connection()
    conn.execute(
        "UPDATE claims SET verification_status = ? WHERE claim_id = ?",
        (status, claim_id)
    )
    conn.commit()
    conn.close()