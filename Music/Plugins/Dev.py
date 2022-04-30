import asyncio
from pyrogram import Client, filters
from Music.MusicUtilities.helpers.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


@app.on_message(
    command(["عمار"])
    & filters.group
    & ~filters.edited
)
async def khalid(client: Client, message: Message):
    usr = await client.get_users(5268261948)
    name = usr.first_name
    async for photo in client.iter_profile_photos(5268261948, limit=1):
                    await message.reply_photo(photo.file_id,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/X_A_R3"),
                ],[
                    InlineKeyboardButton(
                        "- sᴏᴜʀᴄᴇ ᴀᴄᴇ .", callback_data=f"fft"),
                ],
            ]
        ),
    )
