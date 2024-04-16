import re, asyncio
from database import Database, db
from config import temp
from .test import CLIENT
from info import BOTCRACKER_CHNL
from MrSyD import is_reqb_subscribed
from script import Script
import base64
from pyrogram.file_id import FileId
from pyrogram import Client, filters, enums
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto

CLIENT = CLIENT()
COMPLETED_BTN = InlineKeyboardMarkup([[InlineKeyboardButton('• sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ •', url='https://t.me/crazysupportz')],
                [InlineKeyboardButton('• ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ •', url='https://t.me/crazybotz')]])
CANCEL_BTN = InlineKeyboardMarkup([[InlineKeyboardButton('• ᴄᴀɴᴄᴇʟ', 'terminate_frwd')]])

# functions
def encode_file_id(s: bytes) -> str:
    r = b""
    n = 0

    for i in s + bytes([22]) + bytes([4]):
        if i == 0:
            n += 1
        else:
            if n:
                r += b"\x00" + bytes([n])
                n = 0

            r += bytes([i])

    return base64.urlsafe_b64encode(r).decode().rstrip("=")

def unpack_new_file_id(new_file_id):
    """Return file_id"""
    decoded = FileId.decode(new_file_id)
    file_id = encode_file_id(
        pack(
            "<iiqq",
            int(decoded.file_type),
            decoded.dc_id,
            decoded.media_id,
            decoded.access_hash
        )
    )
    return file_id

@Client.on_message(filters.command("equify") & filters.private)
async def unequify(client, message):
    if BOTCRACKER_CHNL and not await is_reqb_subscribed(bot, message):
        try:
            invite_link = await bot.create_chat_invite_link(int(BOTCRACKER_CHNL), creates_join_request=True)
        except ChatAdminRequired:
            logger.error("Make sure Bot is admin in Forcesub channel")
            return
        btn = [
            [
                InlineKeyboardButton(
                    "📌 ᴊᴏɪɴ ᴜᴘᴅᴀᴛᴇꜱ ᴄʜᴀɴɴᴇʟ 📌", url='https://gplinks.co/BREcQ'
                )
            ],[
                InlineKeyboardButton(
                    "↻ Tʀʏ Aɢᴀɪɴ", callback_data='syd0check'
                )
              ]
        ]
        await bot.send_message(
            text="ᴊᴏɪɴ ᴏᴜʀ ᴜᴘᴅᴀᴛᴇꜱ ᴄʜᴀɴɴᴇʟ ᴀɴᴅ ᴛʜᴇɴ ᴄʟɪᴄᴋ ᴏɴ ᴛʀʏ ᴀɢᴀɪɴ ᴛᴏ ɢᴇᴛ ʏᴏᴜʀ ʀᴇǫᴜᴇꜱᴛᴇᴅ ꜰɪʟᴇ.",
            reply_markup=InlineKeyboardMarkup(btn),
            parse_mode=enums.ParseMode.MARKDOWN
            )
        return
    user_id = message.from_user.id
    temp.CANCEL[user_id] = False
    if temp.lock.get(user_id) and str(temp.lock.get(user_id))=="True":
       return await message.reply("**please wait until previous task complete**")
    _bot = await db.get_bot(user_id)
    if not _bot or _bot['is_bot']:
       return await message.reply("<b>ɴᴇᴇᴅ ᴜꜱᴇʀʙᴏᴛ ᴛᴏ ᴅᴏ ᴛʜɪꜱ ᴘʀᴏᴄᴇꜱꜱ. ᴘʟᴇᴀꜱᴇ ᴀᴅᴅ ᴀ ᴜꜱᴇʀʙᴏᴛ ᴜꜱɪɴɢ /settings</b>")
    target = await client.ask(user_id, text="**ꜰᴏʀᴡᴀʀᴅ ᴛʜᴇ ʟᴀꜱᴛ ᴍᴇꜱꜱᴀɢᴇ ꜰʀᴏᴍ ᴛᴀʀɢᴇᴛ ᴄʜᴀᴛ ᴏʀ ꜱᴇɴᴅ ʟᴀꜱᴛ ᴍᴇꜱꜱᴀɢᴇ ʟɪɴᴋ.**\n/cancel - `cancel this process`")
    if target.text.startswith("/"):
       return await message.reply("**ᴘʀᴏᴄᴇꜱꜱ ᴄᴀɴᴄᴇʟʟᴇᴅ !**")
    elif target.text:
       regex = re.compile("(https://)?(t\.me/|telegram\.me/|telegram\.dog/)(c/)?(\d+|[a-zA-Z_0-9]+)/(\d+)$")
       match = regex.match(target.text.replace("?single", ""))
       if not match:
          return await message.reply('**Invalid link**')
       chat_id = match.group(4)
       last_msg_id = int(match.group(5))
       if chat_id.isnumeric():
          chat_id  = int(("-100" + chat_id))
    elif fromid.forward_from_chat.type in ['channel', 'supergroup']:
         last_msg_id = target.forward_from_message_id
         chat_id = target.forward_from_chat.username or target.forward_from_chat.id
    else:
         return await message.reply_text("**invalid !**")
    confirm = await client.ask(user_id, text="**send /yes to start the process and /no to cancel this process**")
    if confirm.text.lower() == '/no':
       return await confirm.reply("**process cancelled !**")
    sts = await confirm.reply("`processing..`")
    try:
       bot = await client.start_clone_bot(CLIENT.client(_bot))
    except Exception as e:
       return await sts.edit(e)
    try:
        k = await bot.send_message(chat_id, text="testing")
        await k.delete()
    except:
        await sts.edit(f"**please make your [userbot](t.me/{_bot['username']}) admin in target chat with full permissions**")
        return await bot.stop()
    MESSAGES = []
    DUPLICATE = []
    total=deleted=0
    temp.lock[user_id] = True
    try:
      await sts.edit(Script.DUPLICATE_TEXT.format(total, deleted, "ᴘʀᴏɢʀᴇssɪɴɢ"), reply_markup=CANCEL_BTN)
      async for message in bot.search_messages(chat_id=chat_id, filter="document"):
         if temp.CANCEL.get(user_id) == True:
            await sts.edit(Script.DUPLICATE_TEXT.format(total, deleted, "ᴄᴀɴᴄᴇʟʟᴇᴅ"), reply_markup=COMPLETED_BTN)
            return await bot.stop()
         file = message.document
         file_id = unpack_new_file_id(file.file_id) 
         if file_id in MESSAGES:
            DUPLICATE.append(message.id)
         else:
            MESSAGES.append(file_id)
         total += 1
         if total %10000 == 0:
            await sts.edit(Script.DUPLICATE_TEXT.format(total, deleted, "ᴘʀᴏɢʀᴇssɪɴɢ"), reply_markup=CANCEL_BTN)
         if len(DUPLICATE) >= 100:
            await bot.delete_messages(chat_id, DUPLICATE)
            deleted += 100
            await sts.edit(Script.DUPLICATE_TEXT.format(total, deleted, "ᴘʀᴏɢʀᴇssɪɴɢ"), reply_markup=CANCEL_BTN)
            DUPLICATE = []
      if DUPLICATE:
         await bot.delete_messages(chat_id, DUPLICATE)
         deleted += len(DUPLICATE)
    except Exception as e:
        temp.lock[user_id] = False 
        await sts.edit(f"**ERROR**\n`{e}`")
        return await bot.stop()
    temp.lock[user_id] = False
    await sts.edit(Script.DUPLICATE_TEXT.format(total, deleted, "ᴄᴏᴍᴘʟᴇᴛᴇᴅ"), reply_markup=COMPLETED_BTN)
    await bot.stop()
