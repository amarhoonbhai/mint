# ad_bot/handlers/start.py
from pyrogram import filters
from ad_bot.main import bot
from ad_bot.utils import dashboard_buttons
from ad_bot.state import *
from ad_bot.config import FORCE_CHANNEL, FORCE_GROUP

async def check_membership(user_id):
    try:
        ch = await bot.get_chat_member(FORCE_CHANNEL, user_id)
        gr = await bot.get_chat_member(FORCE_GROUP, user_id)
        return ch.status not in ["left", "kicked"] and gr.status not in ["left", "kicked"]
    except:
        return False

@bot.on_message(filters.command("start"))
async def start(_, message):
    user_id = message.from_user.id
    if not await check_membership(user_id):
        await message.reply(f"Please join {FORCE_CHANNEL} and {FORCE_GROUP} to use the bot.")
        return

    await bot.send_photo(
        chat_id=user_id,
        photo="https://i.postimg.cc/qv7fcQXb/a-logo-design-featuring-the-text-lord-ad-0sfrm-JKJTea-DLQfz82-X-Q-Sd-Clrr-URTS22-Yyz6rn-8-g.jpg",
        caption="✅ Welcome to Ad Bot Dashboard!\nChoose an option below:",
        reply_markup=dashboard_buttons()
    )
  
