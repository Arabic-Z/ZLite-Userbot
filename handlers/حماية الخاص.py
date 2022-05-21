from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton , InlineQuery ,Message, CallbackQuery, InlineQueryResultPhoto, User
from pyrogram import filters, Client
from pyrogram.types import Message
import re
from helpers.SQL.pmstuff import givepermit, checkpermit, blockuser, getwarns, allallowed, allblocked, inwarns, addwarns
from main import SUDO_USERS as Adminsettings, LOG_GROUP
from handlers.help import *
from main import ALIVE_PIC

Alive_msg = f"𓆩𝙎𝙊𝙐𝙍𝘾𝙀 𝙕𝞝𝘿𝙏𝙃𝙊𝙉 - 𝑷𝑴 𝑺𝑬𝑪𝑼𝑹𝑰𝑻𝒀𓆪\n"
Alive_msg = f"◐━─━─━─━─𝙕𝞝𝘿─━─━─━─━◐\n"
Alive_msg += f"❞ **مـرحبـاً عـزيـزي**❝\n\n"
Alive_msg += f"**⤶ انا مشغـول حـالياً لا تقـم بازعـاجي والا سـوف يتم حظـرك تلقـائياً.....**\n\n"
Alive_msg += f"**⤶ فقط قل سبب مجيئك وانتظـر الـرد ⏳**\n\n"
Alive_msg += f"◐━─━─━─━─𝙕𝞝𝘿─━─━─━─━◐\n\n"

@Client.on_message(~filters.me & filters.private & ~filters.bot & filters.incoming , group = 69)
async def alive(client: Client, e: Message):
  message = e
  if checkpermit(message.chat.id):
        print("sql is cringe here")
        return
  else:
    print("gotit")
    addwarns(message.chat.id)
    gw= getwarns(message.chat.id)
    teriu= message.from_user
    teriun= teriu.id
    teriuni= str(teriun)
    teriunia="aprv_"+teriuni
    teriunid="decine_"+teriuni
    ids = 0
  if isinstance(gw , str):
      sb= await client.get_me()
      un= LOG_GROUP
  else:
      keyboard= InlineKeyboardMarkup([  # First row
                    InlineKeyboardButton(  # Generates a callback query when pressed
                        "Approve",
                        callback_data=teriunia
                    ),
                    InlineKeyboardButton(
                        "Decline",
                        callback_data=teriunid
                    ),
                ])
      await message.reply_photo(photo=ALIVE_PIC, caption=Alive_msg)
      if gw==3:
        await message.reply_text("**⤶ لقـد حـذرتــڪ مـسـبـقـاً مـن تـڪـرار الـرسـائـل ...**\n**⤶ تـم حـظـرڪ تلقـائيـاً 🚷.** \n**⤶ الـى ان يـاتـي مـالـڪ الـحـسـاب 😇**")
        await client.block_user(message.from_user.id)
        blockuser(message.from_user.id)
        return


@Client.on_message(filters.command(["سماح", "س", "قبول"], ["."]) & filters.me & filters.private)
async def refet(client: Client, message: Message):
    givepermit(message.chat.id)
    await message.edit_text("**⌔∮تـم السـمـاح لـه بـإرسـال الـرسـائـل هنـا 💬✓**")
    
     
@Client.on_message(filters.command(["رفض", "dap", "ر", "disapprove", "dp"], ["."]) & filters.me & filters.private)
async def refes(client: Client, message: Message):
    await message.edit_text("**⌔∮تـم رفضـه مـن إرسـال الـرسـائـل هنـا 💬✓**")
    blockuser(message.chat.id)
    await client.block_user(message.chat.id)
    
@Client.on_message(filters.command(["allpermitted", "المقبولين"], ["."]) & filters.me)
async def rfet(client: Client, message: Message):
  dtt = allallowed()
  strr ="**⌔∮قـائمـة السمـاح :**"
  for x in dtt:
    usr= client.get_users(x)
    strr+=f"\n {usr.mention()}"
  await message.edit_text(strr)

@Client.on_message(filters.command(["المرفوضين"], ["."]) & filters.me)
async def rfet(client: Client, message: Message):
  dtt = allblocked()
  strr ="**⌔∮قـائمـة المرفـوضين :**"
  for x in dtt:
    usr= client.get_users(x)
    strr+=f"\n {usr.mention()}"
  await message.edit_text(strr)

@Client.on_message(filters.command(["nonpermitted"], ["."]) & filters.me)
async def rfet(client: Client, message: Message):
  dtt = inwarns()
  strr ="**⌔∮قـائمـة الغير مرفوضين بعـد :**"
  for x in dtt:
    usr= client.get_users(x)
    strr+=f"\n {usr.mention()}"
  await message.edit_text(strr)


add_command_help(
    "حماية الخاص",
    [
        [
            ".ap",
            "To Approve A User in Your Pm",
        ],
        [
            ".dap",
            "To Disapprove/Block A User in Your Pm",
        ],
        [
            ".approvedlist",
            "Get approved Users list",
        ],
        [
            ".allblocked",
            "Get blocked list",
        ],
        [
            ".nonpermitted",
            "non permitted list",
        ],
    ],
)
