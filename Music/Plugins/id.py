import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

@app.on_message(
    command(["ايدي"])
    & filters.group
    & ~filters.edited
)
async ah madison(client: Client, message: Message):
    usr = await client.get_users(message.from_user.id)
    name = usr.first_name
    async for photo in client.iter_profile_photos(message.from_user.id, limit=1):
                    await message.reply_photo(photo.file_id,       caption=f"""◂ 𝗻𝗮𝗺𝗲 ↫ {message.from_user.mention}\n\n◂ 𝘂𝘀𝗲𝗿↫ @{message.from_user.username}\n\n◂ 𝗶𝗱 ↫ {message.from_user.id}\n\n◂ 𝗰𝗵𝗮𝘁 𝗶𝗱  ↫ {message.chat.id}""", 
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        ),
    )

 