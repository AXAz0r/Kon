import discord


async def ex(args, message, bot, invoke):
    response = discord.Embed(description=f"`🏓 {int(bot.latency * 1000)}ms`", color=0xA5FFF6)
    await message.channel.send(embed=response)
