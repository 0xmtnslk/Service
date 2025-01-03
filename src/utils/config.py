import os
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
ADMIN_USER_IDS = [int(id) for id in os.getenv('ADMIN_USER_IDS').split(',')]
DATABASE_ENCRYPTION_KEY = os.getenv('DATABASE_ENCRYPTION_KEY')
TENDERDUTY_METRICS_URL = os.getenv('TENDERDUTY_METRICS_URL')
