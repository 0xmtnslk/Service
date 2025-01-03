from cryptography.fernet import Fernet
from src.utils.config import DATABASE_ENCRYPTION_KEY

class Database:
    def __init__(self):
        self.fernet = Fernet(DATABASE_ENCRYPTION_KEY)
        
    def init_tables(self):
        self.execute("""
            CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY,
                is_admin BOOLEAN,
                alert_preferences TEXT
            )
        """)
        
        self.execute("""
            CREATE TABLE IF NOT EXISTS validators (
                id INTEGER PRIMARY KEY,
                chain_id TEXT,
                valoper_address TEXT,
                user_id INTEGER,
                FOREIGN KEY (user_id) REFERENCES users (user_id)
            )
        """)

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
