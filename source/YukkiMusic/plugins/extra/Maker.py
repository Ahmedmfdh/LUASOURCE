import asyncio
from pyrogram import Client, filters
from strings import get_command
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from YukkiMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)


@app.on_message(
    command(["مصنع","المصنع"])
    & filters.group
    & ~filters.edited
)
async def maker(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/9ac90b6bfcaa826534453.jpg",
        caption=f"""• | مصانع سورس سكران للتنصيب""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "مصنع الميوزك", url=f"https://t.me/@fvjdvedibot"),
                    InlineKeyboardButton(
                        "مصنع الحمايه ♡", url=f"https://t.me/med_O_Ubot"),
                ],
                [
                   InlineKeyboardButton(
                        "𝚃𝙸𝙶𝙴𝚁 ", url=f"https://t.me/H_a_g_a_r_M_U_S_I_C_C_bot"),
                ],       
            ]
        ),
    )