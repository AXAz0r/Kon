import discord


def mention_check(message):
    chn_mention = False
    if message.channel_mentions:
        slices = message.content.split()
        if slices[0] == message.channel_mentions[0].mention:
            chn_mention = True
    return chn_mention, message.channel_mentions[0]


async def ex(args, message, bot, invoke):
    if message.guild:
        if message.author.guild_permissions.manage_messages:
            if args:
                if '::' in message.content:
                    all_qry = ' '.join(args)
                    post_qry = all_qry.split(':: ')
                    lookup = ''.join(post_qry[0]).lower()
                    if mention_check(message):
                        chn = post_qry[1].split()
                        output = f"\n{' '.join(chn[1:])}"
                        target = mention_check(message)[1]
                        title_end = f'#{target.name}'
                        await message.channel.send(embed=discord.Embed(color=0x77B255,
                                                                       title=f'✅ Message sent to {title_end}'))
                    else:
                        output = f"\n{' '.join(post_qry[1:])}"
                        target = message.channel
                else:
                    target = message.channel
                    lookup = ' '.join(args[0:]).lower()
                    output = ''
                role_search = discord.utils.find(lambda x: x.name.lower() == lookup, message.guild.roles)
                if role_search:
                    await message.delete()
                    await role_search.edit(mentionable=True)
                    await target.send(role_search.mention + output)
                    await role_search.edit(mentionable=False)
                else:
                    await message.add_reaction('🔍')
            else:
                await message.add_reaction('❗')
        else:
            await message.add_reaction('⛔')
    else:
        await message.channel.send(embed=discord.Embed(title='🔒 You can\'t use that command in a DM', color=0xFFCC4d))
