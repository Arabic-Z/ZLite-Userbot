import asyncio
from datetime import datetime
from time import sleep

from pyrogram import filters, Client
from pyrogram.raw import functions
from pyrogram.types import Message, User
from pyrogram.errors import PeerIdInvalid


from helpers.PyroHelpers import ReplyCheck
from handlers.help import add_command_help

WHOIS = (
    "**╮•⎚ مـعلومات الـشخص مـن بـوت زدثـون**\n"
    "**ٴ════════════════ **\n"
    '**•❃ | الاسـم    ⇦ ** `{full_name}`\n'
    "**•❃ | الايـدي   ⇦ ** `{user_id}`\n"
    "**•❃ |الحسـاب ⇦ ** [{full_name}](tg://user?id={user_id})\n"
    "**•❃ | المعـرف  ⇦ ** {username}\n"
    "**•❃ | الصـور   ⇦ ** `{pic_count}`\n"
    "**•❃ | الـمجموعات المشتـركة ⇦ ** `{common_groups}`\n"
    "**•❃ | البايـو    ⇦ ** `{bio}`**\n"
    "**ٴ════════════════ **\n"
    "** 𓆩 𝙎𝙊𝙐𝙍𝘾𝞝 𝙕𝞝𝘿 𓆪 ** - @ZedThon "
)

WHOIS_PIC = (
    "**╮•⎚ مـعلومات الـشخص مـن بـوت زدثـون**\n"
    "**ٴ════════════════ **\n"
    '**•❃ | الاسـم    ⇦ ** `{full_name}`\n'
    "**•❃ | الايـدي   ⇦ ** `{user_id}`\n"
    "**•❃ |الحسـاب ⇦ ** [{full_name}](tg://user?id={user_id})\n"
    "**•❃ | المعـرف  ⇦ ** {username}\n"
    "**•❃ | الصـور   ⇦ ** `{pic_count}`\n"
    "**•❃ | الـمجموعات المشتـركة ⇦ ** `{common_groups}`\n"
    "**•❃ | البايـو    ⇦ ** `{bio}`**\n"
    "**ٴ════════════════ **\n"
    "** 𓆩 𝙎𝙊𝙐𝙍𝘾𝞝 𝙕𝞝𝘿 𓆪 ** - @ZedThon "
)


def LastOnline(user: User):
    if user.is_bot:
        return ""
    elif user.status == "recently":
        return "Recently"
    elif user.status == "within_week":
        return "Within the last week"
    elif user.status == "within_month":
        return "Within the last month"
    elif user.status == "long_time_ago":
        return "A long time ago :("
    elif user.status == "online":
        return "Currently Online"
    elif user.status == "offline":
        return datetime.fromtimestamp(user.last_online_date).strftime(
            "%a, %d %b %Y, %H:%M:%S"
        )


async def GetCommon(bot: Client, get_user):
    common = await bot.send(
        functions.messages.GetCommonChats(
            user_id=await bot.resolve_peer(get_user), max_id=0, limit=0
        )
    )
    return common


def FullName(user: User):
    return user.first_name + " " + user.last_name if user.last_name else user.first_name


def ProfilePicUpdate(user_pic):
    return datetime.fromtimestamp(user_pic[0].date).strftime("%d.%m.%Y, %H:%M:%S")


@Client.on_message(filters.command(["ايدي", "ا"], [".", ""]) & filters.me)
async def who_is(bot: Client, message: Message):
    cmd = message.command
    if not message.reply_to_message and len(cmd) == 1:
        get_user = message.from_user.id
    elif message.reply_to_message and len(cmd) == 1:
        get_user = message.reply_to_message.from_user.id
    elif len(cmd) > 1:
        get_user = cmd[1]
        try:
            get_user = int(cmd[1])
        except ValueError:
            pass
    try:
        user = await bot.get_users(get_user)
    except PeerIdInvalid:
        await message.edit("**- لـم استطـع العثــور ع الشخــص**")
        await asyncio.sleep(2)
        await message.delete()
        return

    user_details = await bot.get_chat(get_user)
    bio = user_details.bio
    user_pic = await bot.get_profile_photos(user.id)
    pic_count = await bot.get_profile_photos_count(user.id)
    common = await GetCommon(bot, user.id)

    if not user.photo:
        await message.edit(
            WHOIS.format(
                full_name=FullName(user),
                user_id=user.id,
                first_name=user.first_name,
                last_name=user.last_name if user.last_name else "",
                username=user.username if user.username else "",
                last_online=LastOnline(user),
                common_groups=len(common.chats),
                pic_count=pic_count,
                bio=bio if bio else "لا يـوجـد",
            ),
            disable_web_page_preview=True,
        )
    elif user.photo:
        await bot.send_photo(
            message.chat.id,
            user_pic[0].file_id,
            caption=WHOIS_PIC.format(
                full_name=FullName(user),
                user_id=user.id,
                first_name=user.first_name,
                last_name=user.last_name if user.last_name else "",
                username=user.username if user.username else "",
                last_online=LastOnline(user),
                pic_count=pic_count,
                common_groups=len(common.chats),
                bio=bio if bio else "لا يـوجـد",
                profile_pic_update=ProfilePicUpdate(user_pic),
            ),
            reply_to_message_id=ReplyCheck(message),
        )

        await message.delete()


add_command_help(
    "ايدي",
    [
        [
            ".ايدي",
            "Finds out who the person is. Reply to message sent by the person"
            "you want information from and send the command. Without the dot also works.",
        ]
    ],
)
