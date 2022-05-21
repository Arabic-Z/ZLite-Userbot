import asyncio
import time

import speedtest
import os

from telegraph import upload_file
from pyrogram import filters, Client
from pyrogram.raw import functions
from pyrogram.types import Message

from helpers.PyroHelpers import SpeedConvert
from helpers.constants import WWW
from helpers.expand import expand_url
from helpers.shorten import shorten_url
from handlers.help import add_command_help
from handlers.help import *
from main import *


@Client.on_message(filters.command(["تلكراف ميديا", "تليكراف ميديا", "تلكراف"], ".") & filters.me) 
async def telegraph(client: Client, message: Message):
    replied = message.reply_to_message
    if not replied:
        await message.reply_text("reply to a supported media file")
        return
    if not (
        (replied.photo and replied.photo.file_size <= 5242880)
        or (replied.animation and replied.animation.file_size <= 5242880)
        or (
            replied.video
            and replied.video.file_name.endswith(".mp4")
            and replied.video.file_size <= 5242880
        )
        or (
            replied.document
            and replied.document.file_name.endswith(
                (".jpg", ".jpeg", ".png", ".gif", ".mp4")
            )
            and replied.document.file_size <= 5242880
        )
    ):
        await message.reply_text("not supported!")
        return
    download_location = await client.download_media(
        message=message.reply_to_message, file_name="root/nana/"
    )
    try:
        response = upload_file(download_location)
    except Exception as document:
        await client.send_message(message.chat.id, document)
    else:
        await message.reply_text(
            f"**⌔∮الــرابـط : [اضغــط هنـــا](https://telegra.ph{response[0]})**",
        )
    finally:
        os.remove(download_location)


@Client.on_message(filters.command(["سرعه النت", "سرعة النت"], ".") & filters.me)
async def speed_test(client: Client, message: Message):
    new_msg = await message.edit("`Running speed test . . .`")
    spd = speedtest.Speedtest()

    new_msg = await message.edit(
        f"`{new_msg.text}`\n" "`Getting best server based on ping . . .`"
    )
    spd.get_best_server()

    new_msg = await message.edit(f"`{new_msg.text}`\n" "`Testing download speed . . .`")
    spd.download()

    new_msg = await message.edit(f"`{new_msg.text}`\n" "`Testing upload speed . . .`")
    spd.upload()

    new_msg = await new_msg.edit(
        f"`{new_msg.text}`\n" "`Getting results and preparing formatting . . .`"
    )
    results = spd.results.dict()

    await message.edit(
        WWW.SpeedTest.format(
            start=results["timestamp"],
            ping=results["ping"],
            download=SpeedConvert(results["download"]),
            upload=SpeedConvert(results["upload"]),
            isp=results["client"]["isp"],
        )
    )


@Client.on_message(filters.command("المركز", ".") & filters.me)
async def nearest_dc(client: Client, message: Message):
    dc = await client.send(functions.help.GetNearestDc())
    await message.edit(WWW.NearestDC.format(dc.country, dc.nearest_dc, dc.this_dc))


@Client.on_message(filters.command("بنك", [".", "!"]) & filters.me)
async def pingme(client: Client, message: Message):
    """Ping the assistant"""
    start = time.time()
    reply = await message.reply_text("...")
    delta_ping = time.time() - start
    await reply.edit_text(f"🎉 🇵 🇴 🇳 🇬 !\n\n♡︎ `{delta_ping * 1000:.3f}` 𝗺𝘀 ♡︎")



@Client.on_message(filters.command("expand", ".") & filters.me)
async def expand(client: Client, message: Message):
    if message.reply_to_message:
        url = message.reply_to_message.text or message.reply_to_message.caption
    elif len(message.command) > 1:
        url = message.command[1]
    else:
        url = None

    if url:
        expanded = await expand_url(url)
        if expanded:
            await message.edit(
                f"<b>Shortened URL</b>: {url}\n<b>Expanded URL</b>: {expanded}",
                disable_web_page_preview=True,
            )
        else:
            await message.edit("No bro that's not what I do")
    else:
        await message.edit("Nothing to expand")


@Client.on_message(filters.command("shorten", ".") & filters.me)
async def shorten(client: Client, message: Message):
    keyword = None

    if message.reply_to_message:
        url = message.reply_to_message.text or message.reply_to_message.caption
        if len(message.command) > 1:
            keyword = message.command[1]
    elif len(message.command) > 2:
        url = message.command[1]
        keyword = message.command[2]
    elif len(message.command) > 1:
        url = message.command[1]
    else:
        url = None

    if url:
        shortened = await shorten_url(url, keyword)
        if shortened == "API ERROR":
            txt = "API URL or API KEY not found! Add YOURLS details to config"
        elif shortened == "INVALID URL":
            txt = f"The provided URL: `{url}` is invalid"
        elif shortened == "KEYWORD/URL Exists":
            txt = "The URL or KEYWORD already exists!"
        else:
            txt = f"<b>Original URL</b>: {url}\n<b>Shortened URL</b>: {shortened}"
            await message.edit(txt, disable_web_page_preview=True)
            return
    else:
        txt = "Please provide a URL to shorten"

    await message.edit(txt)
    await asyncio.sleep(3)
    await message.delete()


add_command_help(
    "تلكراف",
    [
        [".تلكراف ميديا", "Reply to Media as args to upload it to telegraph."],
        [".بنك", "Calculates ping time between you and Telegram."],
        [".المركز", "Get's your Telegram DC."],
        [
            ".سرعة النت `or` .speed",
            "Runs a speedtest on the server this userbot is hosted.. Flex on them haters. With an in "
            "Telegram Speedtest of your server..",
        ],
        [
            ".expand",
            "Expands a shortened url. Works for replied to message, photo caption or .expand url",
        ],
        [
            ".shorten",
            "Shortens a url. Works for replied to message, photo caption or .shorten url keyword",
        ],
    ],
)
