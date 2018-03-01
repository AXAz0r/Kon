import discord


async def ex(args, message, bot, invoke):
    await message.delete()
    if args:
        all_qry = ' '.join(args)
        if all_qry.endswith(';'):
            all_qry = all_qry[:-1]
        url_string = all_qry.split('; ')[-1]
        link_name = '; '.join(all_qry.split('; ')[:-1])
        if link_name is not '':
            if "http" in url_string:
                response = discord.Embed(description=f'🌐 [{link_name}]({url_string})', color=0x5DBCD2)
            else:
                response = discord.Embed(title='❗ URL must include http/s', color=0xBE1931)
        else:
            response = discord.Embed(title='❗ Separate the hyperlink text from the URL with ; then a space',
                                     color=0xBE1931)
    else:
        response = discord.Embed(title='❗ No input', color=0xBE1931)
    await message.channel.send(embed=response)
