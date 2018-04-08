import os
import discord
from checks import server_check


async def ex(args, message, bot, invoke):
    if message.guild:
        if server_check(message):
            if message.author.permissions_in(message.channel).manage_guild:
                if os.path.exists('lists/vote_data.json'):
                    os.remove('lists/vote_data.json')
                response = discord.Embed(title='🗑️ Cleared', color=0x67757f)
            else:
                response = discord.Embed(title='⛔ Access denied: Manage Server required', color=0xBE1931)
        else:
            response = discord.Embed(title='🔒 You can\'t use that command on this server', color=0xFFCC4d)
    else:
        response = discord.Embed(title='🔒 You can\'t use that command in a DM', color=0xFFCC4d)
    await message.channel.send(embed=response)
