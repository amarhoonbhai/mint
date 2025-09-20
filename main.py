# ad_bot/main.py
from pyrogram import Client
from ad_bot.config import BOT_TOKEN, API_ID, API_HASH

bot = Client("ad_bot", bot_token=BOT_TOKEN, api_id=API_ID, api_hash=API_HASH)

# Register handlers
from ad_bot.handlers import start, account, dashboard, text_input, ad_control, admin

if __name__ == "__main__":
    bot.run()
  
