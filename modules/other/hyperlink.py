import discord


async def ex(args, message, bot, invoke):
    await message.delete()
    link_name = ' '.join(args[1:])
    url_string = args[0].lower()
    if "http" in url_string:
        response = discord.Embed(description=f'🌐 [{link_name}]({url_string})', color=0x5DBCD2)
    else:
        response = discord.Embed(title='❗ URL must include http/s', color=0xBE1931)
    await message.channel.send(embed=response)
