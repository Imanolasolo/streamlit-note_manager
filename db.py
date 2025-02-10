import sqlite3
from passlib.hash import bcrypt
import os

def init_db():
    conn = sqlite3.connect("notes.db")
    c = conn.cursor()
    
    # Create Users Table
    c.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password_hash TEXT NOT NULL
    )
    """)
    
    # Create Notes Table
    c.execute("""
    CREATE TABLE IF NOT EXISTS notes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        title TEXT NOT NULL,
        content TEXT NOT NULL,
        FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
    )
    """)
    
    conn.commit()
    conn.close()
    print("Database initialized successfully!")

def register_user(username, password):
    init_db()  # Ensure the database is initialized before inserting a user
    conn = sqlite3.connect("notes.db")
    c = conn.cursor()
    
    c.execute("SELECT * FROM users WHERE username = ?", (username,))
    if c.fetchone():
        return False  # User already exists
    
    hashed_password = bcrypt.hash(password)
    c.execute("INSERT INTO users (username, password_hash) VALUES (?, ?)", (username, hashed_password))
    
    conn.commit()
    conn.close()
    return True

def get_user(username):
    init_db()  # Ensure the database is initialized before querying a user
    conn = sqlite3.connect("notes.db")
    c = conn.cursor()
    c.execute("SELECT id, username, password_hash FROM users WHERE username = ?", (username,))
    user = c.fetchone()
    conn.close()
    return user

def create_note(user_id, title, content):
    conn = sqlite3.connect("notes.db")
    c = conn.cursor()
    c.execute("INSERT INTO notes (user_id, title, content) VALUES (?, ?, ?)", (user_id, title, content))
    conn.commit()
    conn.close()

def get_notes(user_id):
    conn = sqlite3.connect("notes.db")
    c = conn.cursor()
    c.execute("SELECT id, title, content FROM notes WHERE user_id = ?", (user_id,))
    notes = c.fetchall()
    conn.close()
    return notes

def update_note(note_id, title, content):
    conn = sqlite3.connect("notes.db")
    c = conn.cursor()
    c.execute("UPDATE notes SET title = ?, content = ? WHERE id = ?", (title, content, note_id))
    conn.commit()
    conn.close()

def delete_note(note_id):
    conn = sqlite3.connect("notes.db")
    c = conn.cursor()
    c.execute("DELETE FROM notes WHERE id = ?", (note_id,))
    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()