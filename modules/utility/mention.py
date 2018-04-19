import discord


async def ex(args, message, bot, invoke):
    if message.guild:
        if message.author.guild_permissions.manage_messages:
            if args:
                lookup = ' '.join(args[0:]).lower()
                role_search = discord.utils.find(lambda x: x.name.lower() == lookup, message.guild.roles)
                if role_search:
                    await message.delete()
                    await role_search.edit(mentionable=True)
                    await message.channel.send(role_search.mention)
                    await role_search.edit(mentionable=False)
                else:
                    message.add_reaction('🔍')
            else:
                message.add_reaction('❗')
        else:
            message.add_reaction('⛔')
    else:
        await message.channel.send(embed=discord.Embed(title='🔒 You can\'t use that command in a DM', color=0xFFCC4d))
        
