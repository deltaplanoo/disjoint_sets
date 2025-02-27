import sqlite3
import time

# Database file name
DATABASE_FILE = "benchmark_results.db"

# Create the database and table (if they don't exist)
def create_database():
    with sqlite3.connect(DATABASE_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS results (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
				method TEXT,
                n INTEGER,
                m INTEGER,
                time REAL
            )
        """)
        conn.commit()

# Insert a record into the database
def insert_result(method, n, m, time):
    with sqlite3.connect(DATABASE_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO results (method, n, m, time)
            VALUES (?, ?, ?, ?)
        """, (method, n, m, time))
        conn.commit()

# Query and display all results
def display_results():
    with sqlite3.connect(DATABASE_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM results")
        rows = cursor.fetchall()
        for row in rows:
            print(row)

