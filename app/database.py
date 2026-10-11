import sqlite3
from config import Configs

def connectDatabase():
    conn = sqlite3.connect(Configs.DATABASE_URL)
    conn.row_factory = sqlite3.Row
    return conn

def createDatabase():
    conn = connectDatabase()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS customers (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            name        VARCHAR NOT NULL,
            email       VARCHAR,
            phoneNumber TEXT,
            text        VARCHAR,
            createdAt   TEXT DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()

def addNewCustomer(name, email, phone, message):
    conn = connectDatabase()
    try:
        cur = conn.execute(
            "INSERT INTO customers (name, email, phoneNumber, text) VALUES (?, ?, ?, ?)",
            (name, email, phone, message),
        )
        conn.commit()
        return cur.lastrowid
    finally:
        conn.close()

def getAllCustomers():
    conn = connectDatabase()
    try:
        rows = conn.execute("SELECT * FROM customers ORDER BY createdAt DESC").fetchall()
        return [dict(row) for row in rows]
    finally:
        conn.close()
