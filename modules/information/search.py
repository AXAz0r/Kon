import discord


async def ex(args: list, message: discord.Message, bot, invoke):
    if args:
        lookup = '%20'.join(args)
        ddg_icon = 'https://i.imgur.com/vIjGX9L.png'
        query_url = f'https://duckduckgo.com/html/?q={lookup}'
        response = discord.Embed(color=0xE04f25)
        response.set_author(name='Search Results', icon_url=ddg_icon, url=query_url)
    else:
        response = discord.Embed(title='❗ No search inputted.', color=0xBE1931)
    await message.channel.send(embed=response)
