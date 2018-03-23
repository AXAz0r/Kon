import discord


async def ex(args, message, bot, invoke):
    with open('lists/mentors.txt', 'r') as file:
        mentors = file.read()
    response = discord.Embed(title='🎓 Mentors', description=f'{mentors}', color=0xFF0000)
    await message.channel.send(embed=response)
