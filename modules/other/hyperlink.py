import discord


async def ex(args, message, bot, invoke):
    await message.delete()
    link_name = ' '.join(args[1:])
    url_string = args[0].lower()
    response = discord.Embed(description=f'[{link_name}]({url_string})')
    await message.channel.send(embed=response)
