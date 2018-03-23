import discord


async def ex(args, message, bot, invoke):
    if message.guild:
        role = discord.utils.find(lambda x: x.id == 376195917407191040, message.guild.roles)
        if role:
            if role.id in [y.id for y in message.author.roles]:
                if args:
                    if message.mentions:
                        mentor_role = discord.utils.find(lambda x: x.id == 376195755482021888, message.guild.roles)
                        if mentor_role:
                            if mentor_role.id in [y.id for y in message.author.roles]:
                                target = message.mentions[0]
                                a = open('lists/mentors.txt')
                                output = []
                                for line in a:
                                    if f'{target.id}' not in line.lower():
                                        output.append(line)
                                a.close()
                                a = open('lists/mentors.txt', 'w')
                                a.writelines(output)
                                a.close()
                                await target.remove_roles(mentor_role)
                                response = discord.Embed(title=f"✅ {target.display_name} is no longer a Mentor", color=0x77b255)
                            else:
                                response = discord.Embed(title="❗ That user wasn't a Mentor", color=0xBE1931)
                        else:
                            response = discord.Embed(title=f'🔍 I couldn\'t find the Mentor role', color=0x696969)
                    else:
                        response = discord.Embed(title='❗ A user mention required', color=0xBE1931)
                else:
                    response = discord.Embed(title="❗ No input", color=0xBE1931)
            else:
                response = discord.Embed(title="⛔ Access denied: Head Mentor required", color=0xBE1931)
        else:
            response = discord.Embed(title=f'🔍 I couldn\'t find the Head Mentor role', color=0x696969)
    else:
        response = discord.Embed(title='🔒 You can\'t use that command in a DM', color=0xFFCC4d)
    await message.channel.send(embed=response)
