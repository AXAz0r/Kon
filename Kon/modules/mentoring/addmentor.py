import discord


async def ex(args, message, bot, invoke):
    try:
        target = discord.utils.find(lambda x: x.name.lower() == 'head mentor', message.guild.roles)
        if target.id in [y.id for y in message.author.roles]:
            target = message.mentions[0]
            msg = ' '.join(args)
            a = open('lists/mentors.txt', 'a')
            a.write('%s' % msg + '\n')
            a.close()
            mentor_role = discord.utils.get(message.guild.roles, name='Mentor')
            await target.add_roles(mentor_role)
            response = discord.Embed(title=f"✅ {target.display_name} is now a Mentor", color=0xA5FFF6)
        else:
            response = discord.Embed(title="⛔ Access denied: Head Mentor required", color=0xBE1931)
    except AttributeError:
        response = discord.Embed(title="❗ I couldn\'t find the role 'Head Mentor'")
    await message.channel.send(embed=response)
