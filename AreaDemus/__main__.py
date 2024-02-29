# Copyright (C) 2021-2023 TeamUltroid.
# Ultroid - UserBot.
# UltroidUser - XexenId.
#
# This file is a part of https://github.com/teamultroid/ultroid.
# Please read the GNU affero general license.
# https://www.github.com/teamultroid/ultroid/blob/main/license.


import asyncio
import importlib

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from AreaDemus import LOGGER, app, userbot
from AreaDemus.core.call import Anony
from AreaDemus.misc import sudo
from AreaDemus.plugins import ALL_MODULES
from AreaDemus.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error("Assistant client variables not defined, exiting...")
        exit()
    await sudo()
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("AreaDemus.plugins" + all_module)
    LOGGER("AreaDemus.plugins").info("Successfully imported modules...")
    await userbot.start()
    await Anony.start()
    try:
        await Anony.stream_call("https://graph.org/file/0cc4a470fb3c5a7007bfe.jpg")
    except NoActiveGroupCall:
        LOGGER("AreaDemus").error(
            "Please turn on the videochat of your log group\channel.\n\nStopping bot..."
        )
        exit()
    except:
        pass
    await Anony.decorators()
    LOGGER("AreaDemus").info(
        "\x41\x6e\x6f\x6e\x58\x20\x4d\x75\x73\x69\x63\x20\x42\x6f\x74\x20\x53\x74\x61\x72\x74\x65\x64\x20\x53\x75\x63\x63\x65\x73\x73\x66\x75\x6c\x6c\x79\x2e\n\n\x44\x6f\x6e'\x74\x20\x66\x6f\x72\x67\x65\x74\x20\x74\x6f\x20\x76\x69\x73\x69\x74\x20\x40\x46\x61\x6c\x6c\x65\x6e\x41\x73\x73\x6f\x63\x69\x61\x74\x69\x6f\x6e"
    )
    await idle()
    await app.stop()
    await userbot.stop()
    LOGGER("AreaDemus").info("Stopping AreaDemus music bot...")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())