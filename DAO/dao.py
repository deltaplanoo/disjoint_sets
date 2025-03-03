import sqlite3
import time
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
DATABASE_FILE = os.path.join(current_dir, "benchmark_results.db")

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

def remove_by_method(method_value):
    """
    Removes tuples from the 'results' table where the 'method' field matches the given value.

    Args:
        method_value: The string value of the 'method' field to filter by.
    """
    try:
        with sqlite3.connect(DATABASE_FILE) as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM results WHERE method = ?", (method_value,))
            conn.commit()
            print(f"Removed tuples with method = '{method_value}'.")
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")

def remove_by_id(id_value):
    try:
        with sqlite3.connect(DATABASE_FILE) as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM results WHERE id = ?", (id_value,))
            conn.commit()
            print(f"Removed tuples with id = '{id_value}'.")
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")


# Query and display all results
def display_results():
    with sqlite3.connect(DATABASE_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM results")
        rows = cursor.fetchall()
        for row in rows:
            print(row)

