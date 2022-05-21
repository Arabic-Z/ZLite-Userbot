import os
import zipfile
import wget
import shutil
from pyrogram import Client, filters
from pyrogram.types import Message
from main import SUDO_USERS


async def restart(message: Message, restart_type):
    if restart_type == "update":
        text = "1"
    else:
        text = "2"
    try:
        await os.execvp(
            "python3",
            [
                "python3",
                "./main.py",
                f"{message.chat.id}",
                f"{message.id}",
                f"{text}",
            ],
        )
    except:
        await os.execvp(
            "python",
            [
                "python",
                "./main.py",
                f"{message.chat.id}",
                f"{message.id}",
                f"{text}",
            ],
        )


# Restart
@Client.on_message(filters.command(["اعاده تشغيل", "restart"], ["."]) & filters.me)
@Client.on_message(filters.user(SUDO_USERS) & filters.command(["اعاده تشغيل", "restart"], [".", "!"]))
async def restart_get(client: Client, message: Message):
    try:
        zaid = await message.reply_text("**⌔∮ يتـم الان اعـادة تشغيـل بـوت زدثــون لايـت قـد يستغـرق الامـر 1-2 دقيقـه ▬▭ ...**")
        await restart(message, restart_type="restart")
    except:
        await zaid.edit_text("**An error occured...**")


# Update
@Client.on_message(filters.command(['تحديث', 'update'], ["."]) & filters.me)
async def update(client: Client, message: Message):
    try:
        await message.edit('𓆰 𝗦𝗢𝗨𝗥𝗖𝗘 𝙕𝞝𝘿 - 𝑼𝑷𝑫𝑨𝑻𝑬 𝑴𝑺𝑮 𓆪\n 𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n**⪼ يتـم تحـديث بـوت زدثــون انتظـر 🌐..𓆰،**')
        link = "https://github.com/ZThon-Ar/ZLite-Userbot/archive/refs/heads/main.zip"
        wget.download(link, 'temp/archive.zip')

        with zipfile.ZipFile("temp/archive.zip", "r") as zip_ref:
            zip_ref.extractall("temp/")
        os.remove("temp/archive.zip")

        shutil.make_archive("temp/archive", "zip", "temp/ZLite-Userbot-main/")

        with zipfile.ZipFile("temp/archive.zip", "r") as zip_ref:
            zip_ref.extractall(".")
        os.remove("temp/archive.zip")

        await message.edit('𓆰 𝗦𝗢𝗨𝗥𝗖𝗘 𝙕𝞝𝘿 - 𝑼𝑷𝑫𝑨𝑻𝑬 𝑴𝑺𝑮 𓆪\n𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n**⪼ تم التحديث بنجاح ✅**\n ** جارٍ إعادة تشغيل بوت زد ثـون ، انتظر 𓆰.**')
        await restart(message, restart_type="update")
    except:
        await message.edit(f"**An error occured...**")



