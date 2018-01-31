import discord


async def ex(args, message, bot, invoke):
    embed = discord.Embed(title=':information_source: GitHub for Kon:', color=0xA5FFF6)
    embed.description = 'https://github.com/Shifty6/Kon'
    await message.channel.send(embed=embed)
