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

    def add_user(self, user_id, username):
        # Add user to database
        pass
    
    def get_user(self, user_id):
        # Get user info
        pass
        
    def add_validator(self, user_id, network, address):
        # Add validator for user
        pass
    
    def get_user_validators(self, user_id):
        # Get user's validators
        pass
    
    def set_alert(self, user_id, alert_type, threshold):
        # Set alert preferences
        pass
    
    def get_alerts(self, user_id):
        # Get user's alert settings
        pass
