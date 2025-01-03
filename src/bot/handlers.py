from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from utils.database import Database

db = Database()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    db.conn.execute("INSERT OR IGNORE INTO users (user_id) VALUES (?)", (user_id,))
    db.conn.commit()
    
    keyboard = [
        [InlineKeyboardButton("Register Validator", callback_data="register_validator")],
        [InlineKeyboardButton("View Validators", callback_data="view_validators")],
        [InlineKeyboardButton("Alert Settings", callback_data="alert_settings")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Welcome to Validator Monitor Bot!", reply_markup=reply_markup)

async def register(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = get_network_keyboard()
    await update.message.reply_text(
        "Select a network to register:", 
        reply_markup=keyboard
    )

async def monitor(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = get_monitoring_keyboard()
    await update.message.reply_text(
        "Select monitoring options:",
        reply_markup=keyboard
    )

async def settings(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = get_settings_keyboard()
    await update.message.reply_text(
        "Bot Settings:",
        reply_markup=keyboard
    )

async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Fetching node status..."
    )
