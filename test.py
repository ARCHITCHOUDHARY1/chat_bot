import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()
conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="ARCHit@18",  # <-- Use the correct password
    host="localhost",
    port=5432
)
print("Connected successfully")