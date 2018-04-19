import discord


async def ex(args, message, bot, invoke):
    response = discord.Embed(description=f"`🏓 {int(bot.latency * 1000)}ms`", color=0xAA2C15)
    await message.channel.send(embed=response)
