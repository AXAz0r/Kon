import discord


async def ex(args, message, bot, invoke):
    if args:
        lookup = args[0].lower()
        if message.mentions:
            target = message.mentions[0].id
        elif message.channel_mentions:
            target = message.channel_mentions[0].id
        elif lookup == 'server':
            target = message.guild.id
        elif ':' in lookup:
            split_args = lookup.split(':')
            if len(split_args) > 2:
                emote_id = split_args[2][:-1]
                if str.isdigit(emote_id):
                    target = int(emote_id)
                else:
                    target = None
            else:
                target = None
        else:
            qry = ' '.join(args).lower()
            role_search = discord.utils.find(lambda x: x.name.lower() == qry, message.guild.roles)
            if role_search:
                target = role_search.id
            else:
                target = None
    else:
        target = message.author.id
    if target:
        await message.channel.send(target)
    else:
        response = discord.Embed(title=f'🔍 I couldn\'t find the ID for that', color=0x696969)
        await message.channel.send(embed=response)
