# Zed-Thon

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from pyrogram import __version__ as pyro_vr
import asyncio
import time
from pyrogram import filters, Client
from config import SUDO_USERS as SUDO_USER
from main import *
from main import ALIVE_PIC


@Client.on_message(filters.user(SUDO_USER) & filters.command(["تكرار", "deletespam"], [".", "!", "/"]))
async def delspam(client: Client, message: Message):
    zaid = await message.reply_text("**- الاسـتخـدام :**\n /delspam 10 Umm")
    quantity = message.command[1]
    spam_text = ' '.join(message.command[2:])
    quantity = int(quantity)
    await message.delete()
    for i in range(quantity):
        await zaid.delete()
        msg = await client.send_message(message.chat.id, spam_text)
        await asyncio.sleep(0.1)
        await msg.delete()
        await asyncio.sleep(0.1)


@Client.on_message(filters.user(SUDO_USER) & filters.command(["سبامر", "سبام"], [".", "!", "/"]))
async def suspam(client: Client, message: Message):
    zaid = await message.reply_text("**- الاسـتخـدام :**\n /spam 10 Umm")
    quantity = message.command[1]
    spam_text = ' '.join(message.command[2:])
    quantity = int(quantity)

    if message.reply_to_message:
        reply_to_id = message.reply_to_message.message_id
        for _ in range(quantity):
            await client.send_message(message.chat.id, spam_text,
                                      reply_to_message_id=reply_to_id)
            await asyncio.sleep(0.15)
        return

    for _ in range(quantity):
        await zaid.delete()
        await client.send_message(message.chat.id, spam_text)
        await asyncio.sleep(0.15)


@Client.on_message(filters.user(SUDO_USER) & filters.command(["تكرار_سريع"], [".", "!", "/"]))
async def spspam(client: Client, message: Message):
    zaid = await message.reply_text("**- الاسـتخـدام :**\n /fastspam 10 Umm")
    quantity = message.command[1]
    spam_text = ' '.join(message.command[2:])
    quantity = int(quantity)
    
    if message.reply_to_message:
        reply_to_id = message.reply_to_message.message_id
        for _ in range(quantity):
            await client.send_message(message.chat.id, spam_text,
                                      reply_to_message_id=reply_to_id)
            await asyncio.sleep(0.002)
        return
    
    for _ in range(quantity):
        await zaid.delete()
        await client.send_message(message.chat.id, spam_text)
        await asyncio.sleep(0.002)



@Client.on_message(filters.user(SUDO_USER) & filters.command(["تكرار_بطيئ", "delayspam"], [".", "!", "/"]))
async def sperm(client: Client, message: Message):
    zaid = await message.reply_text("**- الاسـتخـدام :**\n /slowspam 10 Umm")
    quantity = message.command[1]
    spam_text = ' '.join(message.command[2:])
    quantity = int(quantity)

    if message.reply_to_message:
        reply_to_id = message.reply_to_message.message_id
        for _ in range(quantity):
            await client.send_message(message.chat.id, spam_text,
                                      reply_to_message_id=reply_to_id)
            await asyncio.sleep(0.9)
        return

    for _ in range(quantity):
        await zaid.delete()
        msg = await client.send_message(message.chat.id, spam_text)
        await asyncio.sleep(0.9)







@Client.on_message(filters.user(SUDO_USER) & filters.command(["سبام_ملصق", "stkspam", "spamstk", "stickerspam"], [".", "!", "/"]))
async def pussy(client: Client, message: Message):
    if not message.reply_to_message:
        await message.edit_text("**reply to a sticker with amount you want to spam**")
        return
    if not message.reply_to_message.sticker:
        await message.edit_text(text="**reply to a sticker with amount you want to spam**")
        return
    else:
        i=0
        times = message.command[1]
        if message.chat.type in ["supergroup", "group"]:
            for i in range(int(times)):
                sticker=message.reply_to_message.sticker.file_id
                await client.send_sticker(
                    message.chat.id,
                    sticker,
                )
                await asyncio.sleep(0.10)

        if umm.chat.type == "private":
            for i in range(int(times)):
                sticker=message.reply_to_message.sticker.file_id
                await client.send_sticker(
                    message.chat.id, sticker
                )
                await asyncio.sleep(0.10)



@Client.on_message(filters.user(SUDO_USER) & filters.command(["فحص", "بوت"], [".", "!", "/"]))
async def awake(client: Client, e: Message):
    ids = 0
    try:
        if bot:
            ids += 1
        if bot1:
            ids += 1
        if bot2:
            ids += 1
        if bot3:
            ids += 1
        if bot4:
            ids += 1
        if bot5:
            ids += 1
        if bot6:
            ids += 1
        if bot7:
            ids += 1
        if bot8:
            ids += 1
        if bot9:
            ids += 1
        if bot:
            ids += 1
        if bot11:
            ids += 1
        if bot12:
            ids += 1
        if bot13:
            ids += 1
        if bot14:
            ids += 1
        if bot15:
            ids += 1
        if bot16:
            ids += 1
        if bot17:
            ids += 1
        if bot18:
            ids += 1
        if bot19:
            ids += 1
        if bot20:
            ids += 1
        if bot21:
            ids += 1
        if bot22:
            ids += 1
        if bot23:
            ids += 1
        if bot24:
            ids += 1
        if bot25:
            ids += 1
        if bot26:
            ids += 1
        if bot27:
            ids += 1
        if bot28:
            ids += 1
        if bot29:
            ids += 1
        if bot30:
            ids += 1
        if bot31:
            ids += 1
        if bot32:
            ids += 1
        if bot33:
            ids += 1
        if bot34:
            ids += 1
        if bot35:
            ids += 1
        if bot36:
            ids += 1
        if bot37:
            ids += 1
        if bot38:
            ids += 1
        if bot39:
            ids += 1
        if bot40:
            ids += 1
        if bot41:
            ids += 1
        if bot42:
            ids += 1
        if bot43:
            ids += 1
        if bot44:
            ids += 1
        if bot45:
            ids += 1
        if bot46:
            ids += 1
        if bot47:
            ids += 1
        if bot48:
            ids += 1
        if bot49:
            ids += 1
        if bot50:
            ids += 1
        Alive_msg = f"** بـوت  زدثــون 𝙕𝞝𝘿𝙏𝙃𝙊𝙉  يعمـل .. بنجـاح ☑️ 𓆩 **\n"
        Alive_msg += f"ٴ◈ ━━━━━━ ◆ ━━━━━━ ◈ \n"
        Alive_msg += f"**✥┊ قاعدۿ البيانات :** تعمل بنـجاح\n"
        Alive_msg += f"**✥┊ إصـدار البـايثون :** 3.10.2\n"
        Alive_msg += f"**✥┊ إصـدار زد_لايـت :** 1.1\n"
        Alive_msg += f"**✥┊ إصـدار بايـروجـرام :**`{pyro_vr}` \n"
        Alive_msg += f"**✥┊ الايـدي :**`{ids}` \n"
        Alive_msg += f"**✥┊ قنـاة السـورس :** [اضغـط هنـا](https://t.me/ZedThon) \n"
        Alive_msg += f"ٴ◈ ━━━━━━ ◆ ━━━━━━ ◈ \n\n"
        await e.reply_text(photo=ALIVE_PIC, caption=Alive_msg)
    except Exception as lol:         
        Alive_msg = f"** بـوت  زدثــون 𝙕𝞝𝘿𝙏𝙃𝙊𝙉  يعمـل .. بنجـاح ☑️ 𓆩 **\n"
        Alive_msg += f"ٴ◈ ━━━━━━ ◆ ━━━━━━ ◈ \n"
        Alive_msg += f"**✥┊ قاعدۿ البيانات :** تعمل بنـجاح\n"
        Alive_msg += f"**✥┊ إصـدار البـايثون :** 3.10.2\n"
        Alive_msg += f"**✥┊ إصـدار زد_لايـت :** 1.1\n"
        Alive_msg += f"**✥┊ إصـدار بايـروجـرام :**`{pyro_vr}` \n"
        Alive_msg += f"**✥┊ الايـدي :**`{ids}` \n"
        Alive_msg += f"**✥┊ قنـاة السـورس :** [اضغـط هنـا](https://t.me/ZedThon) \n"
        Alive_msg += f"ٴ◈ ━━━━━━ ◆ ━━━━━━ ◈ \n\n"
        await e.reply_photo(photo=ALIVE_PIC, caption=Alive_msg)


@Client.on_message(filters.command("بنك", [".", "!"]) & filters.user(SUDO_USER))
async def pingme(client: Client, message: Message):
    start = time.time()
    reply = await message.reply_text("...")
    delta_ping = time.time() - start
    await reply.edit_text(f"🎉 🇵 🇴 🇳 🇬 !\n\n♡︎ `{delta_ping * 1000:.3f}` 𝗺𝘀 ♡︎")




@Client.on_message(filters.command(["اذاعه", "br", "chatbroadcast"], [".", "!", "."]) & filters.user(SUDO_USER))
async def chat_broadcast(c: Client, m: Message):
    if m.reply_to_message:
        msg = m.reply_to_message.text.markdown
    else:
        await m.reply_text("Reply to a message to broadcast it")
        return

    exmsg = await m.reply_text("Started broadcasting!")
    err_str, done_broadcast = "", 0

    async for dialog in c.iter_dialogs():
          try:
                await c.send_message(dialog.chat.id, msg, disable_web_page_preview=True)
                done_broadcast += 1
                await asyncio.sleep(0.1)
          except Exception as e:
            await m.reply_text(f"[Broadcast] {dialog.chat.id} {e}")


ZED_Help = f"𓆰 [𝗦𝗢𝗨𝗥𝗖𝗘 𝙕𝞝𝘿 - قائمــة الاوامــر العــامــه](t.me/ZEDthon) 𓆪\n"
ZED_Help += f"◐━─━─━─━─**𝙕𝞝𝘿**─━─━─━─━◐\n\n"
ZED_Help += f"**⌔╎مـرحبـاً عـزيـزي اضغـط ع الامـر لـ النسـخ - ملاحظـه : ضـع نقطه (.) بداية كل امـر :**\n\n"
ZED_Help += f" `.م1`**   ➪ اوامـر البحـث والتحميــل**\n"
ZED_Help += f" `.م2`**   ➪ اوامـر البــوت**\n"
ZED_Help += f" `.م3`**   ➪ اوامـر الـوقتــي**\n"
ZED_Help += f" `.م4`**   ➪ اوامـر المجمــوعــه¹**\n"
ZED_Help += f" `.م5`**   ➪ اوامـر المجمــوعــه²**\n"
ZED_Help += f" `.م6`**   ➪ اوامـر الحســاب**\n"
ZED_Help += f" `.م7`**   ➪ اوامـر الميـديـا والصيــغ**\n"
ZED_Help += f" `.م8`**   ➪ اوامـر الفــارات**\n"
ZED_Help += f" `.م9`**   ➪ اوامـر الــردود والتــرحيب**\n"
ZED_Help += f" `.م10`** ➪ اوامـر التســليـه والالـعــاب**\n\n"
ZED_Help += f"◐━─━─━─━─**𝙕𝞝𝘿**─━─━─━─━◐\n"
ZED_Help += f" 𓆩 [𝗦𝗢𝗨𝗥𝗖𝗘 𝙕𝞝𝘿 - قنـاة السـورس](t.me/ZEDthon) 𓆪\n"

@Client.on_message(filters.user(SUDO_USER) & filters.command(["help", "الاوامر"], [".", "!", "/"]))
async def helpsx(client: Client, e: Message):
    ids = 0
    try:
        if bot:
            ids += 1
        if bot1:
            ids += 1
        if bot2:
            ids += 1
        Alive_msg = f"** بـوت  زدثــون 𝙕𝞝𝘿𝙏𝙃𝙊𝙉  يعمـل .. بنجـاح ☑️ 𓆩 **\n"
        Alive_msg += f"ٴ◈ ━━━━━━ ◆ ━━━━━━ ◈ \n"
        Alive_msg += f"**✥┊ قاعدۿ البيانات :** تعمل بنـجاح\n"
        Alive_msg += f"**✥┊ إصـدار البـايثون :** 3.10.2\n"
        Alive_msg += f"**✥┊ إصـدار زد_لايـت :** 1.1\n"
        Alive_msg += f"**✥┊ إصـدار بايـروجـرام :**`{pyro_vr}` \n"
        Alive_msg += f"**✥┊ الايـدي :**`{ids}` \n"
        Alive_msg += f"**✥┊ قنـاة السـورس :** [اضغـط هنـا](https://t.me/ZedThon) \n"
        Alive_msg += f"ٴ◈ ━━━━━━ ◆ ━━━━━━ ◈ \n\n"
        await e.reply_text(photo=ALIVE_PIC, caption=ZED_Help)
    except Exception as lol:         
        Alive_msg = f"** بـوت  زدثــون 𝙕𝞝𝘿𝙏𝙃𝙊𝙉  يعمـل .. بنجـاح ☑️ 𓆩 **\n"
        Alive_msg += f"ٴ◈ ━━━━━━ ◆ ━━━━━━ ◈ \n"
        Alive_msg += f"**✥┊ قاعدۿ البيانات :** تعمل بنـجاح\n"
        Alive_msg += f"**✥┊ إصـدار البـايثون :** 3.10.2\n"
        Alive_msg += f"**✥┊ إصـدار زد_لايـت :** 1.1\n"
        Alive_msg += f"**✥┊ إصـدار بايـروجـرام :**`{pyro_vr}` \n"
        Alive_msg += f"**✥┊ الايـدي :**`{ids}` \n"
        Alive_msg += f"**✥┊ قنـاة السـورس :** [اضغـط هنـا](https://t.me/ZedThon) \n"
        Alive_msg += f"ٴ◈ ━━━━━━ ◆ ━━━━━━ ◈ \n\n"
        await e.reply_photo(photo=ALIVE_PIC, caption=ZED_Help)




@Client.on_message(filters.command('join', [".", "!"]) & filters.user(SUDO_USER))
async def fuck(client: Client, message: Message):
    zaid = message.text[6:]
    count = 0
    if not zaid:
        return await message.reply_text("Need a chat username or invite link to join.")
    if zaid.isnumeric():
        return await message.reply_text("Can't join a chat with chat id. Give username or invite link.")
    try:
        await client.join_chat(zaid)
        await message.reply_text(f"**Joined**")
    except Exception as ex:
        await message.reply_text(f"**ERROR:** \n\n{str(ex)}")


@Client.on_message(filters.command('leave', [".", "!"]) & filters.user(SUDO_USER))
async def leftfuck(client: Client, message: Message):
    zaid = message.text[6:]
    count = 0
    if not zaid:
        return await message.reply_text("Need a chat username or invite link to leave.")
    if zaid.isnumeric():
        return await message.reply_text("Can't leave a chat with chat id. Give username or invite link.")
    try:
        await client.leave_chat(zaid)
        await message.reply_text(f"**Lefted**")
    except Exception as ex:
        await message.reply_text(f"**ERROR:** \n\n{str(ex)}")
