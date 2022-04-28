import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


from Music.config import (
    BOT_PHOTO,
    ALIVE_NAME,
    BOT_NAME,
    BOT_USERNAME,
    OWNER_NAME,
    SUDO_USERS,
    BOT_TOKEN,
    DEV_PHOTO,
    DEV_NAME,
)
@app.on_message(
    command(["ايدي"])
    & filters.group
    & ~filters.edited
)
async def khalid(client: Client, message: Message):
    usr = await client.get_users(message.from_user.id)
    name = usr.first_name
    async for photo in client.iter_profile_photos(message.from_user.id, limit=1):
                    await message.reply_photo(photo.file_id,       caption=f"""◂ اسمك ↫ {message.from_user.mention}\n\n◂ معرفك ↫ @{message.from_user.username}\n\n◂ ايديك ↫ {message.from_user.id}\n\n◂ ايدي الجروب ↫ {message.chat.id}""", 
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        ),
    )
 
