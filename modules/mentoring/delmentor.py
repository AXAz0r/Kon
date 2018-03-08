import discord


async def ex(args, message, bot, invoke):
    try:
        target = discord.utils.find(lambda x: x.name.lower() == 'head mentor', message.guild.roles)
        if target.id in [y.id for y in message.author.roles]:
            fn = 'lists/mentors.txt'
            target = message.mentions[0]
            a = open(fn)
            output = []
            temp = 0
            for line in a:
                if f'{target.id}' not in line:
                    output.append(line)
                else:
                    temp += 1
            a.close()
            a = open(fn, 'w')
            a.writelines(output)
            a.close()
            mentor_role = discord.utils.get(message.guild.roles, name='Mentor')
            await target.remove_roles(mentor_role)
            if not temp == 0:
                response = discord.Embed(title=f"✅ {target.display_name} is no longer a Mentor", color=0x77b255)
            else:
                response = discord.Embed(title="❗ That user wasn't a Mentor", color=0xBE1931)
        else:
            response = discord.Embed(title="⛔ Access denied: Head Mentor required", color=0xBE1931)
    except AttributeError:
        response = discord.Embed(title="❗ I couldn't find the role 'Head Mentor'", color=0xBE1931)
    await message.channel.send(embed=response)
