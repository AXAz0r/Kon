import discord


async def ex(args, message, bot, invoke):
    if message.guild:
        if message.author.guild_permissions.manage_messages:
            if args:
                if '::' in message.content:
                    all_qry = ' '.join(args)
                    post_qry = all_qry.split(':: ')
                    lookup = ''.join(post_qry[0]).lower()
                    output = f"\n {' '.join(post_qry[1:])}"
                else:
                    lookup = ' '.join(args[0:]).lower()
                    output = ''
                role_search = discord.utils.find(lambda x: x.name.lower() == lookup, message.guild.roles)
                if role_search:
                    await message.delete()
                    await role_search.edit(mentionable=True)
                    await message.channel.send(role_search.mention + output)
                    await role_search.edit(mentionable=False)
                else:
                    await message.add_reaction('🔍')
            else:
                await message.add_reaction('❗')
        else:
            await message.add_reaction('⛔')
    else:
        await message.channel.send(embed=discord.Embed(title='🔒 You can\'t use that command in a DM', color=0xFFCC4d))
