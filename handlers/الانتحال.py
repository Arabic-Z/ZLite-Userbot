#~ Ported from Zed-Thon[Telethon]
#~ ©ZedThon

import os
from asyncio import sleep
from pyrogram import *
from pyrogram.types import *
from pyrogram import filters, Client
from pyrogram.raw import functions
from pyrogram.types import Message
from helpers.basic import edit_or_reply, get_text, get_user
from helpers.SQL.cloner_db import backup_indentity, restore_identity
from handlers.help import add_command_help


OWNER = os.environ.get("OWNER", None)
BIO = os.environ.get("BIO", None)
profile_photo = "handlers/cache/pfp.jpg"



@Client.on_message(filters.command('نسخ', ["."]) & filters.me)
async def clone(client: Client, message: Message):
  text = get_text(message)
  op = await edit_or_reply(message, "`Cloning`")
  userk = get_user(message, text)[0]
  user_ = await client.get_users(userk)
  if not user_:
    await op.edit("`Whom i should clone:(`")
    return
    
  get_bio = await client.get_chat(user_.id)
  f_name = user_.first_name
  c_bio = get_bio.bio
  pic = user_.photo.big_file_id
  poto = await client.download_media(pic)

  await client.set_profile_photo(photo=poto)
  await client.update_profile(
       first_name=f_name,
       bio=c_bio,
  )
  await message.edit(f"**From now I'm** __{f_name}__")
    

@Client.on_message(filters.command('اعاده', ["."]) & filters.me)
async def revert(client: Client, message: Message):
 await message.edit("`Reverting`")
 r_bio = BIO
	
	#Get ur Name back
 await client.update_profile(
	  first_name=OWNER,
	  bio=r_bio,
	)
	#Delte first photo to get ur identify
 photos = await client.get_profile_photos("me")
 await client.delete_profile_photos(photos[0].file_id)
 await message.edit("`I am back!`")




@Client.on_message(filters.me & filters.command(["setpfp"], ["."]))
async def set_pfp(client: Client, message: Message):
    replied = message.reply_to_message
    if (replied and replied.media and (
            replied.photo or (
            replied.document and "image" in replied.document.mime_type
    )
    )
    ):
        await client.download_media(
            message=replied,
            file_name=profile_photo
        )
        await client.set_profile_photo(profile_photo)
        if os.path.exists(profile_photo):
            os.remove(profile_photo)
        await message.edit(
            "<code>Profile picture changed.</code>",
            parse_mode='html'
        )
    else:
        await message.edit("```Reply to any photo to set as pfp```")
        await sleep(3)
        await message.delete()


@Client.on_message(filters.me & filters.command(["vpfp"], ["."]))
async def view_pfp(client: Client, message: Message):
    replied = message.reply_to_message
    if replied:
        user = await client.get_users(replied.from_user.id)
    else:
        user = await client.get_me()
    if not user.photo:
        await message.edit("profile photo not found!")
        return
    await client.download_media(
        user.photo.big_file_id,
        file_name=profile_photo
    )
    await client.send_photo(message.chat.id, profile_photo)
    await message.delete()
    if os.path.exists(profile_photo):
        os.remove(profile_photo)



add_command_help(
    "usertools",
    [
        [".setpfp", "Reply to any photo to set as pfp."],
        [".vpfp", "View current pfp of user."],
        [
            ".نسخ",
            "clone user identity without original backup",
        ],
        [
            ".clone origin",
            "clone user identity with original backup",
        ],
        [
            ".اعاده",
            "revert to original identity",
        ],
    ],
)
