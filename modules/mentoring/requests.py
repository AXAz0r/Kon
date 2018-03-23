import discord


async def ex(args, message, bot, invoke):
    with open('lists/requests.txt', 'r') as file:
        requests = file.read()
    response = discord.Embed(title="Student Requests", description=f'{requests}', color=0xA5FFF6)
    await message.channel.send(embed=response)
