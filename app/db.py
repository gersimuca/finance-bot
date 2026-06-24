import sqlite3
import os

os.makedirs("data", exist_ok=True)

DB_PATH = "data/data.db"

conn = sqlite3.connect(DB_PATH)

conn.execute("""
CREATE TABLE IF NOT EXISTS transactions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT,
    merchant TEXT,
    amount REAL,
    category TEXT,
    source TEXT UNIQUE
)
""")

def insert(tx):
    try:
        conn.execute("""
        INSERT INTO transactions(date, merchant, amount, category, source)
        VALUES (?, ?, ?, ?, ?)
        """, tx)
        conn.commit()
    except:
        pass