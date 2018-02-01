import logging
import os
import json
import discord
import secrets
from spreadsheet import ban_check
from modules.mentoring import addmentor, apply, delline, delmentor, mentors, requests
from modules.moderative import purge, raidban, raidbans, reboot, unraidban
from modules.other import commands, dance, help, info, modules, ping, roll, sleep
from modules.voting import clrperms, clrvotes, permit, perms, register, setpassword, unpermit, vote, voters, votes
from discord.ext import commands


logging.basicConfig(level=logging.INFO)


os.chdir(os.path.dirname(os.path.realpath(__file__)))
with open('config.json') as json_data_file:
    cfg = json.load(json_data_file)


bot = commands.Bot(command_prefix=cfg["Prefix"])
bot.remove_command('help')


@bot.event
async def on_ready():
    print('Bot ready.')


async def on_message(message):
    await bot.process_commands(message)
    await bot.change_presence(game=discord.Game(name='^help for help'))


commands = {
    "addmentor": addmentor,
    "apply": apply,
    "delline": delline,
    "delmentor": delmentor,
    "mentors": mentors,
    "requests": requests,
    "purge": purge,
    "raidban": raidban,
    "raidbans": raidbans,
    "reboot": reboot,
    "unraidban": unraidban,
    "commands": commands,
    "dance": dance,
    "help": help,
    "info": info,
    "modules": modules,
    "ping": ping,
    "roll": roll,
    "sleep": sleep,
    "clrperms": clrperms,
    "clrvotes": clrvotes,
    "permit": permit,
    "perms": perms,
    "register": register,
    "setpassword": setpassword,
    "unpermit": unpermit,
    "vote": vote,
    "voters": voters,
    "votes": votes,
}


@bot.event
async def on_message(message):
    if message.content.startswith(cfg["Prefix"]):
        invoke = message.content.lower()[len(cfg["Prefix"]):].split(" ")[0]
        args = message.content.split(" ")[1:]
        if commands.__contains__(invoke):
            await commands.get(invoke).ex(args, message, bot, invoke)
    flipped_table = '(╯°□°）╯︵ ┻━┻'
    if flipped_table in message.content:
        table = ['┬─┬ ノ( ^_^ノ)',
                 '┬─┬ ﾉ(° -°ﾉ)',
                 '┬─┬ ノ(゜-゜ノ)',
                 '┬─┬ ノ(ಠ\_ಠノ)',
                 '┻━┻~~~~  ╯(°□° ╯)',
                 '┻━┻====  ╯(°□° ╯)',
                 ' ┬──┬﻿ ¯\_(ツ)',
                 '(ヘ･_･)ヘ┳━┳',
                 'ヘ(´° □°)ヘ┳━┳']
        table_resp = secrets.choice(table)
        await message.channel.send(table_resp)
    elif 'natsuki' in message.content.lower():
        await message.add_reaction(emoji='🔪')
    elif 'sayori' in message.content.lower():
        await message.add_reaction(emoji='🔪')
    elif 'yuri' in message.content.lower():
        await message.add_reaction(emoji='🔪')
    elif message.content.lower() == 'f':
        await message.add_reaction(emoji='🇫')
    channels = [xxxxxxxxxxxxxxxxxxxx, xxxxxxxxxxxxxxxxxxxx]
    if message.channel.id in channels:
        ban = ban_check(message)
        if ban:
            await message.add_reaction(emoji='⛔')


bot.run(cfg["Token"], bot=True)
