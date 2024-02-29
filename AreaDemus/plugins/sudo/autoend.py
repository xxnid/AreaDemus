# Copyright (C) 2021-2023 TeamUltroid.
# Ultroid - UserBot.
# UltroidUser - XexenId.
#
# This file is a part of https://github.com/teamultroid/ultroid.
# Please read the GNU affero general license.
# https://www.github.com/teamultroid/ultroid/blob/main/license.


from pyrogram import filters
from pyrogram.types import Message

from AreaDemus import app
from AreaDemus.misc import SUDOERS
from AreaDemus.utils.database import autoend_off, autoend_on


@app.on_message(filters.command("autoend") & SUDOERS)
async def auto_end_stream(_, message: Message):
    usage = "<b>Example :</b>\n\n/autoend (enable & disable)."
    if len(message.command) != 2:
        return await message.reply_text(usage)
    state = message.text.split(None, 1)[1].strip().lower()
    if state == "enable":
        await autoend_on()
        await message.reply_text(
            "Auto end stream enabled, assistant will automatically leave the videochat after few minutes when no one is listening."
        )
    elif state == "disable":
        await autoend_off()
        await message.reply_text("Auto end stream disable.")
    else:
        await message.reply_text(usage)
