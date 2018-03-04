import discord
from checks import owner_check


async def ex(args, message, bot, invoke):
    if owner_check(message):
        await message.channel.send(embed=discord.Embed(title="⚙ Rebooting", color=0x66757F))
        await bot.logout()
    else:
        await message.channel.send(embed=discord.Embed(title="⛔ You are not the owner", color=0xBE1931))
