# Heroku manager for your ZThon

# CC- @refundisillegal\nSyntax:-\n.get var NAME\n.del var NAME\n.set var NAME

# Copyright (C) 2020 Adek Maulana.
# All rights reserved.

import asyncio
import math
import os

import heroku3
import requests
import urllib3

from pyrogram.errors import PeerIdInvalid
from pyrogram.types import Message
from pyrogram import Client, filters
from pyrogram.types import *

useragent = (
    "Mozilla/5.0 (Linux; Android 9; SM-G975F) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/80.0.3987.149 Mobile Safari/537.36"
)

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
# =================

Heroku = heroku3.from_key(HEROKU_API_KEY)
heroku_api = "https://api.heroku.com"
HEROKU_APP_NAME = HEROKU_APP_NAME
HEROKU_API_KEY = HEROKU_API


@Client.on_message(filters.command('(set|get|del) var', ["."]) & filters.me)
async def setvar_handler(client: Client, message: Message):
    if (HEROKU_API is None) or (HEROKU_APP_NAME is None):
        return await message.edit(
            "**- عــذراً .. لـديك خطـأ بالـفـارات**\n**-اذهـب الـى حسـابك هيـروكو ثم اعـدادات التطبيـق ثم الفـارات وقـم بالتـأكـد من الفـارات التـاليـه :**\n\n `HEROKU_API_KEY` \n `HEROKU_APP_NAME`",
        )
    app = Heroku.app(HEROKU_APP_NAME)
    exe = var.pattern_match.group(1)
    heroku_var = app.config()
    if exe == "get":
        zed = await message.edit("**⌔∮ جاري الحصول على المعلومات. **")
        await asyncio.sleep(1.0)
        try:
            variable = var.pattern_match.group(2).split()[0]
            if variable in heroku_var:
                return await message.edit(
                    "𓆩 𝑺𝑶𝑼𝑹𝑪𝑬 𝙕𝞝𝘿𝙏𝙃𝙊𝙉 - 𝑮𝑶𝑵𝑭𝑰𝑮 𝑽𝑨𝑹𝑺 𓆪\n**𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻**" f"\n\n**⌔∮الفــار** `{variable} = {heroku_var[variable]}` .\n"
                )
            await message.edit(
                "𓆩 𝑺𝑶𝑼𝑹𝑪𝑬 𝙕𝞝𝘿𝙏𝙃𝙊𝙉 - 𝑮𝑶𝑵𝑭𝑰𝑮 𝑽𝑨𝑹𝑺 𓆪\n**𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻**" f"\n\n**⌔∮الفــار** `{variable}` غيــر مـوجــود ؟!"
            )
        except IndexError:
            configs = prettyjson(heroku_var.to_dict(), indent=2)
            with open("configs.json", "w") as fp:
                fp.write(configs)
            with open("configs.json", "r") as fp:
                result = fp.read()
                await message.edit(
                    zed,
                    "`[HEROKU]` ConfigVars:\n\n"
                    "================================"
                    f"\n```{result}```\n"
                    "================================",
                )
            os.remove("configs.json")
    elif exe == "set":
        variable = "".join(var.text.split(maxsplit=2)[2:])
        zed = await message.edit("**⌔∮ جاري اعداد المعلومات**")
        if not variable:
            return await message.edit("`.set var <ConfigVars-name> <value>`")
        value = "".join(variable.split(maxsplit=1)[1:])
        variable = "".join(variable.split(maxsplit=1)[0])
        if not value:
            return await message.edit("`.set var <ConfigVars-name> <value>`")
        await asyncio.sleep(1.5)
        if variable in heroku_var:
            await message.edit("**⌔∮ تم تغيـر** `{}` **:**\n **- المتغير :** `{}` \n**- يتم الان اعـادة تشغيـل بـوت زد ثـون يستغـرق الامر 2-1 دقيقـه ▬▭ ...**".format(variable, value))
        else:
            await message.edit("**⌔∮ تم اضافه** `{}` **:** \n**- المضاف اليه :** `{}` \n**يتم الان اعـادة تشغيـل بـوت زد ثـون يستغـرق الامر 2-1 دقيقـه ▬▭ ...**".format(variable, value))
        heroku_var[variable] = value
    elif exe == "del":
        zed = await message.edit("⌔∮ الحصول على معلومات لحذف المتغير. ")
        try:
            variable = var.pattern_match.group(2).split()[0]
        except IndexError:
            return await message.edit("⌔∮ يرجى تحديد `Configvars` تريد حذفها. ")
        await asyncio.sleep(1.5)
        if variable not in heroku_var:
            return await message.edit(f"⌔∮ `{variable}`**  غير موجود**")

        await message.edit(f"**⌔∮** `{variable}`  **تم حذفه بنجاح. \n**يتم الان اعـادة تشغيـل بـوت زد ثـون يستغـرق الامر 2-1 دقيقـه ▬▭ ...**")
        del heroku_var[variable]



@Client.on_message(filters.command('usage', ["."]) & filters.me)
async def dynostats_handler(client: Client, message: Message):
    if (HEROKU_APP_NAME is None) or (HEROKU_API_KEY is None):
        return await message.edit(
            dyno,
            "**- عــذراً .. لـديك خطـأ بالـفـارات**\n**-اذهـب الـى حسـابك هيـروكو ثم اعـدادات التطبيـق ثم الفـارات وقـم بالتـأكـد من الفـارات التـاليـه :**\n\n `HEROKU_API_KEY` \n `HEROKU_APP_NAME`",
        )
    dyno = await message.edit(dyno, "**⌔∮ جــاري المعـالجـه ...**")
    useragent = (
        "Mozilla/5.0 (Linux; Android 10; SM-G975F) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/80.0.3987.149 Mobile Safari/537.36"
    )
    user_id = Heroku.account().id
    headers = {
        "User-Agent": useragent,
        "Authorization": f"Bearer {HEROKU_API}",
        "Accept": "application/vnd.heroku+json; version=3.account-quotas",
    }
    path = f"/accounts/{user_id}/actions/get-quota"
    r = requests.get(heroku_api + path, headers=headers)
    if r.status_code != 200:
        return await dyno.edit(
            "⌔∮ خطا:** شي سيء قد حدث **\n" f" ⌔∮ `{r.reason}`\n"
        )
    result = r.json()
    quota = result["account_quota"]
    quota_used = result["quota_used"]

    # - Used -
    remaining_quota = quota - quota_used
    percentage = math.floor(remaining_quota / quota * 100)
    minutes_remaining = remaining_quota / 60
    hours = math.floor(minutes_remaining / 60)
    minutes = math.floor(minutes_remaining % 60)
    # - Current -
    App = result["apps"]
    try:
        App[0]["quota_used"]
    except IndexError:
        AppQuotaUsed = 0
        AppPercentage = 0
    else:
        AppQuotaUsed = App[0]["quota_used"] / 60
        AppPercentage = math.floor(App[0]["quota_used"] * 100 / quota)
    AppHours = math.floor(AppQuotaUsed / 60)
    AppMinutes = math.floor(AppQuotaUsed % 60)
    await asyncio.sleep(1.5)
    return await dyno.edit(
        "𓆩 𝑺𝑶𝑼𝑹𝑪𝑬 𝙕𝞝𝘿𝙏𝙃𝙊𝙉 - 𝑫𝒀𝑵𝑶 𝑼𝑺𝑨𝑮𝑬 𓆪\n𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n\n"
        f"**⌔∮ اسم التطبيق في هيروكو :**\n"
        f"**    - معرف اشتراكك ⪼ {HEROKU_APP_NAME}**"
        f"\n\n"
        f" **⌔∮ مدة اسـتخدامك لبوت زد ثـون : **\n"
        f"     -  `{AppHours}`**ساعه**  `{AppMinutes}`**دقيقه**  "
        f"**⪼**  `{AppPercentage}`**%**"
        "\n\n"
        " **⌔∮ الساعات المتبقيه لاستخدامك : **\n"
        f"     -  `{hours}`**ساعه**  `{minutes}`**دقيقه**  "
        f"**⪼**  `{percentage}`**%**"
    )


@Client.on_message(filters.command('logs', ["."]) & filters.me)
async def logs_handler(client: Client, message: Message):
    if (HEROKU_APP_NAME is None) or (HEROKU_API_KEY is None):
        return await message.edit(
            dyno,
            "**- عــذراً .. لـديك خطـأ بالـفـارات**\n**-اذهـب الـى حسـابك هيـروكو ثم اعـدادات التطبيـق ثم الفـارات وقـم بالتـأكـد من الفـارات التـاليـه :**\n\n `HEROKU_API_KEY` \n `HEROKU_APP_NAME`",
        )
    try:
        Heroku = heroku3.from_key(HEROKU_API_KEY)
        app = Heroku.app(HEROKU_APP_NAME)
    except BaseException:
        return await dyno.reply(
            " Please make sure your Heroku API Key, Your App name are configured correctly in the heroku"
        )
    data = app.get_log()
    await message.edit(
        dyno, data, deflink=True, linktext="**-آخـر 100 سطـر مـن سجـلات تنصيبـك :**"
    )


def prettyjson(obj, indent=2, maxlinelength=80):
    """Renders JSON content with indentation and line splits/concatenations to fit maxlinelength.
    Only dicts, lists and basic types are supported"""
    items, _ = getsubitems(
        obj,
        itemkey="",
        islast=True,
        maxlinelength=maxlinelength - indent,
        indent=indent,
    )
    return indentitems(items, indent, level=0)
