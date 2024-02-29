# Copyright (C) 2021-2023 TeamUltroid.
# Ultroid - UserBot.
# UltroidUser - XexenId.
#
# This file is a part of https://github.com/teamultroid/ultroid.
# Please read the GNU affero general license.
# https://www.github.com/teamultroid/ultroid/blob/main/license.


from pyrogram.enums import ParseMode

from AreaDemus import app
from AreaDemus.utils.database import is_on_off
from config import LOGGER_ID


async def play_logs(message, streamtype):
    if await is_on_off(2):
        logger_text = f"""
<b>{app.mention} play lᴏɢ</b>

<b>chat id :</b> <code>{message.chat.id}</code>
<b>chat name :</b> {message.chat.title}
<b>chat ᴜsername :</b> @{message.chat.username}

<b>ᴜser id :</b> <code>{message.from_user.id}</code>
<b>name :</b> {message.from_user.mention}
<b>ᴜsername :</b> @{message.from_user.username}

<b>qᴜery :</b> {message.text.split(None, 1)[1]}
<b>streamtype :</b> {streamtype}"""
        if message.chat.id != LOGGER_ID:
            try:
                await app.send_message(
                    chat_id=LOGGER_ID,
                    text=logger_text,
                    parse_mode=ParseMode.HTML,
                    disable_web_page_preview=True,
                )
            except:
                pass
        return
