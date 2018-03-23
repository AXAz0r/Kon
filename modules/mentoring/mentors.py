import discord


async def ex(args, message, bot, invoke):
    role_search = discord.utils.find(lambda x: x.id == xxxxxxxxxxxxxxxxxx, message.guild.roles)
    if role_search:
        mentors = ''
        for member in message.guild.members:
            member_role_search = discord.utils.find(lambda x: x.id == role_search.id, member.roles)
            if member_role_search:
                mentors += f'{member.mention}\n'
        response = discord.Embed(color=role_search.color)
        response.add_field(name='🎓 Mentors', value=f'{mentors}')
    else:
        response = discord.Embed(title=f'🔍 I couldn\'t find the Mentor role', color=0x696969)
    await message.channel.send(embed=response)
