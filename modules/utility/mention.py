import discord


def mention_check(message, args):
    if message.channel_mentions:
        post_qry = (' '.join(args)).split(':: ')
        slices = post_qry[1].split()
        return slices[0] == message.channel_mentions[0].mention


async def ex(args, message, bot, invoke):
    if message.guild:
        if message.author.guild_permissions.manage_messages:
            if args:
                if '::' in message.content:
                    post_qry = (' '.join(args)).split(':: ')
                    lookup = ''.join(post_qry[0]).lower()
                    if mention_check(message, args):
                        chn = post_qry[1].split()
                        output = f"\n{' '.join(chn[1:])}"
                        target = message.channel_mentions[0]
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
