import json
import discord


with open('config.json') as json_data_file:
    cfg = json.load(json_data_file)


def owner_check(message):
    if message.author.id in cfg["OwnerID"]:
        owner = True
    else:
        owner = False
    return owner


def server_check(message):
    if message.guild.id in cfg["Servers"]:
        server = True
    else:
        server = False
    return server


def private_check(ctx):
    return isinstance(ctx.channel, discord.abc.PrivateChannel)
