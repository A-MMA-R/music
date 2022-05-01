import os

import random

from cache.admins import admins

from datetime import datetime

from sys import version_info

from time import time

from config import (

    ALIVE_IMG,

    ALIVE_NAME,

    AMR_NAME,

    BOT_NAME,

    BOT_USERNAME,

    GROUP_SUPPORT,

    OWNER_NAME,

    UPDATES_CHANNEL,

    BOT_TOKEN

)
@Client.on_message(command(["Kstop", f"Kstop@NKQBoT", "تعطيل الكت"]) & ~filters.edited)

@authorized_users_only

async def stop_filter(client: Client, message: Message):

    start = time()

    m_reply = await message.reply_text(

        f"- اهلين عيني {message.from_user.mention()}\n- ابشر تم تعطيل امر كت"

    )

    obj = settingsApp.BotSettings()

    obj.edit_in_file("open", "no")

    delta_ping = time() - start

    await m_reply.edit_text(

        f"- اهلين عيني {message.from_user.mention()}\n- ابشر تم تعطيل امر كت"

    )

    

@Client.on_message(filters.command("فيونا اقفلي الكت", [".", ""]) & ~filters.edited)

@authorized_users_only

async def stop_filterr(client: Client, message: Message):

    start = time()

    m_reply = await message.reply_text(

        f"- اهلين عيني {message.from_user.mention()}\n- ابشر تم تعطيل امر كت"

    )

    obj = settingsApp.BotSettings()

    obj.edit_in_file("open", "no")

    delta_ping = time() - start

    await m_reply.edit_text(

        f"- اهلين عيني {message.from_user.mention()}\n- ابشر تم تعطيل امر كت"

    )

@Client.on_message(command(["Kstart", f"Kstart@NKQBoT"]) & ~filters.edited)

@authorized_users_only

async def start_filter(client: Client, message: Message):

    start = time()

    m_reply = await message.reply_text(

        f"- اهلين عيني {message.from_user.mention()}\n- ابشر تم تفعيل امر كت"

    )

    obj = settingsApp.BotSettings()

    obj.edit_in_file("open", "yes")

    delta_ping = time() - start

    await m_reply.edit_text(

        f"- اهلين عيني {message.from_user.mention()}\n- ابشر تم تفعيل امر كت"

    )

    

@Client.on_message(filters.command("فيونا شغلي الكت", [".", ""]) & ~filters.edited)

@authorized_users_only

async def start_filterrr(client: Client, message: Message):

    start = time()

    m_reply = await message.reply_text(

        f"- اهلين عيني {message.from_user.mention()}\n- ابشر تم تفعيل امر كت"

    )

    obj = settingsApp.BotSettings()

    obj.edit_in_file("open", "yes")

    delta_ping = time() - start

    await m_reply.edit_text(

        f"- اهلين عيني {message.from_user.mention()}\n- ابشر تم تفعيل امر كت"

    )
