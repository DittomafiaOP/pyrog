# 𝑪𝒐𝒑𝒚𝒓𝒊𝒈𝒉𝒕 𝑩𝒚 𝑨𝒍𝒕𝒓𝒐𝒏
# 𝑨𝒍𝒍 𝑹𝒊𝒈𝒉𝒕𝒔 𝑹𝒆𝒔𝒆𝒓𝒗𝒆𝒅

from config import SUDO_USERS
from data import GROUP
from pyrogram import Client, filters
from pyrogram.types import Message


__MODULE__ = "Alt"
__HELP__ = """
!join - join public or private group

!leave - leave public or private group
"""


@Client.on_message(filters.command(["join"], ["/", "!", "."]) & filters.user(SUDO_USERS))
async def join(xspam: Client, message: Message):
    alt = message.text.split(" ")
    if len(alt) == 1:
        return await message.reply_text("`Need a chat username or chat-id or invite link to join.`")
    try:
        await xspam.join_chat(alt[1])
        await message.reply_text(f"**Joined ✅**")
    except Exception as ex:
        await message.reply_text(f"**ERROR:** \n\n{str(ex)}")
  
         
@Client.on_message(filters.command(["leave", "remove"], [".", "!", "/"]) & filters.user(SUDO_USERS))
async def leave(xspam: Client, message: Message):
    alt = message.text.split(" ")
    if len(alt) > 1:
        if alt[1] in GROUP:
            return
        try:
           await xspam.leave_chat(alt[1])
           await message.reply_text(f"**Left Successfully ✅**")
        except Exception as ex:
           await message.reply_text(f"**ERROR:** \n\n{str(ex)}")
    else:
        chat = message.chat.id
        ok = message.from_user.id
        if chat == ok:
            return await message.reply_text(f"⚡ ᴜsᴀɢᴇ:\n !leave <chat username or id> or !leave [type in Group for Direct leave]")
        elif chat in GROUP:
              return
        try:
           await xspam.leave_chat(chat)
           await message.reply_text(f"**Left Successfully ✅ **")
        except Exception as ex:
           await message.reply_text(f"**ERROR:** \n\n{str(ex)}")
