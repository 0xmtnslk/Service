import telebot
import yaml
from database import Database

# Initialize bot and database
bot = telebot.TeleBot("YOUR_BOT_TOKEN")
db = Database()

@bot.message_handler(commands=['start'])
def start(message):
    db.add_user(message.from_user.id)
    bot.reply_to(message, "Welcome! Use /register <validator_address> to add your validator.")

@bot.message_handler(commands=['register'])
def register_validator(message):
    try:
        _, address = message.text.split()
        db.add_validator(message.from_user.id, address)
        bot.reply_to(message, f"Validator {address} registered successfully!")
    except:
        bot.reply_to(message, "Usage: /register <validator_address>")

@bot.message_handler(commands=['networks'])
def list_networks(message):
    with open('networks/config.yaml') as f:
        networks = yaml.safe_load(f)
    response = "Available networks:\n"
    for network in networks:
        response += f"- {networks[network]['name']} ({networks[network]['chain_id']})\n"
    bot.reply_to(message, response)

if __name__ == '__main__':
    bot.polling()
