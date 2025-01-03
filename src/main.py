from telegram.ext import Application, CommandHandler, CallbackQueryHandler
from bot.handlers import *

def main():
    application = Application.builder().token(BOT_TOKEN).build()
    
    # Add command handlers
    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(CommandHandler("register", register_command))
    application.add_handler(CommandHandler("monitor", monitor_command))
    application.add_handler(CommandHandler("settings", settings_command))
    application.add_handler(CommandHandler("status", status_command))
    
    # Add button handlers
    application.add_handler(CallbackQueryHandler(network_button_handler, pattern="^network_"))
    application.add_handler(CallbackQueryHandler(monitor_action_handler, pattern="^monitor_"))
    
    application.run_polling()

if __name__ == "__main__":
    main()
