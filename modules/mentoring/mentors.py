import discord


async def ex(args, message, bot, invoke):
    with open('lists/mentors.txt', 'r+') as file:
        a = file.read()
    embed = discord.Embed(title="**Mentors:**", color=0xA5FFF6)
    embed.description = ('%s' % a)
    await message.channel.send(embed=embed)
