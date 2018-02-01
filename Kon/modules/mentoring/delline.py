import discord


async def ex(args, message, bot, invoke):
    role = discord.utils.find(lambda x: x.name.lower() == 'head mentor', message.guild.roles)
    try:
        if role.id in [y.id for y in message.author.roles]:
            if message.mentions:
                target = message.mentions[0].id
            else:
                msg = ' '.join(args)
                target = msg.lower()
            fn = 'lists/requests.txt'
            a = open(fn)
            output = []
            for line in a:
                if target not in line:
                    output.append(line)
            a.close()
            a = open(fn, 'w')
            a.writelines(output)
            a.close()
            response = discord.Embed(title="📝 Updated", color=0xA5FFF6)
        else:
            response = discord.Embed(title="⛔ Access denied: Head Mentor required", color=0xBE1931)
    except AttributeError:
        response = discord.Embed(title="❗ I couldn\'t find the role 'Head Mentor'")
    await message.channel.send(embed=response)
