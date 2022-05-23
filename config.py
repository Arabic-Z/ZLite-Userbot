# ZLite - UserBot
# Copyright (C) 2022 ZThon-Ar . All Rights Reserved
#t.me/ZedThon
# This file is a part of < https://github.com/ZThon-Ar/ZLite-UserBot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/ZThon-Ar/ZLite-UserBot/blob/master/LICENSE/>.


import os
from os import getenv

from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")


if os.uname()[1] == "localhost":
    response = os.system("pip3 install -r requirements.txt --no-cache-dir")
    if response == 0:
        print("Successfully Installed all requirements")
    else:
        print("Failed to install requirements")


# if you deployed this userbot using localhost method, then replace all the necessary parts of the variables given below after '=' sign with the required values.
# for example edit like 'API_ID = 1234567' instead of 'API_ID = os.getenv("API_ID")'
# Warning: don't touch anything else given below except the values you wanna change otherwise you'll get errors.
# -------------------------------------------------------------------------------------------------------------
class Config(object):
    """configuration class"""

    # api id of your telegram account (required)
    API_ID = int(os.getenv("API_ID"))
    # api hash of your telegram account (required)
    API_HASH = os.getenv("API_HASH")
    # create a session using command [ python3 session.py ] or use repl.it (required)
    SESSION = os.getenv("SESSION")
    # ------------------
    # temporary download location (required)
    TEMP_DICT = os.getenv("TEMP_DICT", os.path.abspath(".") + "/downloads/")
    # official repo for updates
    UPSTREAM_REPO = os.getenv(
        "UPSTREAM_REPO", "https://github.com/TeamAsterix/AsterixUB.git"
    )
    # ------------------
    # heroku api key (required -> if hosted on heroku)
    HEROKU_API_KEY = os.getenv("HEROKU_API")
    # heroku app name (required -> if hosted on heroku)
    HEROKU_APP_NAME = os.getenv("HEROKU_APP_NAME")
    # database url (required)
    DB_URI = os.getenv("DATABASE_URL")
    # ------------------
    # these users can use your userbot
    SUDO_USERS = [
        int(x) for x in os.getenv("SUDO_USERS", "").split()
    ]  # splits on spaces
    # a group to store logs, etc (required)
    LOG_CHAT = int(os.getenv("LOG_CHAT"))
    # command handler, if you give (exclamation symbol = !) then you can do like this command: !ping => result: pong !
    PREFIX = os.getenv("PREFIX", ".")
    # for more info visit docs.pyrogram.org, workers section
    WORKERS = int(os.getenv("WORKERS", 8))
    # exclude official plugins from installing, give a space between plugin names
    NO_LOAD = [int(x) for x in os.getenv("NO_LOAD", "").split()]  # splits on spaces
    # default reason for afk plugin
    AFK_TEXT = os.getenv("AFK_TEXT", "I am busy Now !")
    # ------------------
    # add True to enable (default: False)
    PMPERMIT = os.getenv("PMPERMIT", False)
    # pmpermit pic (optional)
    PMPERMIT_PIC = os.getenv("PMPERMIT_PIC")
    # custom  pmpermit security text (optional)
    PMPERMIT_TEXT = os.getenv(
        "PMPERMIT_TEXT",
        "Hey ! This is [ Asterix Userbot](https://t.me/TeamAsterix) Security System.\n**You will be blocked if you spammed my owner's pm**\nCurrently My Owner is busy! So Wait Until He Arrives. ????\nAnd Better Not To Spam His here!",
    )
    # pmpermit warn limit (optional)
    PM_LIMIT = int(os.getenv("PM_LIMIT", 4))
    # this is used to get your accurate time
    TIME_ZONE = os.getenv("TIME_ZONE", "Asia/Kolkata")
    # -------------------
    # your custom name (default: telegram name)
    USER_NAME = os.getenv("USER_NAME")
    # your custom bio (default: telegram bio)
    USER_BIO = os.getenv("USER_BIO")
    # used for alive plugin (default: asterixuserbot logo image)
    USER_PIC = os.getenv("USER_PIC", "")
    # add your telegram id if bot fails to get your id
    USER_ID = os.getenv("USER_ID")
    # add your username if bot fails to get your username
    USER_USERNAME = os.getenv("USER_USERNAME")
    # --------------------
    # this bio will be shown in '/help' menu (default: official bio from bot)
    BOT_BIO = os.getenv("BOT_BIO")
    # your assistants custom name (default: Kushina)
    BOT_NAME = os.getenv("BOT_NAME", "Kushina")
    # your assistants alive pic (optional)
    BOT_PIC = os.getenv("BOT_PIC", "https://telegra.ph/file/3930fb44de59f65849f5b.jpg")
    # provide this if bot fails to get username of bot (optional)
    BOT_USERNAME = os.getenv("BOT_USERNAME")
    # telegram id of bot if failed to get automatically (optional)
    BOT_ID = os.getenv("BOT_ID")
    # access token of your bot, without this the bot will not work (required)
    TOKEN = os.getenv("TOKEN")
    # your telegraph account name (default: Asterixuserbot)
    TL_NAME = os.getenv("TL_NAME")
    # this will be shown before (as a prefix) the texts in the help dex (default: None)
    HELP_EMOJI = os.getenv("HELP_EMOJI")



que = {}
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "2095357462").split()))
API_ID = int(getenv("API_ID", "10219117"))
API_HASH = getenv("API_HASH", "13d45619687411928ad2d0a5b747627e")
LOG_GROUP = getenv("LOG_GROUP", "")
MONGO_DB = getenv("MONGO_DB", "")
ALIVE_IMG = getenv("ALIVE_IMG", "")
DB_URL = getenv("DATABASE_URL", "")
STRING_SESSION1 = getenv("STRING_SESSION1", "")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
STRING_SESSION11 = getenv("STRING_SESSION11", "")
STRING_SESSION12 = getenv("STRING_SESSION12", "")
STRING_SESSION13 = getenv("STRING_SESSION13", "")
STRING_SESSION14 = getenv("STRING_SESSION14", "")
STRING_SESSION15 = getenv("STRING_SESSION15", "")
STRING_SESSION16 = getenv("STRING_SESSION16", "")
STRING_SESSION17 = getenv("STRING_SESSION17", "")
STRING_SESSION18 = getenv("STRING_SESSION18", "")
STRING_SESSION19 = getenv("STRING_SESSION19", "")
STRING_SESSION20 = getenv("STRING_SESSION20", "")
STRING_SESSION21 = getenv("STRING_SESSION21", "")
STRING_SESSION22 = getenv("STRING_SESSION22", "")
STRING_SESSION23 = getenv("STRING_SESSION23", "")
STRING_SESSION24 = getenv("STRING_SESSION24", "")
STRING_SESSION25 = getenv("STRING_SESSION25", "")
STRING_SESSION26 = getenv("STRING_SESSION26", "")
STRING_SESSION27 = getenv("STRING_SESSION27", "")
STRING_SESSION28 = getenv("STRING_SESSION28", "")
STRING_SESSION29 = getenv("STRING_SESSION29", "")
STRING_SESSION30 = getenv("STRING_SESSION30", "")
STRING_SESSION31 = getenv("STRING_SESSION31", "")
STRING_SESSION32 = getenv("STRING_SESSION32", "")
STRING_SESSION33 = getenv("STRING_SESSION33", "")
STRING_SESSION34 = getenv("STRING_SESSION34", "")
STRING_SESSION35 = getenv("STRING_SESSION35", "")
STRING_SESSION36 = getenv("STRING_SESSION36", "")
STRING_SESSION37 = getenv("STRING_SESSION37", "")
STRING_SESSION38 = getenv("STRING_SESSION38", "")
STRING_SESSION39 = getenv("STRING_SESSION39", "")
STRING_SESSION40 = getenv("STRING_SESSION40", "")
STRING_SESSION41 = getenv("STRING_SESSION41", "")
STRING_SESSION42 = getenv("STRING_SESSION42", "")
STRING_SESSION43 = getenv("STRING_SESSION43", "")
STRING_SESSION44 = getenv("STRING_SESSION44", "")
STRING_SESSION45 = getenv("STRING_SESSION45", "")
STRING_SESSION46 = getenv("STRING_SESSION46", "")
STRING_SESSION47 = getenv("STRING_SESSION47", "")
STRING_SESSION48 = getenv("STRING_SESSION48", "")
STRING_SESSION49 = getenv("STRING_SESSION49", "")
STRING_SESSION50 = getenv("STRING_SESSION50", "")

