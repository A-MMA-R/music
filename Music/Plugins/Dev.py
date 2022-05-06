import asyncio
import yt_dlp
import psutil

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
from pyrogram.types import CallbackQuery
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from Music.MusicUtilities.helpers.filters import command
from pyrogram import Client, filters
import re
import sys
from os import getenv
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
)


@Client.on_message(
    command(["source", f"source@{BOT_USERNAME}","سورس","السورس"]) & filters.group & ~filters.edited
)
async def ssoyrce(client: Client, message: Message):

    keyboard = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Sᴏᴜʀᴄᴇ ᴀᴄᴇ", url=f"https://t.me/V_III_B"),
                ],[
                    InlineKeyboardButton(
                        "ᴅᴇᴠᴇʟᴏᴘᴇʀ", callback_data="𝒂𝒎𝒎𝒂𝒓")
                ],[
                    InlineKeyboardButton(
                        "sᴜᴘᴘɪʀᴛ", url=f"https://t.me/XL_support"),
                ],
            ]
        )

    source = f"""**[𝒘𝒆𝒍𝒄𝒐𝒎𝒆 𝒕𝒐 𝒔𝒐𝒖𝒓𝒄𝒆 𝒂𝒄𝒆](https://t.me/V_III_B)\n\n [𝒃𝒆𝒔𝐭 𝒔𝒐𝒖𝒓𝒄𝒆 𝒊𝒏 𝒕𝒆𝒍𝒆](https://t.me/V_III_B)**""" 
    await message.reply_photo(
        photo=f"{SOURCE}",
        caption=source,
        reply_markup=keyboard,
    )



@Client.on_callback_query(filters.regex("source"))
async def source(_, query: CallbackQuery):
   await query.edit_message_text(
       f"""**[𝒘𝒆𝒍𝒄𝒐𝒎𝒆 𝒕𝒐 𝒔𝒐𝒖𝒓𝒄𝒆 𝒂𝒄𝒆](https://t.me/V_III_B)\n\n [𝒃𝒆𝒔𝐭 𝒔𝒐𝒖𝒓𝒄𝒆 𝒊𝒏 𝒕𝒆𝒍𝒆](https://t.me/V_III_B)**""",
       reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "SOURCE GHOST", url=f"https://t.me/V_III_B"),
                ],[
                    InlineKeyboardButton(
                        "DEVELOPERS", callback_data="𝒂𝒎𝒎𝒂𝒓")
                ],[
                    InlineKeyboardButton(
                        "GROUP_SUPPORT", url=f"https://t.me/XL_support"), 
                ],
            ]
        ),
    )



@Client.on_message(
    command(["developer", f"developer@{BOT_USERNAME}", "مطور" ,"المطور"]) & filters.group & ~filters.edited
)
async def developer(client: Client, message: Message):

    usr = await client.get_users(5268261948)

    name = usr.first_name

    async for photo in client.iter_profile_photos(5268261948, limit=1):

                    await message.reply_photo(photo.file_id,       

        reply_markup=InlineKeyboardMarkup(

            [

                [

                    InlineKeyboardButton(

                        name, url=f"https://t.me/{OWNER_NAME}") 

                ],[

                    InlineKeyboardButton(

                        "اضف البوت الي مجموعتك", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"),

                ],

            ]

        ),

    )




    
@Client.on_message(
    command(["bot", f"bot@{BOT_USERNAME}", "بوت","البوت"]) & filters.group & ~filters.edited
)
async def gbot(client: Client, message: Message):

    usr = await client.get_users(5268261948)

    name = usr.first_name

    async for photo in client.iter_profile_photos(ID_BOT, limit=1):

                    await message.reply_photo(photo.file_id,       caption=f"اسمي [{me_bot.first_name}](https://t.me/{BOT_USERNAME}) يروحي🙈💕", 

        reply_markup=InlineKeyboardMarkup(

            [

                [

                    InlineKeyboardButton(

                        name, url=f"https://t.me/{OWNER_NAME}") 

                ],[

                    InlineKeyboardButton(

                        "اضف البوت الي مجموعتك", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"),

                ],

            ]

        ),

    )
