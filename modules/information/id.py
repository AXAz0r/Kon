import discord


async def ex(args, message, bot, invoke):
    if args:
        if message.mentions:
            target = message.mentions[0]
        elif message.channel_mentions:
            target = message.channel_mentions[0]
        else:
            qry = ' '.join(args).lower()
            role_search = discord.utils.find(lambda x: x.name.lower() == qry, message.guild.roles)
            if role_search:
                target = role_search
            else:
                response = discord.Embed(title=f'🔍 I couldn\'t find {qry} on this server', color=0x696969)
                await message.channel.send(embed=response)
                return
    else:
        target = message.author
    await message.channel.send(target.id)
