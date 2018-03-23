import discord


async def ex(args, message, bot, invoke):
    if message.guild:
        if args:
            if message.mentions:
                pronoun = 'you' if message.mentions[0].id == message.author.id else 'them'
                if len(args) >= 2:
                    user = args[0]
                    zone = ' '.join(args[1:])
                    with open('lists/requests.txt', 'a') as a:
                        a.write(f'`{zone}`: {user}\n')
                    response = discord.Embed(title=f"✅ I put {pronoun} on the 'Student Requests' list", color=0x77B255)
                else:
                    response = discord.Embed(title='❗ Not enough arguments', color=0xBE1931)
            else:
                response = discord.Embed(title='❗ A user mention required', color=0xBE1931)
        else:
            response = discord.Embed(title="❗ No input", color=0xBE1931)
    else:
        response = discord.Embed(title='🔒 You can\'t use that command in a DM', color=0xFFCC4d)
    await message.channel.send(embed=response)
