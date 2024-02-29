# Copyright (C) 2021-2023 TeamUltroid.
# Ultroid - UserBot.
# UltroidUser - XexenId.
#
# This file is a part of https://github.com/teamultroid/ultroid.
# Please read the GNU affero general license.
# https://www.github.com/teamultroid/ultroid/blob/main/license.


from motor.motor_asyncio import AsyncIOMotorClient
from config import MONGO_DB_URI
from ..logging import LOGGER

LOGGER(__name__).info("Connecting to your mongo database...")
try:
    _mongo_async_ = AsyncIOMotorClient(MONGO_DB_URI)
    mongodb = _mongo_async_.Anon
    LOGGER(__name__).info("Connected to your mongo database.")
except:
    LOGGER(__name__).error("Failed to connect to your mongo database.")
    exit()
