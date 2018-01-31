import discord


async def ex(args, message, bot, invoke):
    if message.channel.id == 404728021216526348:
        with open('lists/requests.txt', 'a') as a:
            msg = ' '.join(args)
            a.write('%s' % msg + '\n')
        embed = discord.Embed(title="✅ I put you on the 'Student Requests' list!", color=0xA5FFF6)
    else:
        embed = discord.Embed(title="⛔ Please use the mentor-chat channel for that command", color=0xBE1931)
    await message.channel.send(embed=embed)
