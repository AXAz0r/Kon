import logging
import os
import json
import discord
import secrets
from checks import ban_check, member_check, role_check, server_check
from modules.banking import additem, bankers, delitem, market, setqty
from modules.information import members, help, info, commands_help, ping, rolepop, user
from modules.mentoring import addmentor, apply, delline, delmentor, mentors, requests
from modules.owner import reboot, setavatar, setstatus, setusername
from modules.utility import dance, kon, link, match, mute, purge, random, roll, sleep, unmute
from modules.voting import clrperms, clrvotes, password, permit, perms, setpassword, unpermit, vote, voters, votes
from discord.ext import commands


logging.basicConfig(level=logging.INFO)


os.chdir(os.path.dirname(os.path.realpath(__file__)))
with open('config.json') as json_data_file:
    cfg = json.load(json_data_file)


bot = commands.Bot(command_prefix=cfg["Prefix"])
bot.remove_command('help')


@bot.event
async def on_ready():
    activity = discord.Activity(type=discord.ActivityType.playing, name=cfg['Status'])
    await bot.change_presence(activity=activity)
    print('Bot ready.')


async def on_message(message):
    await bot.process_commands(message

                               
commands_list = {
    "additem": additem,
    "addmentor": addmentor,
    "apply": apply,
    "bankers": bankers,
    "commands": commands_help,
    "clrperms": clrperms,
    "clrvotes": clrvotes,
    "dance": dance,
    "delitem": delitem,
    "delline": delline,
    "delmentor": delmentor,
    "help": help,
    "info": info,
    "kon": kon,
    "link": link,
    "match": match,
    "market": market,
    "members": members,
    "mentors": mentors,
    "mute": mute,
    "password": password,
    "ping": ping,
    "permit": permit,
    "perms": perms,
    "purge": purge,
    "random": random,
    "reboot": reboot,
    "requests": requests,
    "rolepop": rolepop,
    "roll": roll,
    "setavatar": setavatar,
    "setstatus": setstatus,
    "setusername": setusername,
    "setpassword": setpassword,
    "sleep": sleep,
    "setqty": setqty,
    "unmute": unmute,
    "unpermit": unpermit,
    "user": user,
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
                except Exception as e:
                    if not message.content.lower().startswith(cfg['Prefix'] + 'reboot'):
                        await message.add_reaction(emoji='❗')
                        print(f'Exception: {e}')
                    else:
                        pass
        chars = ['natsuki', 'sayori', 'yuri']
        for char in chars:
            if char in message.content.lower():
                await message.add_reaction(emoji=':monika:375824498882117635')
        if message.content.lower() == 'f':
            await message.add_reaction(emoji='🇫')
        channels = [xxxxxxxxxxxxxxxxxx]
        if role_check(message):
            target = message.mentions[0]
            if target.id != message.author.id:
                if not member_check(message):
                    role = role_check(message)
                    rem_role = discord.utils.get(message.guild.roles, id=xxxxxxxxxxxxxxxxxxx)
                    add_role = discord.utils.get(message.guild.roles, id=role)
                    await target.remove_roles(rem_role, reason='Joined Clan')
                    await target.add_roles(add_role, reason='Joined Clan')
        if message.channel.id == xxxxxxxxxxxxxxxxxxx:
            if message.mentions:
                for target in message.mentions:
                    clan_roles = [xxxxxxxxxxxxxxxxxxx, xxxxxxxxxxxxxxxxxxx
                    user_roles = [y.id for y in target.roles]
                    if target.id != message.author.id:
                        for role in clan_roles:
                            if role in user_roles:
                                rem_role = discord.utils.get(message.guild.roles, id=role)
                                await target.remove_roles(rem_role, reason='Left Clan')
                        add_role = discord.utils.get(message.guild.roles, xxxxxxxxxxxxxxxxxxx
                        await target.add_roles(add_role, reason='Left Clan')
        with open('lists/muted.txt', 'r') as file:
            mute_list = file.readlines()
        if message.guild:
            if server_check(message):
                for line in mute_list:
                    target = message.author.id
                    if f'{target}' in line.lower():
                        await message.delete()


bot.run(cfg["Token"], bot=True)
