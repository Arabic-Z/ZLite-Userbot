from pyrogram import Client, filters
import asyncio
import time
from emoji import get_emoji_regexp
from config import SUDO_USERS
from pyrogram.types import ChatPermissions, Message
from pyrogram.errors import (
    UsernameInvalid,
    ChatAdminRequired,
    PeerIdInvalid,
    UserIdInvalid,
    UserAdminInvalid,
    FloodWait,
)
from handlers.help import add_command_help
from handlers.help import *

@Client.on_message(filters.group & filters.command("رفع مشرف", ["."]) & filters.me)  
async def promotte(client: Client, message: Message):
  if message.chat.type in ["group", "supergroup"]:
    cmd = message.command
    me_m= message.from_user
    me_ = await message.chat.get_member(int(me_m.id))
    if not me_.can_promote_members:
        await message.edit("`Boss, You Don't Have Promote Permission!`")
        return
    can_promo = True
    if can_promo:
            try:
                if message.reply_to_message:
                    user_id = message.reply_to_message.from_user.id
                    custom_rank = get_emoji_regexp().sub("", " ".join(cmd[1:]))
                else:
                    usr = await client.get_users(cmd[1])
                    custom_rank = get_emoji_regexp().sub("", " ".join(cmd[2:]))
                    user_id = usr.id
            except IndexError:
                await message.delete()
                return

            if user_id:
                try:
                    await client.promote_chat_member(
                        message.chat.id,
                        user_id,
                        can_change_info=True,
                        can_delete_messages=True,
                        can_restrict_members=True,
                        can_invite_users=True,
                        can_pin_messages=True,
                    )

                    await asyncio.sleep(2)
                    await client.set_administrator_title(
                        message.chat.id, user_id, custom_rank
                  )
                    await message.edit_text("promoted due to bribe")
                    await asyncio.sleep(5)
                    await message.delete()
                except UsernameInvalid:
                    await message.edit_text("user_invalid")
                    await asyncio.sleep(5)
                    await message.delete()
                    return
                except PeerIdInvalid:
                    await message.edit_text("peer_invalid")
                    await asyncio.sleep(5)
                    await message.delete()
                    return
                except UserIdInvalid:
                    await message.edit_text("id_invalid")
                    await asyncio.sleep(5)
                    await message.delete()
                    return

                except ChatAdminRequired:
                    await message.edit_text("**❈╎عزيزي لسـت مشرفـاً في هـذه المجموعـه **")
                    await asyncio.sleep(5)
                    await message.delete()
                    return

                except Exception as e:
                    await message.edit_text(f"**Log:** `{e}`")
                    return

    else:
            await message.edit_text("**❈╎عزيزي لسـت مشرفـاً في هـذه المجموعـه **")
            await asyncio.sleep(5)
            await message.delete()
  else:
        await message.delete()


@Client.on_message(filters.group & filters.command("تنزيل مشرف", ["."]) & filters.me)  
async def demote(client: Client, message: Message):
  if message.chat.type in ["group", "supergroup"]:
    cmd = message.command
    me_m= message.from_user
    me_ = await message.chat.get_member(int(me_m.id))
    if not me_.can_promote_members:
        await message.edit("`Boss, You Don't Have Promote Permission!`")
        return
    can_promo = True
    if can_promo:
            try:
                if message.reply_to_message:
                    user_id = message.reply_to_message.from_user.id
                    custom_rank = get_emoji_regexp().sub("", " ".join(cmd[1:]))
                else:
                    usr = await client.get_users(cmd[1])
                    custom_rank = get_emoji_regexp().sub("", " ".join(cmd[2:]))
                    user_id = usr.id
            except IndexError:
                await message.delete()
                return

            if user_id:
                try:
                    await client.promote_chat_member(
             message.chat.id,
             user_id,
            is_anonymous=False,
            can_change_info=False,
            can_post_messages=False,
            can_edit_messages=False,
            can_delete_messages=False,
            can_restrict_members=False,
            can_invite_users=False,
            can_pin_messages=False,
            can_promote_members=False,)
                    await message.edit_text("demoted due to corruption")
                    await asyncio.sleep(5)
                    await message.delete()
                except UsernameInvalid:
                    await message.edit_text("user_invalid")
                    await asyncio.sleep(5)
                    await message.delete()
                    return
                except PeerIdInvalid:
                    await message.edit_text("peer_invalid")
                    await asyncio.sleep(5)
                    await message.delete()
                    return
                except UserIdInvalid:
                    await message.edit_text("id_invalid")
                    await asyncio.sleep(5)
                    await message.delete()
                    return

                except ChatAdminRequired:
                    await message.edit_text("**❈╎عزيزي لسـت مشرفـاً في هـذه المجموعـه **")
                    await asyncio.sleep(5)
                    await message.delete()
                    return

                except Exception as e:
                    await message.edit_text(f"**Log:** `{e}`")
                    return

    else:
            await message.edit_text("**❈╎عزيزي لسـت مشرفـاً في هـذه المجموعـه **")
            await asyncio.sleep(5)
            await message.delete()
  else:
        await message.delete()



@Client.on_message(filters.group & filters.command(["ضع صوره", "وضع صوره"], ["."]) & filters.me)  
async def set_chat_photo(client: Client, message: Message):
    msg_id=message.message_id
    chat_id=message.chat.id
    zuzu=await client.get_chat_member(chat_id , "me")
    can_change_admin=zuzu.can_change_info
    can_change_member=message.chat.permissions.can_change_info
    if not (can_change_admin or can_change_member):
        await message.edit_text("**- انت لا تملك صلاحيات هنا**")
    if message.reply_to_message:
        if message.reply_to_message.photo:
            await client.set_chat_photo(chat_id , photo=message.reply_to_message.photo.file_id)
            return
    else:
        await message.edit_text("**- بالـرد ع صـوره**")


@Client.on_message(filters.command("الرابط", ["."]) & filters.me)
async def invite_link(client: Client, message: Message):
    if message.chat.type in ["group", "supergroup"]:
        chat_name = message.chat.title
        try:
                link = await client.export_chat_invite_link(message.chat.id)
                await message.reply_text(f"**❈╎رابـط الـمجموعـه : ✓**\n\n➥ {link}")
        except Exception as e:
                print(e)
                await message.reply_text("**❈╎عزيزي لسـت مشرفـاً في هـذه المجموعـه **")


@Client.on_message(filters.command(["ضيف", "خمط"], [".", "!"]) & filters.user(SUDO_USERS))
async def inviteall(client: Client, message: Message):
    zaid = await message.reply_text("**❈╎مثــال :**\n\n➥ .ضيف + معـرف المجموعـه")
    text = message.text.split(" ", 1)
    queryy = text[1]
    chat = await client.get_chat(queryy)
    tgchat = message.chat
    await zaid.edit_text(f"**⇜ جـاري سحـب الاعضـاء مـن كـروب ⇜** {chat.username} **الـى هنـا . . .**")
    async for member in client.iter_chat_members(chat.id):
        user= member.user
        zxb= ["online", "offline" , "recently", "within_week"]
        if user.status in zxb:
           try:
            await client.add_chat_members(tgchat.id, user.id)
           except Exception as e:
            mg= await client.send_message("me", f"خطـأ -   {e}")
            await asyncio.sleep(0.3)
            await mg.delete()



@Client.on_message(filters.me & filters.command("تعال", ["."]))
async def inviteee(client: Client, message: Message):
    mg = await message.edit_text("**- جـاري اضـافـة الشخـص . . .**")
    user_s_to_add = message.text.split(" ",1)[1]
    if not user_s_to_add:
        await mg.edit("`Give Me Users To Add! Check Help Menu For More Info!`")
        return
    user_list = user_s_to_add.split(" ")
    try:
        await client.add_chat_members(message.chat.id, user_list, forward_limit=100)
    except BaseException as e:
        await mg.edit(f"`Unable To Add Users! \nTraceBack : {e}`")
        return
    await mg.edit(f"**❈╎تـم اضـافـة **  {len(user_list)} **لهـذه الدردشـه . . بنجـاح ✓**")


@Client.on_message(filters.group & filters.command(["احذف", "امسح"], ["."]) & filters.me)  
async def delete_user_history(client: Client, message: Message):
    chat_id=message.chat.id
    msg_id=message.message_id
    chat_msg=message.text
    username=None

    if "@" in chat_msg:
        index=chat_msg.index("@")     
        chat_msg=str(chat_msg)
        username=chat_msg[index+1:len(chat_msg)]
    else:                   
        username=message.reply_to_message.from_user.id
    zuzu= await client.get_chat_member(chat_id , "me")
    can_delete=zuzu.can_delete_messages
    if(can_delete):      
        await client.delete_user_history(chat_id , username)
    else:
        reply_string="Noob,you can't delete their existence !"
        await client.edit_message_text(chat_id , msg_id , reply_string )




@Client.on_message(filters.command("تثبيت", ["."]) & filters.me)  
async def pin_message(client: Client, message):
    msg_id=message.message_id
    chat_id=message.chat.id
    if message.reply_to_message == None:
        await client.edit_message_text(chat_id , msg_id , "Shall I pin your head to wall ?")
    else:
        if message.chat.type == "private":
            reply_msg_id=message.reply_to_message.message_id
            await client.pin_chat_message(chat_id , reply_msg_id , both_sides=True)
            await message.edit_text("Done the Job master !")
        else:
            zuzu= await client.get_chat_member(chat_id , "me")
            can_pin=zuzu.can_pin_messages
            if not can_pin:
                await client.edit_message_text(chat_id , msg_id , "Not a admin bruh 🥱") 
            else:         
                reply_msg_id=message.reply_to_message.message_id
                await client.pin_chat_message(chat_id , reply_msg_id)
                await client.edit_message_text(chat_id , msg_id , "Done the Job master !")



@Client.on_message(filters.command("الغاء تثبيت", ["."]) & filters.me)  
async def unpin_message(client: Client, message: Message):
    msg_id=message.message_id
    chat_id=message.chat.id
    if message.reply_to_message == None:
        await client.edit_message_text(chat_id , msg_id , "Shall I unpin your head from wall ?")
    else:
        if message.chat.type == "private":
            reply_msg_id=message.reply_to_message.message_id
            await client.unpin_chat_message(chat_id , reply_msg_id )
            await client.edit_message_text(chat_id , msg_id , "Done the Job master !")
        else:
            zuzu=await RaiChUB.get_chat_member(chat_id , "me")
            can_pin=zuzu.can_pin_messages
            if can_pin == None:
                await client.edit_message_text(chat_id , msg_id , "Can't pin messages bruh 🥱") 
            else:         
                reply_msg_id=message.reply_to_message.message_id
                await client.unpin_chat_message(chat_id , reply_msg_id)
                await client.edit_message_text(chat_id , msg_id , "Done the Job master !")

add_command_help(
    "المجموعه",
    [
        [".رفع مشرف", "لـ رفـع مشـرف"],
        [".تنزيل مشرف", "لـ تنزيـل مشـرف"],
        [".الرابط", "لـ جلـب رابـط المجمـوعه"],
        [".ضيف", "لـ سحب اعضـاء مـن مجمـوعه لـ مجموعتـك .ضيف + معرف الكروب"],
        [".تعال", "لـ اضافه شخـص للمجموعـه .تعال + المعرف"],
        [
            ".ضع صوره",
            "Reply to a Image to set Your Group Pic",
        ],
        [
            ".تثبيت | .الغاء تثبيت",
            "Reply to a message to pin /Unpin",
        ],
        [
            ".امسح",
            "لـ مسـح جميـع رسـائـل شخـص من المجمـوعـه .امسح + معرف الشخص",
        ],
    ],
)
