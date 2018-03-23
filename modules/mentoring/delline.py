import discord


async def ex(args, message, bot, invoke):
    if message.guild:
        role = discord.utils.find(lambda x: x.id == xxxxxxxxxxxxxxxxxx, message.guild.roles)
        if role:
            if role.id in [y.id for y in message.author.roles]:
                if args:
                    if message.mentions:
                        target = message.mentions[0].id
                    else:
                        msg = ' '.join(args)
                        target = msg.lower()
                    fn = 'lists/requests.txt'
                    a = open(fn)
                    output = []
                    temp = 0
                    for line in a:
                        if f'{target}' not in line.lower():
                            output.append(line)
                        else:
                            temp += 1
                    a.close()
                    a = open(fn, 'w')
                    a.writelines(output)
                    a.close()
                    if not temp == 0:
                        response = discord.Embed(title="📝 Updated", color=0xccd6dd)
                    else:
                        response = discord.Embed(title="❗ I couldn't find that line", color=0xBE1931)
                else:
                    response = discord.Embed(title="❗ No input", color=0xBE1931)
            else:
                response = discord.Embed(title="⛔ Access denied: Head Mentor required", color=0xBE1931)
        else:
            response = discord.Embed(title=f'🔍 I couldn\'t find the Head Mentor role', color=0x696969)
    else:
        response = discord.Embed(title='🔒 You can\'t use that command in a DM', color=0xFFCC4d)
    await message.channel.send(embed=response)
