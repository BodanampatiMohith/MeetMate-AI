import sqlite3, os

def init_db():
    conn = sqlite3.connect("minutes.db")
    conn.execute("""
        CREATE TABLE IF NOT EXISTS action_items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            meeting_id TEXT, task TEXT,
            owner TEXT, deadline TEXT )
    """)
    conn.commit()
    return conn
