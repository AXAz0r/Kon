import discord


async def ex(args, message, bot, invoke):
    try:
        target = discord.utils.find(lambda x: x.name.lower() == 'head mentor', message.guild.roles)
        if target.id in [y.id for y in message.author.roles]:
            if len(args) >= 3:
                user = args[0]
                zone = args[1]
                time = args[2]
                target = message.mentions[0]
                a = open('lists/mentors.txt', 'a')
                a.write(f'`{zone} {time}`: {user}' + '\n')
                a.close()
                mentor_role = discord.utils.get(message.guild.roles, name='Mentor')
                await target.add_roles(mentor_role)
                response = discord.Embed(title=f"✅ {target.display_name} is now a Mentor", color=0xA5FFF6)
            else:
                response = discord.Embed(title='❗ Not enough inputs', color=0xBE1931)
                response.set_footer(text='@Username UTC #')
        else:
            response = discord.Embed(title="⛔ Access denied: Head Mentor required", color=0xBE1931)
    except AttributeError:
        response = discord.Embed(title="❗ I couldn\'t find the role 'Head Mentor'", color=0xBE1931)
    await message.channel.send(embed=response)
