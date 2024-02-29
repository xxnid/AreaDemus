# Copyright (C) 2021-2023 TeamUltroid.
# Ultroid - UserBot.
# UltroidUser - XexenId.
#
# This file is a part of https://github.com/teamultroid/ultroid.
# Please read the GNU affero general license.
# https://www.github.com/teamultroid/ultroid/blob/main/license.


from pyrogram import Client
import config
from ..logging import LOGGER

assistants = []
assistantids = []


class Userbot(Client):
    def __init__(self):
        self.one = Client(
            name="ADXAsstnt1",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING1),
            no_updates=True,
        )
        self.two = Client(
            name="ADXAsstnt2",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING2),
            no_updates=True,
        )
        self.three = Client(
            name="ADXAsstnt",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING3),
            no_updates=True,
        )
        self.four = Client(
            name="ADXAsstnt4",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING4),
            no_updates=True,
        )
        self.five = Client(
            name="ADXAsstnt5",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING5),
            no_updates=True,
        )

    async def start(self):
        LOGGER(__name__).info(f"Starting assistants...")
        if config.STRING1:
            await self.one.start()
            try:
                await self.one.join_chat("AreaDemus")
                await self.one.join_chat("AreaDemusChat")
            except:
                pass
            assistants.append(1)
            try:
                await self.one.send_message(config.LOGGER_ID, "Assistant started")
            except:
                LOGGER(__name__).error(
                    "Assistant account 1 has failed to access the log group. Make sure that you have added your assistant to your log group and promoted as admin."
                )
                exit()
            self.one.id = self.one.me.id
            self.one.name = self.one.me.mention
            self.one.username = self.one.me.username
            assistantids.append(self.one.id)
            LOGGER(__name__).info(f"Assistant started as {self.one.name}")

        if config.STRING2:
            await self.two.start()
            try:
                await self.two.join_chat("AreaDemus")
                await self.one.join_chat("AreaDemusChat")
            except:
                pass
            assistants.append(2)
            try:
                await self.two.send_message(config.LOGGER_ID, "Assistant started")
            except:
                LOGGER(__name__).error(
                    "Assistant Account 2 has failed to access the log group. Make sure that you have added your assistant to your log group and promoted as admin."
                )
                exit()
            self.two.id = self.two.me.id
            self.two.name = self.two.me.mention
            self.two.username = self.two.me.username
            assistantids.append(self.two.id)
            LOGGER(__name__).info(f"Assistant two started as {self.two.name}")

        if config.STRING3:
            await self.three.start()
            try:
                await self.three.join_chat("AreaDemus")
                await self.one.join_chat("AreaDemusChat")
            except:
                pass
            assistants.append(3)
            try:
                await self.three.send_message(config.LOGGER_ID, "Assistant Started")
            except:
                LOGGER(__name__).error(
                    "Assistant account 3 has failed to access the log group. Make sure that you have added your assistant to your log group and promoted as admin."
                )
                exit()
            self.three.id = self.three.me.id
            self.three.name = self.three.me.mention
            self.three.username = self.three.me.username
            assistantids.append(self.three.id)
            LOGGER(__name__).info(f"Assistant three started as {self.three.name}")

        if config.STRING4:
            await self.four.start()
            try:
                await self.four.join_chat("AreaDemus")
                await self.one.join_chat("AreaDemusChat")
            except:
                pass
            assistants.append(4)
            try:
                await self.four.send_message(config.LOGGER_ID, "Assistant started")
            except:
                LOGGER(__name__).error(
                    "Assistant account 4 has failed to access the log group. Make sure that you have added your assistant to your log group and promoted as admin."
                )
                exit()
            self.four.id = self.four.me.id
            self.four.name = self.four.me.mention
            self.four.username = self.four.me.username
            assistantids.append(self.four.id)
            LOGGER(__name__).info(f"Assistant four started as {self.four.name}")

        if config.STRING5:
            await self.five.start()
            try:
                await self.five.join_chat("AreaDemus")
                await self.one.join_chat("AreaDemusChat")
            except:
                pass
            assistants.append(5)
            try:
                await self.five.send_message(config.LOGGER_ID, "Assistant started")
            except:
                LOGGER(__name__).error(
                    "Assistant account 5 has failed to access the log group. Make sure that you have added your assistant to your log group and promoted as admin."
                )
                exit()
            self.five.id = self.five.me.id
            self.five.name = self.five.me.mention
            self.five.username = self.five.me.username
            assistantids.append(self.five.id)
            LOGGER(__name__).info(f"Assistant five started as {self.five.name}")

    async def stop(self):
        LOGGER(__name__).info(f"Stopping assistants...")
        try:
            if config.STRING1:
                await self.one.stop()
            if config.STRING2:
                await self.two.stop()
            if config.STRING3:
                await self.three.stop()
            if config.STRING4:
                await self.four.stop()
            if config.STRING5:
                await self.five.stop()
        except:
            pass
