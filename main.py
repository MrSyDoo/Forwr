#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 
import pytz
import os
from datetime import date, datetime 
from config import Config
from script import Script
from info import PORT, LOG_CHANNEL
from pyrogram import Client as ACE , idle
import asyncio, logging
import tgcrypto
from pyromod import listen
from logging.handlers import RotatingFileHandler

LOGGER = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    format="%(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler(
            "log.txt", maxBytes=5000000, backupCount=10
        ),
        logging.StreamHandler(),
    ],
)

# Auth Users
BOT_OWNER_ID = [ int(chat) for chat in Config.BOT_OWNER_ID.split(",") if chat != '']

# Prefixes 
prefixes = ["/", "~", "?", "!"]

plugins = dict(root="plugins")
if __name__ == "__main__" :
    AceBot = ACE(
        "AceBot",
        bot_token=Config.BOT_TOKEN,
        api_id=Config.API_ID,
        api_hash=Config.API_HASH,
        sleep_threshold=120,
        plugins=plugins
    )
    
    async def main():
        await AceBot.start()
        bot_info  = await AceBot.get_me()
        LOGGER.info(f"<--- @{bot_info.username} Started (c) ACE --->")
        today = date.today()
        tz = pytz.timezone('Asia/Kolkata')
        now = datetime.now(tz)
        time = now.strftime("%H:%M:%S %p")
        await AceBot.send_message(chat_id=LOG_CHANNEL, text=Script.RESTART_TXT.format(today, time))
        app = web.AppRunner(await web_server())
        await app.setup()
        bind_address = "0.0.0.0"
        await web.TCPSite(app, bind_address, PORT).start()
        await idle()
    
    asyncio.get_event_loop().run_until_complete(main())
    LOGGER.info(f"<---Bot Stopped-->")
