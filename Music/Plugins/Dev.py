import asyncio
from pyrogram import Client, filters
from strings import get_command
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


@app.on_message(
    command(["المبرمج"])
    & filters.group
    & ~filters.edited
)
async def khalid(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/7354b21c97883acb00bd9.jpg",
        caption=f""" - ᴅᴇᴠ : ᴀᴍᴍᴀʀ .""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        " - َA𝑚𝑚َ𝑎𝑟 , ُ𝑚𝑜ℎ𝑎𝑚ِ𝑒𝑑 .", url=f"https://t.me/X_A_R3"),
                ],[
                    InlineKeyboardButton(
                        "- sᴏᴜʀᴄᴇ .", callback_data=f"fft"),
                ],
            ]
        ),
    )
