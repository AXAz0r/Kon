import discord


async def ex(args, message, bot, invoke):
    bot_latency = round(bot.latency * 1000, 2)
    response = discord.Embed(description=f"`🏓 {bot_latency}ms`", color=0xA5FFF6)
    await message.channel.send(embed=response)
