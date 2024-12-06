import os
import sys
import asyncio
import random
from database import Database, db
from info import AUTH_CHANNEL, BOTCRACKER_CHNL
from config import Config, temp
from MrSyD import is_req_subscribed, is_reqb_subscribed
from info import PICS
from script import Script
from pyrogram import Client, filters, enums
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, InputMediaDocument, InputMediaPhoto

main_buttons = [[
        InlineKeyboardButton('🌋 Sᴜᴩᴩ0ʀᴛ Gʀ0ᴜᴩ 🌋', url='https://t.me/venombotupdates'),
        InlineKeyboardButton('🗞️ Uᴩᴅᴀᴛᴇꜱ CʜΔɴɴᴇʟ 🗞️', url='https://t.me/BOT_CRACKER')
        ],[
        InlineKeyboardButton('🎐 Hᴇʟᴩ 🎐', callback_data='help'),
        InlineKeyboardButton('D', url='https://t.me/BOT_CRACKER'),
        InlineKeyboardButton('🔍 Δʙᴏᴜᴛ 🔎', callback_data='aboutt')
        

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
            caption=Script.START_TXT.format(message.from_user.mention),
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
    )

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
            InlineKeyboardButton('«« ʙΔᴄᴋ', callback_data='back')
    ]]
    reply_markup = InlineKeyboardMarkup(buttons)
    await bot.edit_message_media(
            query.message.chat.id, 
            query.message.id, 
            InputMediaPhoto(random.choice(PICS))
    )
    await query.message.edit_text(
        text=Script.HELP_TXT,
        reply_markup=reply_markup)

@Client.on_callback_query(filters.regex(r'^how_to_use'))
async def how_to_use(bot, query):
    buttons = [[InlineKeyboardButton('«« ʙΔᴄᴋ', callback_data='help')]]
    reply_markup = InlineKeyboardMarkup(buttons)
    await bot.edit_message_media(
            query.message.chat.id, 
            query.message.id, 
            InputMediaPhoto(random.choice(PICS))
    )
    await query.message.edit_text(
        text=Script.HOW_USE_TXT,
        reply_markup=reply_markup,
        disable_web_page_preview=True
    )

@Client.on_callback_query(filters.regex(r'^back'))
async def back(bot, query):
    reply_markup = InlineKeyboardMarkup(main_buttons)
    await bot.edit_message_media(
            query.message.chat.id, 
            query.message.id, 
            InputMediaPhoto(random.choice(PICS))
    )
    await query.message.edit_text(
       reply_markup=reply_markup,
       text=Script.START_TXT.format(
                query.from_user.first_name))

@Client.on_callback_query(filters.regex(r'^about'))
async def about(bot, query):
    buttons = [[InlineKeyboardButton('«« ʙΔᴄᴋ', callback_data='help')]]
    reply_markup = InlineKeyboardMarkup(buttons)
    await bot.edit_message_media(
            query.message.chat.id, 
            query.message.id, 
            InputMediaPhoto(random.choice(PICS))
    )
    await query.message.edit_text(
        text=Script.ABOUT_TXT,
        reply_markup=reply_markup,
        disable_web_page_preview=True,
    )

@Client.on_callback_query(filters.regex(r'^aboutt'))
async def aboutt(bot, query):
    buttons = [[InlineKeyboardButton('«« ʙΔᴄᴋ', callback_data='back')]]
    reply_markup = InlineKeyboardMarkup(buttons)
    await bot.edit_message_media(
            query.message.chat.id, 
            query.message.id, 
            InputMediaPhoto(random.choice(PICS))
    )
    await query.message.edit_text(
        text=Script.ABOUT_TXT,
        reply_markup=reply_markup,
        disable_web_page_preview=True,
    )

@Client.on_callback_query(filters.regex(r'^status'))
async def status(bot, query):
    users_count, bots_count = await db.total_users_bots_count()
    buttons = [[InlineKeyboardButton('«« ʙΔᴄᴋ', callback_data='help')]]
    reply_markup = InlineKeyboardMarkup(buttons)
    await bot.edit_message_media(
            query.message.chat.id, 
            query.message.id, 
            InputMediaPhoto(random.choice(PICS))
    )
    await query.message.edit_text(
        text=Script.STATUS_TXT.format(users_count, bots_count, temp.forwardings),
        reply_markup=reply_markup,
        disable_web_page_preview=True,
    )

@Client.on_callback_query(filters.regex(r'^sydcheck'))
async def sydcheck(bot, query):
    if AUTH_CHANNEL and not await is_req_subscribed(bot, query):
            await query.answer("ʀᴇQᴇᴜꜱᴛ ᴛᴏ Jᴏɪɴ ᴏᴜʀ ᴄʜᴀɴɴᴇʟ ᴍᴀʜɴ! 😒 Dᴏɴᴛ ᴛʀʏ ᴛᴏ ꜱʜᴏᴡ ʏᴏᴜʀ ᴏᴠᴇʀꜱᴍᴀʀᴛɴᴇꜱꜱ ᴩʟᴢ🥲🥲", show_alert=True)
            return
    await query.message.edit_text("<b>Oᴋ✅, ʏᴏᴜ ᴄΔɴ ᴄᴏɴᴛɪɴᴜᴇ ʏᴏᴜʀ ᴩʀᴏᴄᴇꜱꜱ.... Δɴᴅ Tʜᴀɴᴋꜱ ꜰᴏʀ ᴜꜱɪɴɢ ᴏᴜʀ ʙᴏᴛ... 🧭\nCʟɪᴄᴋ ᴏɴ /forward Tᴏ ᴄᴏɴᴛɪɴᴜᴇ... 🪭</b>")


@Client.on_callback_query(filters.regex(r'^syd0check'))
async def sydcheck(bot, query):
    if BOTCRACKER_CHNL and not await is_reqb_subscribed(bot, query):
            await query.answer("ʀᴇQᴇᴜꜱᴛ ᴛᴏ Jᴏɪɴ ᴏᴜʀ ᴄʜᴀɴɴᴇʟ ᴍᴀʜɴ! 😒 Dᴏɴᴛ ᴛʀʏ ᴛᴏ ꜱʜᴏᴡ ʏᴏᴜʀ ᴏᴠᴇʀꜱᴍᴀʀᴛɴᴇꜱꜱ ᴩʟᴢ🥲🥲", show_alert=True)
            return
    await query.message.edit_text("<b>Oᴋ✅, ʏᴏᴜ ᴄΔɴ ᴄᴏɴᴛɪɴᴜᴇ ʏᴏᴜʀ ᴩʀᴏᴄᴇꜱꜱ.... Δɴᴅ Tʜᴀɴᴋꜱ ꜰᴏʀ ᴜꜱɪɴɢ ᴏᴜʀ ʙᴏᴛ... 🧭\nCʟɪᴄᴋ ᴏɴ /forward Tᴏ ᴄᴏɴᴛɪɴᴜᴇ... 🪭</b>")

        
