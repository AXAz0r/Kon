import logging
import os
import json
import discord
import secrets
from checks import ban_check, member_check, private_check, role_check, server_check
from modules.mentoring import addmentor, apply, delline, delmentor, mentors, requests
from modules.other import commands_help, dance, help, info, kon, link, match, members, \
     mute, ping, purge, random, roll, sleep, unmute
from modules.owner import reboot, setavatar, setstatus, setusername
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
    await bot.process_commands(message


commands_list = {
    "addmentor": addmentor,
    "apply": apply,
    "commands": commands_help,
    "clrperms": clrperms,
    "clrvotes": clrvotes,
    "dance": dance,
    "delline": delline,
    "delmentor": delmentor,
    "help": help,
    "info": info,
    "kon": kon,
    "link": link,
    "match": match,
    "members": members,
    "mentors": mentors,
    "mute": mute,
    "ping": ping,
    "permit": permit,
    "perms": perms,
    "purge": purge,
    "random": random,
    "reboot": reboot,
    "register": register,
    "requests": requests,
    "roll": roll,
    "setavatar": setavatar,
    "setstatus": setstatus,
    "setusername": setusername,
    "setpassword": setpassword,
    "sleep": sleep,
    "unmute": unmute,
    "unpermit": unpermit,
    "vote": vote,
    "voters": voters,
    "votes": votes,
}


@bot.event
async def on_message(message):
    if message.author.id == 216437513709944832:
        tables = ['┬─┬ ノ( ^_^ノ)',
                 '┬─┬ ﾉ(° -°ﾉ)',
                 '┬─┬ ノ(゜-゜ノ)',
                 '┬─┬ ノ(ಠ\_ಠノ)',
                 '┻━┻~~~~  ╯(°□° ╯)',
                 '┻━┻====  ╯(°□° ╯)',
                 '┬──┬﻿ ¯\_(ツ)',
                 '(ヘ･_･)ヘ┳━┳',
                 'ヘ(´° □°)ヘ┳━┳']
        for table in tables:
            if table in message.content:
                await message.channel.send('(╯°□°）╯︵ ┻━┻')
    if not message.author.bot:
        if message.content.startswith(cfg["Prefix"]):
            invoke = message.content.lower()[len(cfg["Prefix"]):].split(" ")[0]
            args = message.content.split(" ")[1:]
            if invoke in commands_list:
                try:
                    await commands_list.get(invoke).ex(args, message, bot, invoke)
                except discord.Forbidden:
                    await message.add_reaction(emoji='❗')
        chars = ['natsuki', 'sayori', 'yuri']
        for char in chars:
            if char in message.content.lower():
                await message.add_reaction(emoji=':monika:375824498882117635')
        if message.content.lower() == 'f':
            await message.add_reaction(emoji='🇫')
        channels = [xxxxxxxxxxxxxxxxxx]
        if message.channel.id in channels:
            ban = ban_check(message)
            if ban:
                await message.add_reaction(emoji='⛔')
        if role_check(message):
            if not member_check(message):
                role = role_check(message)
                target = message.mentions[0]
                clan_role = discord.utils.get(message.guild.roles, name=f'{role}')
                recruit_role = discord.utils.get(message.guild.roles, name='Recruit')
                await target.add_roles(clan_role)
                await target.remove_roles(recruit_role)


bot.run(cfg["Token"], bot=True)
