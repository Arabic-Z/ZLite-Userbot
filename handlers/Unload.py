import os
import time

from pyrogram import Client, filters
from pyrogram.types import *
from handlers.restarter import restart

from pyrogram.types import Message
module_list = {}




@Client.on_message(filters.command('الغاء تنصيب', ["."]) & filters.me)
async def unloadmod(client: Client, message: Message):
    cmd = message.command
    try:
        if client.long(message) > 1:
            if cmd[1].endswith(".py"):
                module_loc = f"handlers/{cmd[1]}"
            elif not cmd[1].endswith(".py"):
                module_loc = f"handlers/{cmd[1]}.py"
            if os.path.exists(module_loc):
                os.remove(module_loc)
                await message.edit(f"**- تـم الغـاء تنصـيب المـلف .. بـ نجـاح ☑️** {cmd[1]}")
            else:
                await message.edit("Module doesn't exist !")
        else:
            await message.edit("Give me a module name . . .")
    except Exception as e:
        await message.edit(f"**An error has occurred.**\nLog: not found {e}")


@Client.on_message(filters.command(['تنصيب', "install"], ["."]) & filters.me)
async def loadmod(client: Client, message: Message):
    reply = message.reply_to_message
    if not reply:
        return await message.edit("Reply to a python file to install . . .")
    if reply:
        if not reply.document.file_name.endswith(".py"):
            return await message.edit("Only (.py) modules can be installed !!")
        doc_name = reply.document.file_name

        module_loc = f"handlers/{doc_name}"
        await message.edit("Installing module . . .")
        if os.path.exists(module_loc):
            return await message.edit(f"Module `{doc_name}` already exists ! skipping installation !")

        try:
            download_loc = await client.download_media(message=reply, file_name=module_loc)
            if download_loc:
                await message.edit(f"**- تـم تنصـيب المـلف .. بـ نجـاح ☑️** `{doc_name}`")
            else:
                await message.edit(f"Failed to install module {doc_name}")
        except Exception as e:
            await message.edit(f"**An error has occurred.**\nLog: not found {e}")
