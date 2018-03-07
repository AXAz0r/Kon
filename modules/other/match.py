import discord
import secrets
import asyncio


async def ex(args, message, bot, invoke):
    matches = []
    members = [x for x in message.guild.members]
    for member in members:
        if message.mentions:
            value_one_one = int(str(message.mentions[0].id)[6])
            value_one_two = int(str(message.mentions[0].id)[9])
            pronouns = ['Their', 'their', 'They']
        else:
            value_one_one = int(str(message.author.id)[6])
            value_one_two = int(str(message.author.id)[9])
            pronouns = ['Your', 'your', 'You']
        value_two_one = int(str(member.id)[6])
        value_two_two = int(str(member.id)[9])
        if value_one_one == value_two_one:
            if message.mentions:
                if member.id != message.mentions[0].id:
                    if value_one_two == value_two_two:
                        matches.append(f'{member.mention}')
            else:
                if member.id != message.author.id:
                    if value_one_two == value_two_two:
                        matches.append(f'{member.mention}')
    response = discord.Embed(title=f'🔎 Searching for {pronouns[1]} match...', color=0xBDDDF4)
    search_resp = await message.channel.send(embed=response)
    await asyncio.sleep(3)
    try:
        match = secrets.choice(matches)
        desc = f'**{pronouns[0]} match is {match}!**'
        match_resp = discord.Embed(title='💗 **I found one!**', description=desc, color=0xE75A70)
    except IndexError:
        match_resp = discord.Embed(title=f'💔 **{pronouns[2]} don\'t have any matches.**', color=0xE75A70)
    await search_resp.edit(embed=match_resp)
