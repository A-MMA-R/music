# كل سنة ونت طيب يخويا  . 
# كود ايدي بـ صورة الشخص وزرار يدخل ع شات الشخص و بيجيب يوزر و ايدي و اسم و ايدي الجروب لـ الشخص  . 


# اتأكد من تنصيب المكآتب . 
import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

# الكود اهو يصحبي  . 

@app.on_message(
    command(["ايدي"])
    & filters.group
    & ~filters.edited
)
async ah madison(client: Client, message: Message):
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

# بس كدا يقلبي الكود هيشتغل معاك  . 
# لو معرفتش تشغلو كلمني هنا  . 
# يوزري : @MaDyY_y
# قناة السورس : @so_alfaa
# دعم السورس : @LURA205

# بس كدا جرب و آدعيلي وخش القناة عشان تشوف باقي الاكواد ♥. 