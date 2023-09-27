import sqlite3


con = sqlite3.connect("sql.db")
cur = con.cursor()

query = """CREATE TABLE IF NOT EXISTS logs (
    raw_log TEXT NOT NULL UNIQUE,
    remote_addr TEXT,
    time_local TEXT,
    request_type TEXT,
    request_path TEXT,
    status INTEGER,
    body_bytes_sent INTEGER,
    http_referer TEXT,
    http_user_agent TEXT,
    created DATETIME DEFAULT CURRENT_TIMESTAMP
    )"""

cur.execute(query)
con.commit()
