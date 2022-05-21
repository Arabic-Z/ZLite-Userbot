import html

from pyrogram import filters, Client
from pyrogram.types import Message

from helpers.parser import mention_html, mention_markdown

__MODULE__ = "Admin List"
__HELP__ = """
لـ جـلب قوائـم المشـرفيـن/البـوتـات أو  عمـل تاك للكل او الإبلاغ عن شخص مـا بعمـل تاك للادمنيـه ، او حذف الحسابات المحذوفه
يرجى ملاحظة أن المشـرفين سوف يعطـوك حظـراً فوريـاً اذا كررت هذه الاوامـر بكثـره بـدون داعـي . . .

──「 **قائمـة المشـرفيـن** 」──
-> `.المشرفين`
-> `.الادمنيه`
لـ جلـب قائمـه بـ مشـرفيـن الكـروب

──「 **التـاكـات** 」──
-> `.تاك للمشرفين`
-> `.تاك للادمنيه`
-> `تاك للكل`
لـ عمـل تـاك للادمنيـه او تـاك للكـل

──「 **قائمـة البـوتـات** 」──
-> `.البوتات`
لـ جلـب قائمـه بـ بوتـات المجمـوعـه

──「 **حـذف الحسـابـات المحـذوفـه** 」──
-> `المحذوفين`
لـ تنظيـف الكـروب مـن الحسـابات المحـذوفـه

"""


@Client.on_message(filters.me & filters.command(["المشرفين", "الادمنيه"], ["."]))
async def adminlist(client: Client, message: Message):
    replyid = None
    toolong = False
    if len(message.text.split()) >= 2:
        chat = message.text.split(None, 1)[1]
        grup = await client.get_chat(chat)
    else:
        chat = message.chat.id
        grup = await client.get_chat(chat)
    if message.reply_to_message:
        replyid = message.reply_to_message.message_id
    alladmins = client.iter_chat_members(chat, filter="administrators")
    creator = []
    admin = []
    badmin = []
    async for a in alladmins:
        try:
            nama = a.user.first_name + " " + a.user.last_name
        except:
            nama = a.user.first_name
        if nama is None:
            nama = "☠️ الحسـابـات المحـذوفـه"
        if a.status == "administrator":
            if a.user.is_bot:
                badmin.append(mention_markdown(a.user.id, nama))
            else:
                admin.append(mention_markdown(a.user.id, nama))
        elif a.status == "creator":
            creator.append(mention_markdown(a.user.id, nama))
    admin.sort()
    badmin.sort()
    totaladmins = len(creator) + len(admin) + len(badmin)
    teks = "𓆩 𝑺𝑶𝑼𝑹𝑪𝑬 𝙕𝞝𝘿𝙏𝙃𝙊𝙉 𝑮𝑹𝑶𝑼𝑷 𝑫𝑨𝑻𝑨 𓆪\n** ⪼ المشـرفـون فـي {} :** \n".format(grup.title)
    teks += "╒═══「 المـالـك 」\n"
    for x in creator:
        teks += "│ • {}\n".format(x)
        if len(teks) >= 4096:
            await message.reply(message.chat.id, teks, reply_to_message_id=replyid)
            teks = ""
            toolong = True
    teks += "╞══「 {} الاعضـاء المشـرفـون 」\n".format(len(admin))
    for x in admin:
        teks += "│ • {}\n".format(x)
        if len(teks) >= 4096:
            await message.reply(message.chat.id, teks, reply_to_message_id=replyid)
            teks = ""
            toolong = True
    teks += "╞══「 {} البـوتـات المشـرفـون 」\n".format(len(badmin))
    for x in badmin:
        teks += "│ • {}\n".format(x)
        if len(teks) >= 4096:
            await message.reply(message.chat.id, teks, reply_to_message_id=replyid)
            teks = ""
            toolong = True
    teks += "╘══「 اجمـالـي المشـرفيـن هـو {}  」".format(totaladmins)
    if toolong:
        await message.reply(message.chat.id, teks, reply_to_message_id=replyid)
    else:
        await message.edit(teks)


@Client.on_message(filters.command(["المحذوفين", "الحسابات المحذوفه"], ["."]) & filters.me)
async def kickdel_cmd(client: Client, message: Message):
    await message.edit("<b>Kicking deleted accounts...</b>")
    # noinspection PyTypeChecker
    values = [
        await message.chat.ban_member(user.user.id, int(time()) + 31)
        for member in await message.chat.get_members()
        if member.user.is_deleted
    ]
    await message.edit(f"<b>❈╎تـم حـذف  {len(values)}  مـن الحسـابات المحذوفـة هنـا ✓</b>")


@Client.on_message(filters.me & filters.command(["تاك للادمنيه", "تاك للمشرفين", "report"], ["."]))
async def report_admin(client: Client, message: Message):
    await message.delete()
    if len(message.text.split()) >= 2:
        text = message.text.split(None, 1)[1]
    else:
        text = None
    grup = await client.get_chat(message.chat.id)
    alladmins = client.iter_chat_members(message.chat.id, filter="administrators")
    admin = []
    async for a in alladmins:
        if a.status == "administrator" or a.status == "creator":
            if not a.user.is_bot:
                admin.append(mention_html(a.user.id, "\u200b"))
    if message.reply_to_message:
        if text:
            teks = '{}'.format(text)
        else:
            teks = '{} reported to admins.'.format(
                mention_html(message.reply_to_message.from_user.id, message.reply_to_message.from_user.first_name))
    else:
        if text:
            teks = '{}'.format(html.escape(text))
        else:
            teks = "Calling admins in {}.".format(grup.title)
    teks += "".join(admin)
    if message.reply_to_message:
        await client.send_message(message.chat.id, teks, reply_to_message_id=message.reply_to_message.message_id,
                                  parse_mode="html")
    else:
        await client.send_message(message.chat.id, teks, parse_mode="html")


@Client.on_message(filters.me & filters.command(["all", "تاك للكل"], "."))
async def tag_all_users(client: Client, message: Message):
    await message.delete()
    if len(message.text.split()) >= 2:
        text = message.text.split(None, 1)[1]
    else:
        text = "**ههها اخوان**"
    kek = client.iter_chat_members(message.chat.id)
    async for a in kek:
        if not a.user.is_bot:
            text += mention_html(a.user.id, "\u200b")
    if message.reply_to_message:
        await client.send_message(message.chat.id, text, reply_to_message_id=message.reply_to_message.message_id,
                                  parse_mode="html")
    else:
        await client.send_message(message.chat.id, text, parse_mode="html")


@Client.on_message(filters.me & filters.command(["البوتات"], ["."]))
async def get_list_bots(client: Client, message: Message):
    replyid = None
    if len(message.text.split()) >= 2:
        chat = message.text.split(None, 1)[1]
        grup = await client.get_chat(chat)
    else:
        chat = message.chat.id
        grup = await client.get_chat(chat)
    if message.reply_to_message:
        replyid = message.reply_to_message.message_id
    getbots = client.iter_chat_members(chat)
    bots = []
    async for a in getbots:
        try:
            nama = a.user.first_name + " " + a.user.last_name
        except:
            nama = a.user.first_name
        if nama is None:
            nama = "☠️ الحسـابـات المحـذوفـه"
        if a.user.is_bot:
            bots.append(mention_markdown(a.user.id, nama))
    teks = "𓆩 𝑺𝑶𝑼𝑹𝑪𝑬 𝙕𝞝𝘿𝙏𝙃𝙊𝙉 𝑮𝑹𝑶𝑼𝑷 𝑫𝑨𝑻𝑨 𓆪\n**⪼ البوتـات فـي {}  :**\n".format(grup.title)
    teks += "╒═══「 البـوتـات 」\n"
    for x in bots:
        teks += "│ • {}\n".format(x)
    teks += "╘══「 اجمـالـي البـوتـات هـو {}  」".format(len(bots))
    if replyid:
        await client.send_message(message.chat.id, teks, reply_to_message_id=replyid)
    else:
        await message.edit(teks)
