import discord
import asyncio
import logging
from discord.ext import commands

logging.basicConfig(level=logging.INFO)

bot = commands.Bot(command_prefix="^")
bot.remove_command('help')


@bot.event
async def on_ready():
    embed = discord.Embed(title="I'm awake! I'm Nya 💕", color=0xA5FFF6)
    chn = bot.get_channel('376194194001100811')
    await bot.send_message(chn, embed=embed)
    await bot.change_presence(game=discord.Game(name='^help for help'))


@bot.command(pass_context=True)
@commands.cooldown(1, 10, commands.BucketType.user)
async def apply(ctx, *, msg: str):
    if ctx.message.channel.id == '376194194001100811':
        a = open('lists/requests.txt', 'a')
        a.write(msg + '\n')
        a.close()
        embed = discord.Embed(title="✅ I put you on the 'Student Requests' list!", color=0xA5FFF6)
    else:
        embed = discord.Embed(title="⛔ Sorry! Please use the mentor-chat channel for that command.", color=0xA5FFF6)
    await bot.say(embed=embed)


@bot.command(pass_context=True)
async def requests(ctx):
    if ctx.message.channel.id == '376194194001100811':
        allow = True
    elif ctx.message.author.id == '208974392644861952':
        allow = True
    else:
        allow = False
    if not allow:
        embed = discord.Embed(title="⛔ Sorry! Please use the mentor-chat channel for that command.", color=0xA5FFF6)
    else:
        with open('lists/requests.txt', 'r') as file:
            a = file.read()
        embed = discord.Embed(title="**Student Requests:**", color=0xA5FFF6)
        embed.description = ('%s' % a)
    await bot.say(embed=embed)


@bot.command(pass_context=True)
async def delline(ctx, *, msg: str):
    headmentor = ['208974392644861952', '134767479435034624']
    if ctx.message.author.id in headmentor:
        fn = 'lists/requests.txt'
        a = open(fn)
        output = []
        for line in a:
            if not '%s' % msg in line:
                output.append(line)
        a.close()
        a = open(fn, 'w')
        a.writelines(output)
        a.close()
        embed = discord.Embed(title="📝 Updated!", color=0xA5FFF6)
    else:
        embed = discord.Embed(title="⛔ Sorry! I can\'t let you do that.", color=0xA5FFF6)
    await bot.say(embed=embed)


@bot.command(pass_context=True)
async def raidban(ctx, *, msg: str):
    if ctx.message.author.permissions_in(ctx.message.channel).administrator:
        allow = True
    elif ctx.message.author.id == '208974392644861952':
        allow = True
    else:
        allow = False
    if not allow:
        response = discord.Embed(title='⛔ Access Denied. Administrator needed.', color=0xBE1931)
        await ctx.bot.say(embed=response)
    else:
        a = open('dir/lists/raidbans.txt', 'a')
        a.write(msg + '\n')
        a.close()
        raidban_role = discord.utils.get(ctx.message.server.roles, name='Raid Banned')
        await ctx.bot.add_roles(ctx.message.mentions[0], raidban_role)
        response = discord.Embed(title="✅ Raid Banned!", color=0xA5FFF6)
        await ctx.bot.say(embed=response)


@bot.command()
async def raidbans():
    with open('lists/raidbans.txt', 'r') as myfile:
        a = myfile.read()
    embed = discord.Embed(title="**Raid Bans:**", color=0xA5FFF6)
    embed.description = ('%s' % a)
    await bot.say(embed=embed)


@bot.command(pass_context=True)
async def unraidban(ctx, *, msg: str):
    if ctx.message.author.permissions_in(ctx.message.channel).administrator:
        allow = True
    elif ctx.message.author.id == '208974392644861952':
        allow = True
    else:
        allow = False
    if not allow:
        response = discord.Embed(title='⛔ Access Denied. Administrator needed.', color=0xBE1931)
    else:
        fn = 'lists/raidbans.txt'
        a = open(fn)
        output = []
        for line in a:
            if not '%s' % msg in line:
                output.append(line)
        a.close()
        a = open(fn, 'w')
        a.writelines(output)
        a.close()
        raidban_role = discord.utils.get(ctx.message.server.roles, name='Raid Banned')
        await ctx.bot.remove_roles(ctx.message.mentions[0], raidban_role)
        response = discord.Embed(title="📝 Updated!", color=0xA5FFF6)
    await ctx.bot.say(embed=response)


@bot.command(pass_context=True)
async def addmentor(ctx, *, msg: str):
    if ctx.message.author.id == '208974392644861952':
        a = open('lists/mentors.txt', 'a')
        a.write(msg + '\n')
        a.close()
        mentor_role = discord.utils.get(ctx.message.server.roles, name='Mentors')
        await bot.add_roles(ctx.message.mentions[0], mentor_role)
        embed = discord.Embed(title="✅ I put them on the 'Mentors' list!", color=0xA5FFF6)
    else:
        embed = discord.Embed(title="⛔ Sorry! I can\'t let you do that.", color=0xA5FFF6)
    await bot.say(embed=embed)


@bot.command()
async def mentors():
    with open('lists/mentors.txt', 'r') as myfile:
        a = myfile.read()
    embed = discord.Embed(title="**Mentors:**", color=0xA5FFF6)
    embed.description = ('%s' % a)
    embed1 = discord.Embed(description="```Mentors are there to help\n"
                                       "anyone who needs it. Check\n"
                                       "to see if any of the following\n"
                                       "mentors are online to assist.```", color=0xA5FFF6)
    await bot.say(embed=embed1)
    await bot.say(embed=embed)


@bot.command(pass_context=True)
async def delmentor(ctx, *, msg: str):
    if ctx.message.author.id == '208974392644861952':
        fn = 'lists/mentors.txt'
        a = open(fn)
        output = []
        for line in a:
            if not '%s' % msg in line:
                output.append(line)
        a.close()
        a = open(fn, 'w')
        a.writelines(output)
        a.close()
        mentor_role = discord.utils.get(ctx.message.server.roles, name='Mentors')
        await bot.remove_roles(ctx.message.mentions[0], mentor_role)
        embed = discord.Embed(title="📝 Updated!", color=0xA5FFF6)
    else:
        embed = discord.Embed(title="⛔ Sorry! I can\'t let you do that.", color=0xA5FFF6)
    await bot.say(embed=embed)


@bot.command()
async def help():
    embed = discord.Embed(title="❔ Hi! I can add your name to the Student Requests list!", color=0xA5FFF6)
    embed.description = 'Type `^apply YourIGN YourRegion` to be added to the list.\n' \
                        'Type `^requests` to get the current Student Requests list.\n' \
                        'Type `^commands` to get a list of my commands and their uses.\n' \
                        'If you\'d like your name removed, please ping Shifty9#0995. 💕'
    await bot.say(embed=embed)


@bot.command()
async def commands():
    embed = discord.Embed(description="```md\n"
                                      "**Commands**\n\n"
                                      "#Mentor commands\n"
                                      "- apply - Apply to the 'Students Requests' list.\n"
                                      "- requests - Returns the 'Student Requests' list.\n"
                                      "- delline - Remove a line from the 'Student Requests' list.**\n"
                                      "- addmentor - Adds the targeted user to the 'Mentors' list.**\n"
                                      "- mentors - Returns the 'Mentors' list.\n"
                                      "- delmentor - Removes the targeted user from the 'Mentors' list.**\n\n"
                                      "#Raid Ban commands\n"
                                      "- raidban - Add the targeted user to the 'Raid Banned' list and assigns the"
                                      " 'Raid Banned' role to them.*\n"
                                      "- raidbans - Returns the 'Raid Banned' list.\n"
                                      "- unraidban - Remove the targeted user from the 'Raid Banned' list"
                                      "and removes the 'Raid Banned' role from them.*\n\n"
                                      "#Other commands\n"
                                      "- help - View help for the Mentor commands.\n"
                                      "- commands - View a list of the commands.\n"
                                      "- prefix - View the current command prefix.\n"
                                      "- purge - Delete a specified number of messages.**\n"
                                      "- gist - View the GitHub link for Nya's source code\n"
                                      "- sleep - Tell Nya to go to sleep.\n\n"
                                      "[*] = Admins only.\n"
                                      "[**] = Shifty9 only.```", color=0xA5FFF6)
    await bot.say(embed=embed)


@bot.command()
async def prefix():
    embed = discord.Embed(title='Prefix: `^`', color=0xA5FFF6)
    await bot.say(embed=embed)


@bot.command(pass_context=True)
async def purge(ctx, number):
    if ctx.message.author.permissions_in(ctx.message.channel).manage_messages:
        allow = True
    elif ctx.message.author.id == '208974392644861952':
        allow = True
    else:
        allow = False
    if not allow:
        response = discord.Embed(title='⛔ Access Denied. Manage Messages needed.', color=0xA5FFF6)
        await ctx.bot.say(embed=response)
    else:
        mgs = []
        number = int(number) + 1
        if number > 100:
            number = 100
        async for x in bot.logs_from(ctx.message.channel, limit=number):
            mgs.append(x)
        await bot.delete_messages(mgs)
        if number == 100:
            amount = number
        else:
            amount = number - 1
        logmsg = discord.Embed(color=0xA5FFF6)
        logmsg.add_field(name='🗑️ A channel was purged',
                         value=f'**Purge Details:**\n'
                               f'Channel: <#%s>\n'
                               f'User: <@%s>\n'
                               f'Amount: %s Messages' % (ctx.message.channel.id, ctx.message.author.id, amount),
                         inline=True)
        logmsg.set_footer(text=f'ChannelID: %s' % ctx.message.channel.id,)
        chn = bot.get_channel('302665883849850881')
        await ctx.bot.send_message(chn, embed=logmsg)
        response = discord.Embed(title=f'✅ {amount} Messages Gone!', color=0xA5FFF6)
        del_response = await ctx.bot.say(embed=response)
        await asyncio.sleep(3)
        await ctx.bot.delete_message(del_response)


@bot.command()
async def sleep():
    tmp = await bot.say("`(≧Д≦)` No!!!")
    await asyncio.sleep(3)
    await bot.edit_message(tmp, "Fine...")


@bot.command()
async def gist():
    embed = discord.Embed(title=':information_source: GitHub for Nya:', color=0xA5FFF6)
    embed.description = 'https://gist.github.com/Shifty6/ab5ba64dae65b9e915203f225ee98f17'
    await bot.say(embed=embed)


bot.run("token_removed", bot=True)
