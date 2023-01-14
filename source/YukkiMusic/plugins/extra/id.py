import asyncio
from pyrogram import Client, filters
from strings import get_command
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from YukkiMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from typing import Union
from pyrogram.types import InlineKeyboardButton
import re
import sys
from config import BANNED_USERS, MUSIC_BOT_NAME
from pyrogram import filters
from YukkiMusic.utils.decorators import AdminRightsCheck
import config
from YukkiMusic.utils.database import (add_served_chat,
                                       add_served_user,
                                       blacklisted_chats,
                                       get_assistant, get_lang,
                                       get_userss, is_on_off,
                                       is_served_private_chat)

@app.on_message(
    command(["ا","ايدي"])
    & filters.group
    & ~filters.edited
)
async def id(client: Client, message: Message):
      usr = await client.get_users(message.from_user.id)
      name = usr.first_name
      async for photo in client.iter_profile_photos(message.from_user.id, limit=1):
                    await message.reply_photo(photo.file_id,       caption=f"""**• اسمك =>** {message.from_user.mention}\n\n**• معرفك =>** @{message.from_user.username}\n\n**• ايديك =>** `{message.from_user.id}`\n\n**• ايدي الجروب =>** `{message.chat.id}`""", 
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        ),
    )
