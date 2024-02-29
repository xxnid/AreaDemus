# Copyright (C) 2021-2023 TeamUltroid.
# Ultroid - UserBot.
# UltroidUser - XexenId.
#
# This file is a part of https://github.com/teamultroid/ultroid.
# Please read the GNU affero general license.
# https://www.github.com/teamultroid/ultroid/blob/main/license.


from pyrogram.enums import MessageEntityType
from pyrogram.types import Message, User

from AreaDemus import app


async def extract_user(m: Message) -> User:
    if m.reply_to_message:
        return m.reply_to_message.from_user
    msg_entities = m.entities[1] if m.text.startswith("/") else m.entities[0]
    return await app.get_users(
        msg_entities.user.id
        if msg_entities.type == MessageEntityType.TEXT_MENTION
        else int(m.command[1])
        if m.command[1].isdecimal()
        else m.command[1]
    )
