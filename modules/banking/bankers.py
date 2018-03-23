import discord


async def ex(args, message, bot, invoke):
    role_search = discord.utils.find(lambda x: x.id == xxxxxxxxxxxxxxxxxx, message.guild.roles)
    if role_search:
        bankers = ''
        for member in message.guild.members:
            member_role_search = discord.utils.find(lambda x: x.id == role_search.id, member.roles)
            if member_role_search:
                bankers += f'- {member.name}#{member.discriminator}\n'
        response = discord.Embed(color=0xC16A4F)
        response.add_field(name='💰 Bankers', value=f'```md\n{bankers}\n```')
    else:
        response = discord.Embed(title=f'🔍 I couldn\'t find the Banker role', color=0x696969)
    await message.channel.send(embed=response)
