from pyrogram import filters, Client
from pyrogram.types import *
from main import *
from handlers.help import *


@Client.on_message(filters.me & filters.command(["خاص", "dm"], [".", "!", "/"]))
async def dm(client: Client, message: Message):
    zaid = await message.reply_text("**- الاسـتخـدام :**\n .خاص @username Umm")
    quantity = 1
    inp = message.text.split(None, 2)[1]
    user = await client.get_chat(inp)
    spam_text = ' '.join(message.command[2:])
    quantity = int(quantity)

    if message.reply_to_message:
        reply_to_id = message.reply_to_message.message_id
        for _ in range(quantity):
            await zaid.edit("**- تم الارسـال للخـاص .. بنجـاح** ✅")
            await client.send_message(user.id, spam_text,
                                      reply_to_message_id=reply_to_id)
            await asyncio.sleep(0.15)
        return

    for _ in range(quantity):
        await client.send_message(user.id, spam_text)
        await zaid.edit("**- تم الارسـال للخـاص .. بنجـاح** ✅")
        await asyncio.sleep(0.15)

@Client.on_message(filters.user(SUDO_USERS) & filters.command(["خاص", "dm"], [".", "!", "/"]))
async def dmm(client: Client, message: Message):
    zaid = await message.reply_text("**- الاسـتخـدام :**\n .خاص @username Umm")
    quantity = 1
    inp = message.text.split(None, 2)[1]
    user = await client.get_chat(inp)
    spam_text = ' '.join(message.command[2:])
    quantity = int(quantity)

    if message.reply_to_message:
        reply_to_id = message.reply_to_message.message_id
        for _ in range(quantity):
            await zaid.edit("**- تم الارسـال للخـاص .. بنجـاح** ✅")
            await client.send_message(user.id, spam_text,
                                      reply_to_message_id=reply_to_id)
            await asyncio.sleep(0.15)
        return

    for _ in range(quantity):
        await client.send_message(user.id, spam_text)
        await zaid.edit("**- تم الارسـال للخـاص .. بنجـاح** ✅")
        await asyncio.sleep(0.15)

add_command_help(
    "للخاص",
    [
        [".خاص", "Give a Message to Dm (ex: `.خاص @Timesisnotwaiting Hii`."],
        ["/خاص", "Give a message to Dm (Sudo-Users)."],
    ],
)
