import sqlite3

class Database:
    def __init__(self, db_path="data/monitor.db"):
        self.conn = sqlite3.connect(db_path)
        self.create_tables()
    
    def create_tables(self):
        self.conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            username TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )""")
        
        self.conn.execute("""
        CREATE TABLE IF NOT EXISTS validators (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            network TEXT,
            valoper_address TEXT,
            FOREIGN KEY (user_id) REFERENCES users(user_id)
        )""")
        
        self.conn.execute("""
        CREATE TABLE IF NOT EXISTS alerts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            validator_id INTEGER,
            alert_type TEXT,
            threshold INTEGER,
            FOREIGN KEY (validator_id) REFERENCES validators(id)
        )""")
        self.conn.commit()
