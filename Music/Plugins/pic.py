import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButto  

@app.on_message(
    command(["صوري"])
    & filters.group
    & ~filters.edited
)
async ah Khalid(client: Client, message: Message):
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

