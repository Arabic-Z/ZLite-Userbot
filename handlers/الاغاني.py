import re
from datetime import datetime
import asyncio
import os
import time
import requests
import wget
from yt_dlp import YoutubeDL
from youtubesearchpython import SearchVideos
from pyrogram import Client, filters
from pyrogram.errors import PeerIdInvalid
from pyrogram.types import User , Message
from urllib.request import urlretrieve
import requests as r
from handlers.help import add_command_help


def get_text(message: Message) -> [None, str]:
    """Extract Text From Commands"""
    text_to_return = message.text
    if message.text is None:
        return None
    if " " in text_to_return:
        try:
            return message.text.split(None, 1)[1]
        except IndexError:
            return None
    else:
        return None


@Client.on_message(filters.command("بحث", ".") & filters.me)
async def song(client: Client, message: Message):
    input_str = get_text(message)
    rep= await message.edit_text(f"**╮ جـارِ البحث ؏ـن {input_str} عـلى يوتيـوب... 🎧♥️╰**")
    if not input_str:
        await rep.edit(
            "`Please Give Me A Valid Input. You Can Check Help Menu To Know More!`"
        )
        return
    await rep.edit(f"**╮ جـارِ تحميـل {input_str} مـن اليوتيـوب... 🎧♥️╰**")
    search = SearchVideos(str(input_str), offset=1, mode="dict", max_results=1)
    rt = search.result()
    result_s = rt["search_result"]
    url = result_s[0]["link"]
    vid_title = result_s[0]["title"]
    yt_id = result_s[0]["id"]
    uploade_r = result_s[0]["channel"]
    thumb_url = f"https://img.youtube.com/vi/{yt_id}/hqdefault.jpg"
    await asyncio.sleep(0.6)
    downloaded_thumb = wget.download(thumb_url)
    opts = {
        "format": "bestaudio",
        "addmetadata": True,
        "key": "FFmpegMetadata",
        "writethumbnail": True,
        "prefer_ffmpeg": True,
        "geo_bypass": True,
        "nocheckcertificate": True,
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "720",
            }
        ],
        "outtmpl": "%(id)s.mp3",
        "quiet": True,
        "logtostderr": False,
    }
    try:
        with YoutubeDL(opts) as ytdl:
            ytdl_data = ytdl.extract_info(url, download=True)
    except Exception as e:
        await rep.edit(f"**- خطـأ فـي التحميـل . . .** \n**- الخطـأ :** `{str(e)}`")
        return
    c_time = time.time()
    file_sung= f"{ytdl_data['id']}.mp3"
    capy = f"**الاسـم ➠** `{vid_title}` \n**نتيجـة بحـث ➠** `{input_str}` \n**قنـاة يوتيـوب ➠** `{uploade_r}` \n**الرابــط ➠** `{url}`"
    await client.send_audio(
        message.chat.id,
        audio=open(file_sung, "rb"),
        title=str(ytdl_data["title"]),
        performer=str(ytdl_data["uploader"]),
        thumb=downloaded_thumb,
        caption=capy
    )
    await rep.delete()
    for files in (downloaded_thumb, file_sung):
        if files and os.path.exists(files):
            os.remove(files)
            
	
	
@Client.on_message(filters.command("سافان", ".") & filters.me)
async def savnana(client: Client, message: Message):
    song = get_text(message)
    if not song:
        return await message.edit_text("`Give me Something to Search")
    hmm = time.time()
    lol = await message.edit_text("`Searching on Saavn...`")
    sung = song.replace(" ", "%20")
    url = f"https://jostapi.herokuapp.com/saavn?query={sung}"
    try:
        k = (r.get(url)).json()[0]
    except IndexError:
        return await eod(lol, "`Song Not Found.. `")
    title = k["song"]
    urrl = k["media_url"]
    img = k["image"]
    duration = k["duration"]
    singers = k["singers"]
    urlretrieve(urrl, title + ".mp3")
    urlretrieve(img, title + ".jpg")
    file= wget.download(urrl)
    await client.send_audio(message.chat.id,file,caption=f"Song from saavan uploaded by king Userbot \n Song name={title}\n Singers={singers}" )   
    await lol.delete()
    os.remove(title + ".mp3")
    os.remove(title + ".jpg")


@Client.on_message(filters.command("كلود", ".") & filters.me)
async def deezergeter(client: Client, message: Message):
    rep = await message.edit_text("`Searching For Song On Deezer.....`")
    sgname = get_text(message)
    if not sgname:
        await rep.edit(
            "`Please Give Me A Valid Input. You Can Check Help Menu To Know More!`"
        )
        return
    link = f"https://api.deezer.com/search?q={sgname}&limit=1"
    dato = r.get(url=link).json()
    match = dato.get("data")
    try:
        urlhp = match[0]
    except IndexError:
        await rep.edit("`Song Not Found. Try Searching Some Other Song`")
        return
    urlp = urlhp.get("link")
    thumbs = urlhp["album"]["cover_big"]
    thum_f = wget.download(thumbs)
    polu = urlhp.get("artist")
    replo = urlp[29:]
    urlp = f"https://starkapis.herokuapp.com/deezer/{replo}"
    datto = r.get(url=urlp).json()
    mus = datto.get("url")
    sname = f"{urlhp.get('title')}.mp3"
    doc = r.get(mus)
    await client.send_chat_action(message.chat.id, "upload_audio")
    await rep.edit("`Downloading Song From Deezer!`")
    with open(sname, "wb") as f:
        f.write(doc.content)
    c_time = time.time()
    car = f"""
**Song Name :** {urlhp.get("title")}
**Duration :** {urlhp.get('duration')} Seconds
**Artist :** {polu.get("name")}
Music Downloaded And Uploaded By King Userbot"""
    await rep.edit(f"`Downloaded {sname}! Now Uploading Song...`")
    await client.send_audio(
        message.chat.id,
        audio=open(sname, "rb"),
        duration=int(urlhp.get("duration")),
        title=str(urlhp.get("title")),
        performer=str(polu.get("name")),
        thumb=thum_f,
        caption=car)
    await client.send_chat_action(message.chat.id, "cancel")
    await rep.delete()


@Client.on_message(filters.command(["فيد", "فيديو"] , ["."]) & filters.me)
async def yt_vid(client: Client, message: Message):
    input_st = message.text
    input_str= input_st.split(" ", 1)[1]
    pablo = await message.edit_text("**- جـاري**")
    if not input_str:
        await message.edit_text(
            "**❈╎قم باضافـة الاغنيـه للامـر .. فيديو + اسـم الفيديـو**"
        )
        return
    await message.edit_text(f"**╮ جـارِ البحث ؏ـن {input_str} ... 🎧♥️╰**")
    search = SearchVideos(str(input_str), offset=1, mode="dict", max_results=1)
    rt = search.result()
    result_s = rt["search_result"]
    url = result_s[0]["link"]
    vid_title = result_s[0]["title"]
    yt_id = result_s[0]["id"]
    uploade_r = result_s[0]["channel"]
    thumb_url = f"https://img.youtube.com/vi/{yt_id}/hqdefault.jpg"
    await asyncio.sleep(0.6)
    downloaded_thumb = wget.download(thumb_url)
    opts = {
        "format": "best",
        "addmetadata": True,
        "key": "FFmpegMetadata",
        "prefer_ffmpeg": True,
        "geo_bypass": True,
        "nocheckcertificate": True,
        "postprocessors": [{"key": "FFmpegVideoConvertor", "preferedformat": "mp4"}],
        "outtmpl": "%(id)s.mp4",
        "logtostderr": False,
        "quiet": True,
    }
    try:
        with YoutubeDL(opts) as ytdl:
            ytdl_data = ytdl.extract_info(url, download=True)
    except Exception as e:
        await message.edit_text(f"**- خطـأ فـي التحميـل . . .** \n**- الخطـأ :** `{str(e)}`")
        return
    c_time = time.time()
    file_path= f"{ytdl_data['id']}.mp4"
    capy = f"**- المقطـع ➠** `{vid_title}` \n**- البحـث ➠** `{input_str}` \n**- القنـاة ➠** `{uploade_r}` \n**- الرابـط ➠** `{url}`"
    await client.send_video(
        message.chat.id,
        video=open(file_path, "rb"),
        duration=int(ytdl_data["duration"]),
        file_name=str(ytdl_data["title"]),
        thumb=downloaded_thumb,
        caption=capy,
        supports_streaming=True,
    )
    await message.delete()
    for files in (downloaded_thumb, file_path):
        if files and os.path.exists(files):
            os.remove(files)



add_command_help(
    "الاغاني",
    [
        [".بحث", "- تحميـل المقـاطـع الصـوتيـه مـن يـوتيـوب"],
        [".فيديو", "- تحميـل مقـاطـع الفيـديـو مـن يـوتيـوب"],
        [".كلود", "- تحميـل المقـاطـع الصـوتيـه مـن سـاونـدكـلاود و دايـزيـر"],
        [".سافان", "- تحميـل مـن سـافـان"],
    ],
)
