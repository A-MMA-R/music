import os
from os import path
from typing import Callable
from asyncio import QueueEmpty

import aiofiles
import aiohttp
import ffmpeg
import requests
import wget
from os import path
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

from pyrogram import Client 
from pyrogram import filters
from pyrogram.errors import UserAlreadyParticipant
from pyrogram.types import Voice
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from pyrogram import Client, filters
from youtube_search import YoutubeSearch

from Music.MusicUtilities.helpers.decorators import authorized_users_only
from Music.MusicUtilities.database.chats import is_served_chat
from Music.MusicUtilities.database.queue import remove_active_chat
from Music.MusicUtilities.database.sudo import get_sudoers
from Music.MusicUtilities.helpers.filters import command
from youtube_search import YoutubeSearch
from Music.MusicUtilities.database.chats import is_served_chat
from Music.MusicUtilities.database.queue import remove_active_chat
from Music.MusicUtilities.database.sudo import get_sudoers
from Music.MusicUtilities.helpers.filters import command
from Music.MusicUtilities.database.assistant import (_get_assistant, get_as_names, get_assistant,
                        save_assistant)
from Music.MusicUtilities.database.auth import (_get_authusers, add_nonadmin_chat, delete_authuser,
                   get_authuser, get_authuser_count, get_authuser_names,
                   is_nonadmin_chat, remove_nonadmin_chat, save_authuser)
from Music.MusicUtilities.database.blacklistchat import blacklist_chat, blacklisted_chats, whitelist_chat
from Music.MusicUtilities.helpers.admins import ActualAdminCB
from Music.MusicUtilities.helpers.inline import personal_markup, setting_markup
from Music.MusicUtilities.helpers.inline import (custommarkup, dashmarkup, setting_markup,
                          start_pannel, usermarkup, volmarkup)
from Music.MusicUtilities.helpers.thumbnails import down_thumb
from Music.MusicUtilities.helpers.ytdl import ytdl_opts
from Music.MusicUtilities.tgcallsrun.music import pytgcalls
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
    filters.command(["المؤقت", "مؤقتت"]) & filters.group & ~filters.edited
)
@errors
@authorized_users_only
async def pause(_, message: Message):
    try:
        conchat = await _.get_chat(message.chat.id)
        conid = conchat.linked_chat.id
        chid = conid
    except:
        await message.reply("**␥┆هل هـذه القنـاة مرتبطـة بالحسـاب...**")
        return
    chat_id = chid
    (
        await message.reply_text("ايقاف مؤقت ▶️")
    ) if (
        callsmusic.pause(chat_id)
    ) else (
        await message.reply_text("␥┆لا يـوجد شيء لـ ايقـافـه!❗")
    )


@Client.on_message(
    filters.command(["الاستئناف", "استئنافف"]) & filters.group & ~filters.edited
)
@authorized_users_only
async def resume(_, message: Message):
    try:
        conchat = await _.get_chat(message.chat.id)
        conid = conchat.linked_chat.id
        chid = conid
    except:
        await message.reply("**␥┆هل هـذه القنـاة مرتبطـة بالحسـاب...**")
        return
    chat_id = chid
    (
       await message.reply_text("استئنـاف ⏸")
    ) if (
        callsmusic.resume(chat_id)
    ) else (
        await message.reply_text("␥┆لا يـوجد شيء لـ استئنـافه!❗")
    )
        
    

@Client.on_message(
    filters.command(["الايقاف", "ايقافف"]) & filters.group & ~filters.edited
)
@authorized_users_only
async def stop(_, message: Message):
    try:
        conchat = await _.get_chat(message.chat.id)
        conid = conchat.linked_chat.id
        chid = conid
    except:
        await message.reply("**␥┆هل هـذه القنـاة مرتبطـة بالحسـاب...**")
        return
    chat_id = chid
    if chat_id not in callsmusic.active_chats:
        await message.reply_text("␥┆لا يـوجد شيء تحت التشغيـل!❗")
    else:
        try:
            queues.clear(chat_id)
        except QueueEmpty:
            pass

        await callsmusic.stop(chat_id)
        await message.reply_text("␥┆تـم ايقـاف التشغيـل! ⏹")


@Client.on_message(
    filters.command(["التالي", "تاليي"]) & filters.group & ~filters.edited
)
@authorized_users_only
async def skip(_, message: Message):
    global que
    try:
        conchat = await _.get_chat(message.chat.id)
        conid = conchat.linked_chat.id
        chid = conid
    except:
        await message.reply("**␥┆هل هـذه القنـاة مرتبطـة بالحسـاب...**")
        return
    chat_id = chid
    if chat_id not in callsmusic.active_chats:
        await message.reply_text("␥┆لا يـوجد شيء لايقـافه مؤقتـاً!❗")
    else:
        queues.task_done(chat_id)

        if queues.is_empty(chat_id):
            await callsmusic.stop(chat_id)
        else:
            await callsmusic.set_stream(chat_id, queues.get(chat_id)["file"])

    qeue = que.get(chat_id)
    if qeue:
        skip = qeue.pop(0)
    if not qeue:
        return
    await message.reply_text(f"- تـم الايقاف **{skip[0]}**\n- قـم بتشغيل **{qeue[0][0]}**")
    
    
@Client.on_message(
    filters.command(["الكتم", "كتم"]) & filters.group & ~filters.edited
)
@authorized_users_only
async def mute(_, message: Message):
    global que
    try:
        conchat = await _.get_chat(message.chat.id)
        conid = conchat.linked_chat.id
        chid = conid
    except:
        await message.reply("**␥┆هل هـذه القنـاة مرتبطـة بالحسـاب...**")
        return 
    chat_id = chid
    result = await callsmusic.mute(chat_id)
    (
        await message.reply_text(" تـم الكتم .. بنجـاح ✅")
    ) if (
        result == 0
    ) else (
        await message.reply_text(" العضـو بالفعـل مكتوم ❌")
    ) if (
        result == 1
    ) else (
        await message.reply_text(" العضـو ليـس متصـل ❌")
    )
        
        
@Client.on_message(
    filters.command(["الغاء الكتم", "الغاء كتم"]) & filters.group & ~filters.edited
)
@authorized_users_only
async def unmute(_, message: Message):
    global que
    try:
        conchat = await _.get_chat(message.chat.id)
        conid = conchat.linked_chat.id
        chid = conid
    except:
        await message.reply("**␥┆هل هـذه القنـاة مرتبطـة بالحسـاب...**")
        return 
    chat_id = chid
    result = await callsmusic.unmute(chat_id)
    (
        await message.reply_text(" تـم الغـاء كتمـه .. بنجـاح✅")
    ) if (
        result == 0
    ) else (
        await message.reply_text("  العضـو ليـس مكتوم ❌")
    ) if (
        result == 1
    ) else (
        await message.reply_text(" العضـو ليـس متصـل ❌")
    )


@Client.on_message(filters.command("تحديث المشرفين"))
async def admincache(client, message: Message):
    try:
        conchat = await client.get_chat(message.chat.id)
        conid = conchat.linked_chat.id
        chid = conid
    except:
        await message.reply("**␥┆هل هـذه القنـاة مرتبطـة بالحسـاب...**")
        return
    set(
        chid,
        [
            member.user
            for member in await conchat.linked_chat.get_members(filter="administrators")
        ],
    )
    await message.reply_text("**␥┆تم تحديث قائمـة المشـرفين ..  بنجـاح ❇️**")
