import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

def get_conn():
    return psycopg2.connect(
        dbname=os.getenv("POSTGRES_DB"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD"),
        host=os.getenv("POSTGRES_HOST"),
        port=os.getenv("POSTGRES_PORT"),
    )

def init_db():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS chat_history (
            id SERIAL PRIMARY KEY,
            role VARCHAR(10),
            message TEXT
        )
    """)
    conn.commit()
    cur.close()
    conn.close()

def store_chat(role, message):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("INSERT INTO chat_history (role, message) VALUES (%s, %s)", (role, message))
    conn.commit()
    cur.close()
    conn.close()

def fetch_chat_history():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT id, role, message FROM chat_history ORDER BY id")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows

def clear_chat_history():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("DELETE FROM chat_history")
    conn.commit()
    cur.close()
    conn.close()

# Initialize table on import
init_db()