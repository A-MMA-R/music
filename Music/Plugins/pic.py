import asyncio
from pyrogram import Client, filters

from Music.config import GROUP, CHANNEL
from Music import (
    ASSID,
    BOT_ID,
    BOT_NAME,
    BOT_USERNAME,
    OWNER,
    SUDOERS,
    app,
)

from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
)

DEV_BOT = getenv("DEV_BOT")
BOTID = getenv("BOTID")
DEVID = getenv("DEVID")
DEV_BOT1 = getenv("DEV_BOT1")
NAME_BOT = getenv("NAME_BOT")

def get_file_id(msg: Message):
    if msg.media:
        for message_type in (
            "photo",
            "animation",
            "audio",
            "document",
            "video",
            "video_note",
            "voice",
            # "contact",
            # "dice",
            # "poll",
            # "location",
            # "venue",
            "sticker",
        ):
            obj = getattr(msg, message_type)
            if obj:
                setattr(obj, "message_type", message_type)
                return obj


@app.on_message(command(["/pics"]) & filters.group)
async def Khalid(client: Client, message: Message):
    usr = await client.get_users(message.from_user.id)
    name = usr.first_name
    async for photo in client.iter_profile_photos(message.from_user.id, limit=1):
                    await message.reply_photo(photo.file_id,       caption=f"""نفس ألصوره كل مرة غير بق""", 
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{message.from_user.username}")
                ],[
                    InlineKeyboardButton(
                        "╞. 𝒅𝒆𝒗 .╡", url=f"https://t.me/X_A_R3"),
                ],
            ]
        ),
    )

