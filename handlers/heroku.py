import math
import os

import heroku3
import requests
from pyrogram.errors import PeerIdInvalid
from pyrogram.types import Message


heroku_api = "https://api.heroku.com"

useragent = (
    "Mozilla/5.0 (Linux; Android 9; SM-G975F) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/80.0.3987.149 Mobile Safari/537.36"
)


if HEROKU_API and HEROKU_APP_NAME:
    heroku_app = heroku3.from_key(HEROKU_API).apps()[HEROKU_APP_NAME]
else:
    heroku_app = None


# shut-down dyno
@Client.on_message(filters.command('shutdown', ["."]) & filters.me)
async def shutdown_handler(client: Client, message: Message):
    if await not_heroku(message):
        return

    try:
        await client.send_message(
            client.LOG_GROUP,
            "#shutdown \n"
            "Bot is now turned off !!\nTurn it on manually on heroku.com",
        )
    except PeerIdInvalid:
        pass
    try:
        await message.edit("Dynos are truned off, if you want turn them on manually from heroku.com")
        heroku_app.process_formation()["worker"].scale(0)
    except Exception as e:
        await message.edit(e)


# restart your bot
@Client.on_message(filters.command('restart', ["."]) & filters.me)
async def restart_handler(client: Client, message: Message):
    if await not_heroku(message):
        return

    try:
        m = await message.edit("Restarting . . .")
        restart = heroku_app.restart()
        if restart:
            await message.edit("Restarted . . .!\nPlease wait for 3 min or more to restart userbot . . .")
        else:
            await message.edit("Failed to restart userbot, try again later . . .")
    except Exception as e:
        await message.edit(e)


# get usage of your dyno hours from heroku
@Client.on_message(filters.command('usage', ["."]) & filters.me)
async def dynostats_handler(client: Client, message: Message):
    if await not_heroku(message):
        return

    Heroku = heroku3.from_key(HEROKU_API)
    m = await message.edit("Checking usage . . .")
    u_id = Heroku.account().id
    try:
        if u_id:
            headers = {
                "User-Agent": useragent,
                "Authorization": f"Bearer {HEROKU_API}",
                "Accept": "application/vnd.heroku+json; version=3.account-quotas",
            }
            path = "/accounts/" + u_id + "/actions/get-quota"
            r = requests.get(heroku_api + path, headers=headers)
            if r.status_code != 200:
                return await message.edit("Error: something bad happened`\n\n" f"> {r.reason}\n")
            result = r.json()
            quota = result["account_quota"]
            quota_used = result["quota_used"]
            # used hours
            remaining_quota = quota - quota_used
            percentage = math.floor(remaining_quota / quota * 100)
            minutes_remaining = remaining_quota / 60
            hours = math.floor(minutes_remaining / 60)
            minutes = math.floor(minutes_remaining % 60)
            # remaining
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

            await message.edit(
                "**Dyno Usage**:\n\n"
                f"**Total Dyno Hours:** `550 Hours`\n\n"
                f"**⧓ Dyno usage for App:** __`{HEROKU_APP_NAME}`__\n"
                f"\r• `{AppHours}h {AppMinutes}m`"
                f"**|**  [ `{AppPercentage}`**%** ]\n\n"
                f"**⧓ Quota remaining this month:**\n"
                f"\r• `{hours} Hours & {minutes} Mins`"
                f" |  [ `{percentage}%` ]",
            )
    except Exception as e:
        await message.edit(e)


# get list of vars from heroku
@Client.on_message(filters.command('vars', ["."]) & filters.me)
async def herokuvars_handler(client: Client, message: Message):
    if await not_heroku(message):
        return

    try:
        m = await message.edit("Fetching all vars from Heroku . . .")
        heroku_vars = heroku_app.config()
        vars_dict = heroku_vars.to_dict()
        vars_keys = list(vars_dict.keys())
        msg = "**All Heroku Vars:**\n\n"
        num = 0
        for i in vars_keys:
            num += 1
            msg += f"**{num}**: `{i}`\n"

        msg += f"\n**Total `{num}` vars found.**"
        await message.edit(msg)
    except Exception as e:
        await message.edit(e)


# set vars in heroku
@Client.on_message(filters.command('setvar', ["."]) & filters.me)
async def setvar_handler(client: Client, message: Message):
    if await not_heroku(message):
        return

    if client.long(message) < 3:
        await message.edit(f"`{app.PREFIX}setvar [key] [value]`")
    elif client.long(message) >= 3:
        key = message.command[1]
        value = message.command[2]
        heroku_vars = heroku_app.config()
        try:
            if key and value in heroku_vars:
                await message.edit(f"{key} is already in vars with value {value}")
            elif not key in heroku_vars:
                await message.edit(f"Added var •> `{key}` = `{value}`", disable_web_page_preview=True)
                heroku_vars[key] = value
            else:
                await message.edit("Something went wrong, try again later !")
        except Exception as e:
            await message.edit(e)


# get vars from heroku vars
@Client.on_message(filters.command('getvar', ["."]) & filters.me)
async def getvar_handler(client: Client, message: Message):
    if await not_heroku(message):
        return

    if client.long(message) == 1:
        return await message.edit(f"`{app.PREFIX}getvar [key name]`")
    elif client.long(message) >= 2:
        key = message.command[1]
        heroku_vars = heroku_app.config()
        try:
            if heroku_vars:
                await message.edit(f"**Key exists:**\n\n`{key}` = `{heroku_vars[key]}`")
            else:
                await message.edit("Failed to get heroku key . . .")
        except Exception as e:
            await message.edit(e)


# delete vars in heroku
@Client.on_message(filters.command('delvar', ["."]) & filters.me)
async def delvar_handler(client: Client, message: Message):
    if await not_heroku(message):
        return

    if client.long(message) == 1:
        return await message.edit(f"{app.PREFIX}delvar [key name]")
    elif client.long(message) >= 2:
        message = await message.edit("Verifying var in heroku config vars . . .")
        key = message.command[1]
        heroku_vars = heroku_app.config()

        if key not in heroku_vars:
            return await message.edit(f"**`{key}`** does not exist in heroku vars . . .")

        try:
            del heroku_vars[key]
        except Exception as e:
            return await message.edit(e)
        await message.edit(f"Successfully deleted var = [ {key} ] from heroku vars !")
    else:
        await message.edit(f"Usage: `{app.PREFIX}delvar [key name]` use this format.")


# get logs from heroku in file format (.txt)
@Client.on_message(filters.command('logs', ["."]) & filters.me)
async def logs_handler(client: Client, message: Message):
    if await not_heroku(message):
        return

    m = await message.edit("⏳ • hold on . . .")
    logsdata = heroku_app.get_log()
    if logsdata:
        try:
            filename = f"./downloads/{app.username}_logs.txt"
            file = open(filename, "w+")
            file.write(logsdata)
            file.close()
            await client.send_document(
                m.chat.id, filename, caption=f"Uploaded By: {app.UserMention()}"
            )
            if os.path.exists(filename):
                os.remove(filename)
            await m.delete()
        except Exception as e:
            await message.edit(e)
    else:
        await message.edit("Failed to get logs . . .")


# get logs from heroku in nekobin link, not as a file
@Client.on_message(filters.command('textlogs', ["."]) & filters.me)
async def textlogs_handler(client: Client, message: Message):
    if await not_heroku(message):
        return

    m = await message.edit("⏳ • hold on . . . ")
    logsdata = heroku_app.get_log()
    if logsdata:
        try:
            url = await client.HasteBinPaste(logsdata)
            text = f"Heroku Logs: [press here]({url})"
            await message.edit(text, disable_web_page_preview=True)
        except Exception as e:
            await message.edit(e)
    else:
        await message.edit(f"Failed to get the heroku text logs, try `{app.PREFIX.split()[0]}logs` command.")


async def not_heroku(message: Message):
    if not (HEROKU_APP_NAME and HEROKU_API):
        return await message.edit("Please fill heroku credentials for this command to work [`HEROKU_APP_NAME`, `HEROKU_API_KEY`")
        return True
    return False
