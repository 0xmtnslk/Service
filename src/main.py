import os
import logging
from dotenv import load_dotenv
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler
from bot.handlers import start_handler, status_handler, settings_handler, button_handler
from monitoring.node_status import NodeStatusMonitor
from utils.database import Database

load_dotenv()

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

def main():
    token = os.getenv('BOT_TOKEN')
    app = ApplicationBuilder().token(token).build()
    
    # Initialize components
    db = Database()
    monitor = NodeStatusMonitor()
    
    # Add handlers
    app.add_handler(CommandHandler("start", start_handler))
    app.add_handler(CommandHandler("status", status_handler))
    app.add_handler(CommandHandler("settings", settings_handler))
    app.add_handler(CallbackQueryHandler(button_handler))
    
    app.run_polling()

if __name__ == "__main__":
    main()
