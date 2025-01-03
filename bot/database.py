import sqlite3

class Database:
    def __init__(self):
        self.conn = sqlite3.connect('bot.db')
        self.create_tables()
        
    def create_tables(self):
        cursor = self.conn.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY
        )''')
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS validators (
            user_id INTEGER,
            address TEXT,
            FOREIGN KEY (user_id) REFERENCES users(user_id)
        )''')
        self.conn.commit()
        
    def add_user(self, user_id):
        cursor = self.conn.cursor()
        cursor.execute('INSERT OR IGNORE INTO users VALUES (?)', (user_id,))
        self.conn.commit()
        
    def add_validator(self, user_id, address):
        cursor = self.conn.cursor()
        cursor.execute('INSERT INTO validators VALUES (?, ?)', (user_id, address))
        self.conn.commit()
