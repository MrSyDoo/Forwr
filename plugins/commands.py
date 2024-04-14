import os
import sys
import asyncio
import random
from database import Database, db
from info import AUTH_CHANNEL
from config import Config, temp
from info import PICS
from script import Script
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, InputMediaDocument

main_buttons = [[
        InlineKeyboardButton('🌋 Sᴜᴩᴩ0ʀᴛ Gʀ0ᴜᴩ 🌋', url='https://t.me/venombotupdates'),
        InlineKeyboardButton('🗞️ Uᴩᴅᴀᴛᴇꜱ CʜΔɴɴᴇʟ 🗞️', url='https://t.me/BOT_CRACKER')
        ],[
        InlineKeyboardButton('🎐 Hᴇʟᴩ 🎐', callback_data='help'),
        InlineKeyboardButton('🔍 Δʙᴏᴜᴛ 🔎', callback_data='about')
        

]]

#===================Start Function===================#

@Client.on_message(filters.private & filters.command(['start']))
async def start(client, message):
    user = message.from_user
    if not await db.is_user_exist(user.id):
      await db.add_user(user.id, user.first_name)
    reply_markup = InlineKeyboardMarkup(main_buttons)
    await message.reply_photo(
        photo=random.choice(PICS),
        reply_markup=reply_markup,
        text=Script.START_TXT.format(message.from_user.first_name))

#==================Restart Function==================#

@Client.on_message(filters.private & filters.command(['restart']) & filters.user(Config.BOT_OWNER_ID))
async def restart(client, message):
    msg = await message.reply_text(
        text="<i>Trying to restarting.....</i>"
    )
    await asyncio.sleep(5)
    await msg.edit("<i>Server restarted successfully ✅</i>")
    os.execl(sys.executable, sys.executable, *sys.argv)

#==================Callback Functions==================#

@Client.on_callback_query(filters.regex(r'^help'))
async def helpcb(bot, query):
    buttons = [[
            InlineKeyboardButton('💦 Sᴛᴀᴛᴜꜱ 💦', callback_data='status'),
            ],[
            InlineKeyboardButton('🗺️ Uꜱᴇʀ Mᴀɴᴜᴀʟ 🗺️', callback_data='how_to_use')
            ],[
            InlineKeyboardButton('🪼 Sᴇᴛᴛɪɴɢꜱ 🪼', callback_data='settings#main')
            ],[
            InlineKeyboardButton('ʙΔᴄᴋ', callback_data='back')
    ]]
    reply_markup = InlineKeyboardMarkup(buttons)
    await query.message.edit_text(
        text=Script.HELP_TXT,
        reply_markup=reply_markup)

@Client.on_callback_query(filters.regex(r'^how_to_use'))
async def how_to_use(bot, query):
    buttons = [[InlineKeyboardButton('• back', callback_data='help')]]
    reply_markup = InlineKeyboardMarkup(buttons)
    await query.message.edit_text(
        text=Script.HOW_USE_TXT,
        reply_markup=reply_markup,
        disable_web_page_preview=True
    )

@Client.on_callback_query(filters.regex(r'^back'))
async def back(bot, query):
    reply_markup = InlineKeyboardMarkup(main_buttons)
    await query.message.edit_text(
       reply_markup=reply_markup,
       text=Script.START_TXT.format(
                query.from_user.first_name))

@Client.on_callback_query(filters.regex(r'^about'))
async def about(bot, query):
    buttons = [[InlineKeyboardButton('• back', callback_data='help')]]
    reply_markup = InlineKeyboardMarkup(buttons)
    await query.message.edit_text(
        text=Script.ABOUT_TXT,
        reply_markup=reply_markup,
        disable_web_page_preview=True,
    )

@Client.on_callback_query(filters.regex(r'^status'))
async def status(bot, query):
    users_count, bots_count = await db.total_users_bots_count()
    buttons = [[InlineKeyboardButton('• back', callback_data='help')]]
    reply_markup = InlineKeyboardMarkup(buttons)
    await query.message.edit_text(
        text=Script.STATUS_TXT.format(users_count, bots_count, temp.forwardings),
        reply_markup=reply_markup,
        disable_web_page_preview=True,
    )

@Client.on_callback_query(filters.regex(r'^sydcheck'))
async def sydcheck(bot, query):
    if AUTH_CHANNEL and not await is_req_subscribed(client, query):
            await query.answer("Jᴏɪɴ ᴏᴜʀ ᴜᴘᴅᴀᴛᴇꜱ ᴄʜᴀɴɴᴇʟ ᴍᴀʜɴ! 😒", show_alert=True)
            return
    await query.message.edit_text("<b>Hi</b>")

        
