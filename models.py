import sqlite3

def init_db():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS entries (
            id INTEGER PRIMARY KEY,
            situation TEXT NOT NULL,
            worry TEXT NOT NULL,
            anxiety_level INTEGER NOT NULL CHECK(anxiety_level BETWEEN 0 AND 10),
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

def insert_entry(situation, worry, anxiety_level):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('INSERT INTO entries (situation, worry, anxiety_level) VALUES (?, ?, ?)',
              (situation, worry, anxiety_level))
    conn.commit()
    conn.close()

def get_entries():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('SELECT situation, worry, anxiety_level, created_at FROM entries ORDER BY created_at DESC')
    entries = c.fetchall()
    conn.close()
    return entries
