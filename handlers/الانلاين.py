import asyncio
from pyrogram import Client, filters
from handlers.restarter import restart
from pyrogram.types import *

@Client.on_message(filters.command("انلاين تفعيل", ["."]) & filters.me)
async def online_now(client: Client, message: Message):
    await message.edit("**- تـم تفعيـل وضـع الانـلاين . . بنجـاح ✓**")
    while True:
        iii = await client.send_message("me", "bruh")
        await client.delete_messages("me", iii.id)
        await asyncio.sleep(45)


@Client.on_message(filters.command("انلاين تعطيل", ["."]) & filters.me)
async def offline_now(client: Client, message: Message):
    await message.edit("**- تـم تعطيـل وضـع الانـلاين . . بنجـاح ✓**\n\n**- جـاري اعـاده تشغيـل البـوت . . انتظـر**")
    await restart(message, restart_type="restart")


