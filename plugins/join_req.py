from pyrogram import Client, filters, enums
from pyrogram.types import ChatJoinRequest
from database import db, bd
from info import AUTH_CHANNEL, ADMINS, SYD_CHANNEL

@Client.on_chat_join_request(filters.chat(AUTH_CHANNEL))
async def join_reqs(client, message: ChatJoinRequest):
  if not await db.find_join_req(message.from_user.id):
    await db.add_join_req(message.from_user.id)

@Client.on_message(filters.command("delreq") & filters.private & filters.user(ADMINS))
async def del_requests(client, message):
    await db.del_join_req()    
    await message.reply("<b>⚙ ꜱᴜᴄᴄᴇꜱꜱғᴜʟʟʏ ᴄʜᴀɴɴᴇʟ ʟᴇғᴛ ᴜꜱᴇʀꜱ ᴅᴇʟᴇᴛᴇᴅ</b>")
  
@Client.on_chat_join_request(filters.chat(SYD_CHANNEL))
async def join_reqsa(client, message: ChatJoinRequest):
  if not await bd.find_join_req(message.from_user.id):
    await bd.add_join_req(message.from_user.id)

@Client.on_message(filters.command("delreqa") & filters.private & filters.user(ADMINS))
async def del_requestsa(client, message):
    await bd.del_join_req()    
    await message.reply("<b>⚙ ꜱᴜᴄᴄᴇꜱꜱғᴜʟʟʏ ᴄʜᴀɴɴᴇʟ ʟᴇғᴛ ᴜꜱᴇʀꜱ ᴅᴇʟᴇᴛᴇᴅ</b>")
