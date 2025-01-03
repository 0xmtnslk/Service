from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def get_network_keyboard():
    keyboard = [
        [InlineKeyboardButton("Nibiru", callback_data='network_nibiru'),
         InlineKeyboardButton("Zetachain", callback_data='network_zetachain')],
        [InlineKeyboardButton("Dymension", callback_data='network_dymension'),
         InlineKeyboardButton("BlockX", callback_data='network_blockx')],
        [InlineKeyboardButton("Mantrachain", callback_data='network_mantrachain'),
         InlineKeyboardButton("Kopi", callback_data='network_kopi')],
        [InlineKeyboardButton("Lava", callback_data='network_lava')]
    ]
    return InlineKeyboardMarkup(keyboard)

def get_monitoring_keyboard():
    keyboard = [
        [InlineKeyboardButton("Node Status", callback_data='monitor_status')],
        [InlineKeyboardButton("Sync Status", callback_data='monitor_sync')],
        [InlineKeyboardButton("Validator Info", callback_data='monitor_validator')]
    ]
    return InlineKeyboardMarkup(keyboard)

def get_settings_keyboard():
    keyboard = [
        [InlineKeyboardButton("Alert Thresholds", callback_data='settings_alerts')],
        [InlineKeyboardButton("Monitoring Interval", callback_data='settings_interval')],
        [InlineKeyboardButton("Notification Settings", callback_data='settings_notifications')]
    ]
    return InlineKeyboardMarkup(keyboard)
