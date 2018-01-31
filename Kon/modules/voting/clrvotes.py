import os
import discord
from checks import server_check


async def ex(args, message, bot, invoke):
    if server_check(message):
        if message.author.permissions_in(message.channel).administrator:
            if os.path.exists('lists/vote_data.json'):
                os.remove('lists/vote_data.json')
            response = discord.Embed(title='🗑️ Cleared', color=0xA5FFF6)
        else:
            response = discord.Embed(title='⛔ Access denied: Administrator required', color=0xBE1931)
    else:
        response = discord.Embed(title='🔒 You can\'t use that command on this server', color=0xFFCC4d)
    await message.channel.send(embed=response)
