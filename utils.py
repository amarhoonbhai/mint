# ad_bot/utils.py
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from ad_bot.config import BOT_USERNAME, FORCE_CHANNEL, FORCE_GROUP

def dashboard_buttons():
    buttons = [
        [InlineKeyboardButton("Add Accounts", callback_data="add_accounts"),
         InlineKeyboardButton("My Accounts", callback_data="my_accounts")],
        [InlineKeyboardButton("Set Ad Message", callback_data="set_ad")],
        [InlineKeyboardButton("Set Time Intervals", callback_data="set_time"),
         InlineKeyboardButton("Start/Stop Ad", callback_data="ad_control")],
        [InlineKeyboardButton("Add Groups", callback_data="add_groups")],
        [InlineKeyboardButton("Premium", callback_data="premium"),
         InlineKeyboardButton("Support", url="https://t.me/NeoHarsh")]
    ]
    return InlineKeyboardMarkup(buttons)

def otp_keypad(current=""):
    buttons = [
        [InlineKeyboardButton("1", callback_data="otp_1"), InlineKeyboardButton("2", callback_data="otp_2")],
        [InlineKeyboardButton("3", callback_data="otp_3"), InlineKeyboardButton("4", callback_data="otp_4")],
        [InlineKeyboardButton("5", callback_data="otp_5"), InlineKeyboardButton("6", callback_data="otp_6")],
        [InlineKeyboardButton("7", callback_data="otp_7"), InlineKeyboardButton("8", callback_data="otp_8")],
        [InlineKeyboardButton("9", callback_data="otp_9"), InlineKeyboardButton("0", callback_data="otp_0")],
        [InlineKeyboardButton("🔙 Back", callback_data="otp_back"), InlineKeyboardButton("✅ OK", callback_data="otp_ok")]
    ]
    caption = f"📝 Enter the OTP code:\n\n`{current}`\n\nUse the keypad below:"
    return InlineKeyboardMarkup(buttons), caption
  
