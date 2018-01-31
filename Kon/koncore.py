import logging
import os
import json
import discord
from modules.other import roll, sleep, ping, github, dance, help, modules, commands
from modules.moderative import purge, raidban, unraidban, raidbans, reboot
from modules.voting import voters, votes, vote, setpassword, permit, unpermit, register, perms, clrperms, clrvotes
from modules.mentoring import apply, requests, addmentor, delmentor, mentors, delline
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
    "sleep": sleep,
    "ping": ping,
    "reboot": reboot,
    "roll": roll,
    "voters": voters,
    "votes": votes,
    "vote": vote,
    "apply": apply,
    "setpassword": setpassword,
    "requests": requests,
    "github": github,
    "dance": dance,
    "purge": purge,
    "help": help,
    "addmentor": addmentor,
    "delmentor": delmentor,
    "delline": delline,
    "mentors": mentors,
    "raidban": raidban,
    "raidbans": raidbans,
    "unraidban": unraidban,
    "permit": permit,
    "unpermit": unpermit,
    "register": register,
    "perms": perms,
    "clrperms": clrperms,
    "clrvotes": clrvotes,
    "modules": modules,
    "commands": commands,
}


@bot.event
async def on_message(message):
    if message.content.startswith(cfg["Prefix"]):
        invoke = message.content.lower()[len(cfg["Prefix"]):].split(" ")[0]
        args = message.content.split(" ")[1:]
        if commands.__contains__(invoke):
            await commands.get(invoke).ex(args, message, bot, invoke)


bot.run(cfg["Token"], bot=True)
