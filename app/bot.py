import os
import yaml
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from tenderduty_config import generate_config

def start(update: Update, context: CallbackContext):
    keyboard = []
    with open("networks.yaml") as f:
        networks = yaml.safe_load(f)["networks"]
        for network_id, network in networks.items():
            keyboard.append([InlineKeyboardButton(network["name"], callback_data=f"network_{network_id}")])
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text("Please select a network:", reply_markup=reply_markup)

def main():
    token = os.environ["TELEGRAM_BOT_TOKEN"]
    updater = Updater(token)
    dispatcher = updater.dispatcher
    
    dispatcher.add_handler(CommandHandler("start", start))
    
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
