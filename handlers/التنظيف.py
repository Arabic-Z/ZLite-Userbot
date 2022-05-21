from pyrogram import Client, filters
import asyncio
import time
from pyrogram.types import ChatPermissions, Message


@Client.on_message(filters.command("تنظيف", ["."]) & filters.me)  
async def purge(client: Client, message: Message):
    start_time = time.time()
    message_ids = []
    purge_len = 0
    event = await message.edit_text("**- جـاري التنظـيف . . .**")
    me_m =await client.get_me()
    if message.chat.type in ["supergroup", "channel"]:
        me_ = await message.chat.get_member(int(me_m.id))
        if not me_.can_delete_messages:
            await event.edit("**- عـذراً . . ليـس لـديك صـلاحيـة حـذف الرسـائـل هنـا**")
            return
    if not message.reply_to_message:
        await event.edit("**- بالـرد ع رسـالـه لـ حـذف مـابعـدهـا . .**")
        return
    async for msg in client.iter_history(
        chat_id=message.chat.id,
        offset_id=message.reply_to_message.message_id,
        reverse=True,
    ):
        if msg.message_id != message.message_id:
            purge_len += 1
            message_ids.append(msg.message_id)
            if len(message_ids) >= 100:
                await client.delete_messages(
                    chat_id=message.chat.id, message_ids=message_ids, revoke=True
                )
                message_ids.clear()
    if message_ids:
        await client.delete_messages(
            chat_id=message.chat.id, message_ids=message_ids, revoke=True
        )
    end_time = time.time()
    u_time = round(end_time - start_time)
    await event.edit(
        f"**>> تـم التنظيـف . . بنجـاح☑️** \n\n**>> عـدد الرسـائـل المحـذوفـه 🗑:** `{purge_len}` \n**>> الوقـت المستغـرق ⏳:** `{u_time}`",
    )
    await asyncio.sleep(3)
    await event.delete()



@Client.on_message(filters.command("حذف رسائلي", ["."]) & filters.me)  
async def purgeme(client: Client, message: Message):
    msg_text=message.text
    chat_id=message.chat.id
    if " " in msg_text:
        number=msg_text[msg_text.index(" ")+1 : len(msg_text)]
        if(not number.isnumeric()):
            await message.edit_text("**- ادخـل عـدد الرسـائـل . . لـ الحـذف**")
        else:
            number=int(number)
            msg_id=message.message_id - 1
            while number > 0:
                try:
                    print(msg_id)
                    if client.get_messages(chat_id , msg_id).from_user.id == client.get_users("me").id:
                        await client.delete_messages(chat_id , msg_id)
                        print("ZLite")
                        number=number-1
                    msg_id=msg_id-1
                except Exception as e:
                    msg_id=msg_id-1
    else:
        await message.edit_text("**- ادخـل عـدد الرسـائـل . . لـ الحـذف**")
