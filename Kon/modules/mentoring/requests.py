import discord


async def ex(args, message, bot, invoke):
    if message.channel.id == 376194194001100811:
        allow = True
    elif message.author.id == 208974392644861952:
        allow = True
    else:
        allow = False
    if not allow:
        embed = discord.Embed(title="⛔ Please use the mentor-chat channel for that command", color=0xBE1931)
    else:
        with open('lists/requests.txt', 'r') as file:
            a = file.read()
        embed = discord.Embed(title="**Student Requests:**", color=0xA5FFF6)
        embed.description = ('%s' % a)
    await message.channel.send(embed=embed)
