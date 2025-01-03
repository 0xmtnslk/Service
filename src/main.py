from telegram.ext import Application, CommandHandler
from bot.handlers import start, register, monitor, settings, status
from dotenv import load_dotenv
import os

load_dotenv()

def main():
    app = Application.builder().token(os.getenv('BOT_TOKEN')).build()
    
    app.add_handler(CommandHandler('start', start))
    app.add_handler(CommandHandler('register', register))
    app.add_handler(CommandHandler('monitor', monitor))
    app.add_handler(CommandHandler('settings', settings))
    app.add_handler(CommandHandler('status', status))
    
    app.run_polling()

if __name__ == '__main__':
    main()
