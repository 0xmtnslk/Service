from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes
import yaml
import os

with open("app/networks.yaml") as f:
    NETWORKS = yaml.safe_load(f)["networks"]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = []
    for net_id, net_data in NETWORKS.items():
        keyboard.append([InlineKeyboardButton(
            net_data["name"], 
            callback_data=f"network_{net_id}"
        )])

    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "Welcome! Please select a network:",
        reply_markup=reply_markup
    )

async def network_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    network = query.data.split("_")[1]
    context.user_data["selected_network"] = network
    await query.message.reply_text(
        f"Selected network: {NETWORKS[network]['name']}\n"
        "Please enter your validator address (valoper...):"
    )

def main():
    app = ApplicationBuilder().token(os.getenv("TELEGRAM_BOT_TOKEN")).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(network_callback, pattern="^network_"))
    app.run_polling()

if __name__ == "__main__":
    main()
