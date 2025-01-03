from src.utils.rate_limiter import RateLimiter
from src.utils.config import ADMIN_USER_IDS
from telegram.ext import CommandHandler

rate_limiter = RateLimiter()

async def start_handler(update, context):
    if not rate_limiter.is_allowed(update.effective_user.id):
        return await update.message.reply_text("Rate limit exceeded. Please try again later.")
    
    # Rest of the handler code

async def add_validator_handler(update, context):
    if update.effective_user.id not in ADMIN_USER_IDS:
        return await update.message.reply_text("This command is only available to admins.")
    
    # Rest of the handler code

def register_handlers(dispatcher):
    dispatcher.add_handler(CommandHandler("start", start_command))
    dispatcher.add_handler(CommandHandler("register", register_command))
    dispatcher.add_handler(CommandHandler("monitor", monitor_command))
    dispatcher.add_handler(CommandHandler("settings", settings_command))

# Implement command handlers
