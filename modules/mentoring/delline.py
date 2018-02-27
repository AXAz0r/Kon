import discord


async def ex(args, message, bot, invoke):
    try:
        role = discord.utils.find(lambda x: x.name.lower() == 'head mentor', message.guild.roles)
        if role.id in [y.id for y in message.author.roles]:
            if message.mentions:
                target = "%s" % message.mentions[0].id
            else:
                msg = ' '.join(args)
                target = msg.lower()
            fn = 'lists/requests.txt'
            a = open(fn)
            output = []
            temp = 0
            for line in a:
                if target not in line:
                    output.append(line)
                else:
                    temp += 1
            a.close()
            a = open(fn, 'w')
            a.writelines(output)
            a.close()
            if not temp == 0:
                response = discord.Embed(title="📝 Updated", color=0xA5FFF6)
            else:
                response = discord.Embed(title="❗ I couldn\'t find that line", color=0xBE1931)
        else:
            response = discord.Embed(title="⛔ Access denied: Head Mentor required", color=0xBE1931)
    except AttributeError:
        response = discord.Embed(title="❗ I couldn\'t find the role 'Head Mentor'")
    await message.channel.send(embed=response)
