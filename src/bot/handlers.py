from telegram import Update
from telegram.ext import ContextTypes
from .keyboards import get_network_keyboard, get_monitoring_keyboard, get_settings_keyboard

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Welcome to the Node Monitoring Bot! Use /register to set up your nodes."
    )

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
