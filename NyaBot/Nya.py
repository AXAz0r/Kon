import discord
import asyncio
import logging
from discord.ext import commands

logging.basicConfig(level=logging.INFO)

bot = commands.Bot(command_prefix="^")
bot.remove_command('help')


@bot.event
async def on_ready():
    embed = discord.Embed(title="I'm awake! I'm Nya ??", color=0xA5FFF6)
    chn = bot.get_channel('376194194001100811')
    await bot.send_message(chn, embed=embed)
    await bot.change_presence(game=discord.Game(name='^help for help'))


@bot.command(pass_context=True)
@commands.cooldown(1, 10, commands.BucketType.server)
async def apply(ctx, *, msg: str):
    if ctx.message.channel.id == '376194194001100811':
        a = open('lists/requests.txt', 'a')
        a.write(msg + '\n')
        a.close()
        embed = discord.Embed(title="✅ I put you on the 'Student Requests' list!", color=0xA5FFF6)
    else:
        embed = discord.Embed(title="⛔ Sorry! Please use the mentor-chat channel for that command", color=0xBE1931)
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
        embed = discord.Embed(title="⛔ Sorry! Please use the mentor-chat channel for that command", color=0xBE1931)
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
            if '%s' % msg not in line:
                output.append(line)
        a.close()
        a = open(fn, 'w')
        a.writelines(output)
        a.close()
        response = discord.Embed(title="📝 Updated", color=0xA5FFF6)
    else:
        response = discord.Embed(title="⛔ Access denied: Head Mentor required", color=0xBE1931)
    await bot.say(embed=response)


@bot.command(pass_context=True)
async def raidban(ctx, message: str):
    if ctx.message.author.permissions_in(ctx.message.channel).administrator:
        allow = True
    elif ctx.message.author.id == '208974392644861952':
        allow = True
    else:
        allow = False
    if not allow:
        response = discord.Embed(title='⛔ Access denied: Administrator required', color=0xBE1931)
    else:
        msg = message.replace("!", "")
        a = open('lists/raidbans.txt', 'a')
        a.write('%s' % msg + '\n')
        a.close()
        raidban_role = discord.utils.get(ctx.message.server.roles, name='Raid Banned')
        await ctx.bot.add_roles(ctx.message.mentions[0], raidban_role)
        response = discord.Embed(title="🔒 User is now Raid Banned", color=0xA5FFF6)
    await ctx.bot.say(embed=response)


@bot.command()
async def raidbans():
    with open('lists/raidbans.txt', 'r') as file:
        a = file.read()
    embed = discord.Embed(title="**Raid Bans:**", color=0xA5FFF6)
    embed.description = ('%s' % a)
    await bot.say(embed=embed)


@bot.command(pass_context=True)
async def unraidban(ctx):
    if ctx.message.author.permissions_in(ctx.message.channel).administrator:
        allow = True
    elif ctx.message.author.id == '208974392644861952':
        allow = True
    else:
        allow = False
    if not allow:
        response = discord.Embed(title='⛔ Access denied: Administrator required', color=0xBE1931)
    else:
        fn = 'lists/raidbans.txt'
        target = ctx.message.mentions[0]
        a = open(fn)
        output = []
        for line in a:
            if '%s' % target.id not in line:
                output.append(line)
        a.close()
        a = open(fn, 'w')
        a.writelines(output)
        a.close()
        raidban_role = discord.utils.get(ctx.message.server.roles, name='Raid Banned')
        await ctx.bot.remove_roles(ctx.message.mentions[0], raidban_role)
        response = discord.Embed(title="🔓 User is no longer Raid Banned", color=0xA5FFF6)
    await ctx.bot.say(embed=response)


@bot.command(pass_context=True)
async def addmentor(ctx):
    headmentor = ['208974392644861952', '134767479435034624']
    if ctx.message.author.id in headmentor:
        target = ctx.message.mentions[0]
        a = open('lists/mentors.txt', 'a')
        a.write('<@%s>' % target.id + '\n')
        a.close()
        with open('lists/mentors.txt', 'r+') as file:
            a = file.read()
        new = a.replace('!', '')
        file.write(new)
        mentor_role = discord.utils.get(ctx.message.server.roles, name='Mentors')
        await bot.add_roles(ctx.message.mentions[0], mentor_role)
        embed = discord.Embed(title="✅ I put them on the 'Mentors' list!", color=0xA5FFF6)
    else:
        embed = discord.Embed(title="⛔ Access denied: Head Mentor required", color=0xBE1931)
    await bot.say(embed=embed)


@bot.command()
async def mentors():
    with open('lists/mentors.txt', 'r+') as file:
        a = file.read()
    embed = discord.Embed(title="**Mentors:**", color=0xA5FFF6)
    embed.description = ('%s' % a)
    embed1 = discord.Embed(description="```Mentors are there to help\n"
                                       "anyone who needs it. Check\n"
                                       "to see if any of the following\n"
                                       "mentors are online to assist.```", color=0xA5FFF6)
    await bot.say(embed=embed1)
    await bot.say(embed=embed)


@bot.command(pass_context=True)
async def delmentor(ctx):
    headmentor = ['208974392644861952', '134767479435034624']
    if ctx.message.author.id in headmentor:
        fn = 'lists/mentors.txt'
        target = ctx.message.mentions[0]
        a = open(fn)
        output = []
        for line in a:
            if '%s' % target.id not in line:
                output.append(line)
        a.close()
        a = open(fn, 'w')
        a.writelines(output)
        a.close()
        mentor_role = discord.utils.get(ctx.message.server.roles, name='Mentors')
        await bot.remove_roles(ctx.message.mentions[0], mentor_role)
        embed = discord.Embed(title="📝 Updated", color=0xA5FFF6)
    else:
        embed = discord.Embed(title="⛔ Access denied: Head Mentor required", color=0xBE1931)
    await bot.say(embed=embed)


@bot.command()
async def help():
    embed = discord.Embed(title="❔ Hi! I can add your name to the Student Requests list!", color=0xA5FFF6)
    embed.description = 'Type `^apply YourIGN YourRegion` to be added to the list.\n' \
                        'Type `^requests` to get the current Student Requests list.\n' \
                        'Type `^mentors` to get a list of the current Mentors.\n' \
                        'Type `^commands` to get a list of my commands and their uses.' \
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
                                      "#Voting commands\n"
                                      "- vote - Vote 'yes' or 'no' on the current poll.\n"
                                      "- votes - Returns the results of the current primary poll.*\n"
                                      "- voters - Returns a list of users who voted on the current primary poll.*\n"
                                      "- clrvotes - Deletes all data pertaining to the current primary poll.*\n"
                                      "- changerole - Changes the role required to vote on the primary poll.*\n"
                                      "- vote2 - Vote 'yes' or 'no' on the current secondary poll.\n"
                                      "- votes2 - Returns the results of the current secondary poll.*\n"
                                      "- voters2 - Returns a list of users who voted on the current secondary poll.*\n"
                                      "- clrvotes2 - Deletes all data pertaining to the current secondary poll.*\n\n"
                                      "#Other commands\n"
                                      "- help - View help for the Mentor commands.\n"
                                      "- commands - View a list of the commands.\n"
                                      "- purge - Delete a specified number of messages.\n"
                                      "- github - View the GitHub link for Nya's source code.\n"
                                      "- sleep - Tell Nya to go to sleep.\n\n"
                                      "[^] = Prefix.\n"
                                      "[*] = Admins only.\n"
                                      "[**] = Shifty9 only.\n"
                                      "Commands are case sensitive.```", color=0xA5FFF6)
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
        response = discord.Embed(title='⛔ Access denied: Manage Messages required', color=0xBE1931)
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
        logmsg = discord.Embed(title='', color=0xA5FFF6)
        logmsg.add_field(name='🗑️ A channel was purged',
                         value=f'**Purge Details:**\n'
                               f'Channel: <#%s>\n'
                               f'User: <@%s>\n'
                               f'Amount: %s Messages' % (ctx.message.channel.id, ctx.message.author.id, amount),
                         inline=True)
        logmsg.set_footer(text=f'ChannelID: %s' % ctx.message.channel.id, )
        chn = bot.get_channel('302665883849850881')
        await ctx.bot.send_message(chn, embed=logmsg)
        response = discord.Embed(title=f'✅ {amount} Messages Gone', color=0xA5FFF6)
        del_response = await ctx.bot.say(embed=response)
        await asyncio.sleep(3)
        await ctx.bot.delete_message(del_response)


@bot.command()
async def sleep():
    tmp = await bot.say("`(≧Д≦)` No!!!")
    await asyncio.sleep(3)
    await bot.edit_message(tmp, "Fine...")


@bot.command()
async def github():
    embed = discord.Embed(title=':information_source: GitHub for Nya:', color=0xA5FFF6)
    embed.description = 'https://github.com/Shifty6/Nya'
    await bot.say(embed=embed)


@bot.command(pass_context=True)
async def vote(ctx, msg):
    async for x in bot.logs_from(ctx.message.channel, limit=1):
        await bot.delete_message(x)
    fn1 = 'permissions/channels.txt'
    fn2 = 'permissions/users.txt'
    fn3 = 'permissions/roles.txt'
    with open(fn1, 'r') as file:
        a = file.read()
    if ctx.message.channel.id in a:
        channel = True
    else:
        channel = False
    with open(fn2, 'r') as file:
        a = file.read()
    if ctx.message.author.id in a:
        user = True
    else:
        user = False
    a = open(fn3)
    for line in a:
        if line.rstrip() in [y.id for y in ctx.message.author.roles]:
            role = True
        else:
            role = False
    a.close()
    if channel:
        if user or role:
            with open('lists/voters.txt', 'r') as file:
                a = file.read()
            if not '%s' % ctx.message.author.id in a:
                if 'yes' in msg:
                    a = open('lists/yvote.txt', 'a')
                    a.write('yes' + '\n')
                    a.close()
                    a = open('lists/voters.txt', 'a')
                    a.write(f'<@{ctx.message.author.id}>' + '\n')
                    a.close()
                    response = discord.Embed(title='🗳️ Voted!', color=0xA5FFF6)
                elif 'no' in msg:
                    a = open('lists/nvote.txt', 'a')
                    a.write('no' + '\n')
                    a.close()
                    a = open('lists/voters.txt', 'a')
                    a.write(f'<@{ctx.message.author.id}>' + '\n')
                    a.close()
                    response = discord.Embed(title='🗳️ Voted!', color=0xA5FFF6)
                else:
                    response = discord.Embed(title="❗ Vote must contain 'yes' or 'no'", color=0xBE1931)
            else:
                response = discord.Embed(title='⛔ Sorry! You already voted', color=0xBE1931)
        else:
            response = discord.Embed(title='🔒 You do not have the required roles', color=0xFFCC4d)
    else:
        response = discord.Embed(title='🔒 You can\'t use that command in this channel', color=0xFFCC4d)
    await bot.say(embed=response)


@bot.command(pass_context=True)
async def changerole(ctx, *, msg: str):
    if ctx.message.author.permissions_in(ctx.message.channel).administrator:
        a = open('lists/roles.txt', 'w')
        a.write(msg)
        a.close()
        response = discord.Embed(title='📝 Role changed', color=0xA5FFF6)
    else:
        response = discord.Embed(title='⛔ Access denied: Administrator required', color=0xBE1931)
    await ctx.bot.say(embed=response)


@bot.command(pass_context=True)
async def votes(ctx):
    if ctx.message.author.permissions_in(ctx.message.channel).administrator:
        a = open('lists/yvote.txt', 'r')
        yvotes = 0
        for line in a:
            if 'yes' in line:
                x = int(yvotes) + 1
                yvotes = 0 + x
        a.close()
        a = open('lists/nvote.txt', 'r')
        nvotes = 0
        for line in a:
            if 'no' in line:
                x = int(nvotes) + 1
                nvotes = 0 + x
        a.close()
        tvotes = yvotes + nvotes
        try:
            nftmp = (nvotes / tvotes) * 10
            netmp = 10 - nftmp
            nfill = int(round(nftmp))
            nempty = int(round(netmp))
            nbar = f'[{nfill * "▣"}{nempty * "▢"}]'
        except ZeroDivisionError:
            nstat_line = "[▢▢▢▢▢▢▢▢▢▢] 0% - No"
        try:
            yftmp = (yvotes / tvotes) * 10
            yetmp = 10 - yftmp
            yfill = int(round(yftmp))
            yempty = int(round(yetmp))
            ybar = f'[{yfill * "▣"}{yempty * "▢"}]'
        except ZeroDivisionError:
            ystat_line = "[▢▢▢▢▢▢▢▢▢▢] 0% - Yes"
        else:
            ystat_line = f'{ybar} {int((yvotes / tvotes) * 100)}% - Yes'
            nstat_line = f'{nbar} {int((nvotes / tvotes) * 100)}% - No'
        response = discord.Embed(title=f'📊 Poll Statistics', color=0xA5FFF6)
        output = f'{ystat_line}\n' \
                 f'{nstat_line}'
        response.description = f'```{output}```'
    else:
        response = discord.Embed(title='⛔ Access denied: Administrator required', color=0xBE1931)
    await bot.say(embed=response)


@bot.command(pass_context=True)
async def voters(ctx):
    if ctx.message.author.permissions_in(ctx.message.channel).administrator:
        with open('lists/voters.txt', 'r') as file:
            a = file.read()
        response = discord.Embed(title="**Voters:**", color=0xA5FFF6)
        response.description = ('%s' % a)
    else:
        response = discord.Embed(title='⛔ Access denied: Administrator required', color=0xBE1931)
    await bot.say(embed=response)


@bot.command(pass_context=True)
async def clrvotes(ctx):
    if ctx.message.author.permissions_in(ctx.message.channel).administrator:
        a = open('lists/yvote.txt', 'w')
        a.write('')
        a.close()
        a = open('lists/nvote.txt', 'w')
        a.write('')
        a.close()
        a = open('lists/voters.txt', 'w')
        a.write('')
        a.close()
        response = discord.Embed(title='🗑️ Cleared', color=0xA5FFF6)
        await bot.say(embed=response)
    else:
        response = discord.Embed(title='⛔ Access denied: Administrator required', color=0xBE1931)
        await bot.say(embed=response)


@bot.command(pass_context=True)
async def vote(ctx, msg):
    async for x in bot.logs_from(ctx.message.channel, limit=1):
        await bot.delete_message(x)
    fn1 = 'permissions/channels2.txt'
    fn2 = 'permissions/users2.txt'
    fn3 = 'permissions/roles2.txt'
    with open(fn1, 'r') as file:
        a = file.read()
    if ctx.message.channel.id in a:
        channel = True
    else:
        channel = False
    with open(fn2, 'r') as file:
        a = file.read()
    if ctx.message.author.id in a:
        user = True
    else:
        user = False
    a = open(fn3)
    for line in a:
        if line.rstrip() in [y.id for y in ctx.message.author.roles]:
            role = True
        else:
            role = False
    a.close()
    if channel:
        if user or role:
            with open('lists/voters2.txt', 'r') as file:
                a = file.read()
            if not '%s' % ctx.message.author.id in a:
                if 'yes' in msg:
                    a = open('lists/yvote2.txt', 'a')
                    a.write('yes' + '\n')
                    a.close()
                    a = open('lists/voters2.txt', 'a')
                    a.write(f'<@{ctx.message.author.id}>' + '\n')
                    a.close()
                    response = discord.Embed(title='🗳️ Voted!', color=0xA5FFF6)
                elif 'no' in msg:
                    a = open('lists/nvote2.txt', 'a')
                    a.write('no' + '\n')
                    a.close()
                    a = open('lists/voters2.txt', 'a')
                    a.write(f'<@{ctx.message.author.id}>' + '\n')
                    a.close()
                    response = discord.Embed(title='🗳️ Voted!', color=0xA5FFF6)
                else:
                    response = discord.Embed(title="❗ Vote must contain 'yes' or 'no'", color=0xBE1931)
            else:
                response = discord.Embed(title='⛔ Sorry! You already voted', color=0xBE1931)
        else:
            response = discord.Embed(title='🔒 You do not have the required roles', color=0xFFCC4d)
    else:
        response = discord.Embed(title='🔒 You can\'t use that command in this channel', color=0xFFCC4d)
    await bot.say(embed=response)


@bot.command(pass_context=True)
async def votes2(ctx):
    if ctx.message.author.permissions_in(ctx.message.channel).administrator:
        a = open('lists/yvote2.txt', 'r')
        yvotes = 0
        for line in a:
            if 'yes' in line:
                x = int(yvotes) + 1
                yvotes = 0 + x
        a.close()
        a = open('lists/nvote2.txt', 'r')
        nvotes = 0
        for line in a:
            if 'no' in line:
                x = int(nvotes) + 1
                nvotes = 0 + x
        a.close()
        tvotes = yvotes + nvotes
        try:
            nftmp = (nvotes / tvotes) * 10
            netmp = 10 - nftmp
            nfill = int(round(nftmp))
            nempty = int(round(netmp))
            nbar = f'[{nfill * "▣"}{nempty * "▢"}]'
        except ZeroDivisionError:
            nstat_line = "[▢▢▢▢▢▢▢▢▢▢] 0% - No"
        try:
            yftmp = (yvotes / tvotes) * 10
            yetmp = 10 - yftmp
            yfill = int(round(yftmp))
            yempty = int(round(yetmp))
            ybar = f'[{yfill * "▣"}{yempty * "▢"}]'
        except ZeroDivisionError:
            ystat_line = "[▢▢▢▢▢▢▢▢▢▢] 0% - Yes"
        else:
            ystat_line = f'{ybar} {int((yvotes / tvotes) * 100)}% - Yes'
            nstat_line = f'{nbar} {int((nvotes / tvotes) * 100)}% - No'
        response = discord.Embed(title=f'📊 Poll Statistics.', color=0xA5FFF6)
        output = f'{ystat_line}\n' \
                 f'{nstat_line}'
        response.description = f'```{output}```'
    else:
        response = discord.Embed(title='⛔ Access denied: Administrator required', color=0xBE1931)
    await bot.say(embed=response)


@bot.command(pass_context=True)
async def voters2(ctx):
    if ctx.message.author.permissions_in(ctx.message.channel).administrator:
        with open('lists/voters2.txt', 'r') as file:
            a = file.read()
        response = discord.Embed(title="**Voters:**", color=0xA5FFF6)
        response.description = ('%s' % a)
    else:
        response = discord.Embed(title='⛔ Access denied: Administrator required', color=0xBE1931)
    await bot.say(embed=response)


@bot.command(pass_context=True)
async def clrvotes2(ctx):
    if ctx.message.author.permissions_in(ctx.message.channel).administrator:
        a = open('lists/yvote2.txt', 'w')
        a.write('')
        a.close()
        a = open('lists/nvote2.txt', 'w')
        a.write('')
        a.close()
        a = open('lists/voters2.txt', 'w')
        a.write('')
        a.close()
        response = discord.Embed(title='🗑️ Cleared', color=0xA5FFF6)
        await bot.say(embed=response)
    else:
        response = discord.Embed(title='⛔ Access denied: Administrator required', color=0xBE1931)
        await bot.say(embed=response)


@bot.command(pass_context=True)
async def permitc(ctx):
    if ctx.message.author.permissions_in(ctx.message.channel).administrator:
        if ctx.message.channel_mentions:
            with open('permissions/channels.txt', 'r') as file:
                a = file.read()
                for line in ctx.message.channel_mentions:
                    if line.id not in a:
                        perm = True
                    else:
                        perm = False
                    if perm:
                        a = open('permissions/channels.txt', 'a')
                        a.write('<#%s>\n' % line.id)
                        a.close()
                        response = discord.Embed(title="🔓 Channel permitted", color=0xFFCC4d)
                    else:
                        response = discord.Embed(title="❗ Channel already permitted", color=0xBE1931)
                    await bot.say(embed=response)
        else:
            response = discord.Embed(title='❗ Input must be a channel', color=0xBE1931)
            await bot.say(embed=response)
    else:
        response = discord.Embed(title='⛔ Access denied: Administrator required', color=0xBE1931)
        await bot.say(embed=response)
        
        
@bot.command(pass_context=True)
async def permitc2(ctx):
    if ctx.message.author.permissions_in(ctx.message.channel).administrator:
        if ctx.message.channel_mentions:
            with open('permissions/channels2.txt', 'r') as file:
                a = file.read()
                for line in ctx.message.channel_mentions:
                    if line.id not in a:
                        perm = True
                    else:
                        perm = False
                    if perm:
                        a = open('permissions/channels2.txt', 'a')
                        a.write('<#%s>\n' % line.id)
                        a.close()
                        response = discord.Embed(title="🔓 Channel permitted", color=0xFFCC4d)
                    else:
                        response = discord.Embed(title="❗ Channel already permitted", color=0xBE1931)
                    await bot.say(embed=response)
        else:
            response = discord.Embed(title='❗ Input must be a channel', color=0xBE1931)
            await bot.say(embed=response)
    else:
        response = discord.Embed(title='⛔ Access denied: Administrator required', color=0xBE1931)
        await bot.say(embed=response)


@bot.command(pass_context=True)
async def permitu(ctx):
    if ctx.message.author.permissions_in(ctx.message.channel).administrator:
        if ctx.message.mentions:
            with open('permissions/users.txt', 'r') as file:
                a = file.read()
                for line in ctx.message.mentions:
                    if line.id not in a:
                        perm = True
                    else:
                        perm = False
                    if perm:
                        a = open('permissions/users.txt', 'a')
                        a.write('<@%s>\n' % line.id)
                        a.close()
                        response = discord.Embed(title="🔓 User permitted", color=0xFFCC4d)
                    else:
                        response = discord.Embed(title="❗ User already permitted", color=0xBE1931)
                    await bot.say(embed=response)
        else:
            response = discord.Embed(title='❗ Input must be a user', color=0xBE1931)
            await bot.say(embed=response)
    else:
        response = discord.Embed(title='⛔ Access denied: Administrator required', color=0xBE1931)
        await bot.say(embed=response)
        
        
@bot.command(pass_context=True)
async def permitu2(ctx):
    if ctx.message.author.permissions_in(ctx.message.channel).administrator:
        if ctx.message.mentions:
            with open('permissions/users2.txt', 'r') as file:
                a = file.read()
                for line in ctx.message.mentions:
                    if line.id not in a:
                        perm = True
                    else:
                        perm = False
                    if perm:
                        a = open('permissions/users2.txt', 'a')
                        a.write('<@%s>\n' % line.id)
                        a.close()
                        response = discord.Embed(title="🔓 User permitted", color=0xFFCC4d)
                    else:
                        response = discord.Embed(title="❗ User already permitted", color=0xBE1931)
                    await bot.say(embed=response)
        else:
            response = discord.Embed(title='❗ Input must be a user', color=0xBE1931)
            await bot.say(embed=response)
    else:
        response = discord.Embed(title='⛔ Access denied: Administrator required', color=0xBE1931)
        await bot.say(embed=response)


@bot.command(pass_context=True)
async def permitr(ctx, *, msg):
    if ctx.message.author.permissions_in(ctx.message.channel).administrator:
        lookup = msg.lower()
        target = discord.utils.find(lambda x: x.name.lower() == lookup, ctx.message.server.roles)
        if target is not None:
            with open('permissions/roles.txt', 'r') as file:
                a = file.read()
                if target.id not in a:
                    perm = True
                else:
                    perm = False
                if perm:
                    a = open('permissions/roles.txt', 'a')
                    a.write('<@&%s>\n' % target.id)
                    a.close()
                    response = discord.Embed(title="🔓 Role permitted", color=0xFFCC4d)
                else:
                    response = discord.Embed(title="❗ Role already permitted", color=0xBE1931)
                await bot.say(embed=response)
        else:
            response = discord.Embed(title='❗ Input must be a role', color=0xBE1931)
            await bot.say(embed=response)
    else:
        response = discord.Embed(title='⛔ Access denied: Administrator required', color=0xBE1931)
        await bot.say(embed=response)
        
        
@bot.command(pass_context=True)
async def permitr2(ctx, *, msg):
    if ctx.message.author.permissions_in(ctx.message.channel).administrator:
        lookup = msg.lower()
        target = discord.utils.find(lambda x: x.name.lower() == lookup, ctx.message.server.roles)
        if target is not None:
            with open('permissions/roles2.txt', 'r') as file:
                a = file.read()
                if target.id not in a:
                    perm = True
                else:
                    perm = False
                if perm:
                    a = open('permissions/roles2.txt', 'a')
                    a.write('<@&%s>\n' % target.id)
                    a.close()
                    response = discord.Embed(title="🔓 Role permitted", color=0xFFCC4d)
                else:
                    response = discord.Embed(title="❗ Role already permitted", color=0xBE1931)
                await bot.say(embed=response)
        else:
            response = discord.Embed(title='❗ Input must be a role', color=0xBE1931)
            await bot.say(embed=response)
    else:
        response = discord.Embed(title='⛔ Access denied: Administrator required', color=0xBE1931)
        await bot.say(embed=response)


@bot.command(pass_context=True)
async def unpermitc(ctx):
    if ctx.message.author.permissions_in(ctx.message.channel).administrator:
        if ctx.message.channel_mentions:
            target = ctx.message.channel_mentions[0].id
            fn = 'permissions/channels.txt'
            a = open(fn)
            output = []
            for line in a:
                if target not in line:
                    output.append(line)
            a.close()
            a = open(fn, 'w')
            a.writelines(output)
            a.close()
            response = discord.Embed(title="🔒 Channel unpermitted", color=0xFFCC4d)
        else:
            response = discord.Embed(title='❗ Input must be a channel', color=0xBE1931)
    else:
        response = discord.Embed(title='⛔ Access denied: Administrator required', color=0xBE1931)
    await bot.say(embed=response)
    
    
@bot.command(pass_context=True)
async def unpermitc2(ctx):
    if ctx.message.author.permissions_in(ctx.message.channel).administrator:
        if ctx.message.channel_mentions:
            target = ctx.message.channel_mentions[0].id
            fn = 'permissions/channels.txt'
            a = open(fn)
            output = []
            for line in a:
                if target not in line:
                    output.append(line)
            a.close()
            a = open(fn, 'w')
            a.writelines(output)
            a.close()
            response = discord.Embed(title="🔒 Channel unpermitted", color=0xFFCC4d)
        else:
            response = discord.Embed(title='❗ Input must be a channel', color=0xBE1931)
    else:
        response = discord.Embed(title='⛔ Access denied: Administrator required', color=0xBE1931)
    await bot.say(embed=response)


@bot.command(pass_context=True)
async def unpermitr(ctx, *, msg):
    lookup = msg.lower()
    target = discord.utils.find(lambda x: x.name.lower() == lookup, ctx.message.server.roles)
    if ctx.message.author.permissions_in(ctx.message.channel).administrator:
        if target is not None:
            fn = 'permissions/roles.txt'
            a = open(fn)
            output = []
            for line in a:
                if target.id not in line:
                    output.append(line)
            a.close()
            a = open(fn, 'w')
            a.writelines(output)
            a.close()
            response = discord.Embed(title="🔒 Role unpermitted", color=0xFFCC4d)
        else:
            response = discord.Embed(title='❗ Input must be a role', color=0xBE1931)
    else:
        response = discord.Embed(title='⛔ Access denied: Administrator required', color=0xBE1931)
    await bot.say(embed=response)
    
    
@bot.command(pass_context=True)
async def unpermitr2(ctx, *, msg):
    lookup = msg.lower()
    target = discord.utils.find(lambda x: x.name.lower() == lookup, ctx.message.server.roles)
    if ctx.message.author.permissions_in(ctx.message.channel).administrator:
        if target is not None:
            fn = 'permissions/roles2.txt'
            a = open(fn)
            output = []
            for line in a:
                if target.id not in line:
                    output.append(line)
            a.close()
            a = open(fn, 'w')
            a.writelines(output)
            a.close()
            response = discord.Embed(title="🔒 Role unpermitted", color=0xFFCC4d)
        else:
            response = discord.Embed(title='❗ Input must be a role', color=0xBE1931)
    else:
        response = discord.Embed(title='⛔ Access denied: Administrator required', color=0xBE1931)
    await bot.say(embed=response)


@bot.command(pass_context=True)
async def unpermitu(ctx):
    if ctx.message.author.permissions_in(ctx.message.channel).administrator:
        if ctx.message.mentions:
            target = ctx.message.mentions[0].id
            fn = 'permissions/users.txt'
            a = open(fn)
            output = []
            for line in a:
                if target not in line:
                    output.append(line)
            a.close()
            a = open(fn, 'w')
            a.writelines(output)
            a.close()
            response = discord.Embed(title="🔒 User unpermitted", color=0xFFCC4d)
        else:
            response = discord.Embed(title='❗ Input must be a user', color=0xBE1931)
    else:
        response = discord.Embed(title='⛔ Access denied: Administrator required', color=0xBE1931)
    await bot.say(embed=response)
    
    
@bot.command(pass_context=True)
async def unpermitu2(ctx):
    if ctx.message.author.permissions_in(ctx.message.channel).administrator:
        if ctx.message.mentions:
            target = ctx.message.mentions[0].id
            fn = 'permissions/users2.txt'
            a = open(fn)
            output = []
            for line in a:
                if target not in line:
                    output.append(line)
            a.close()
            a = open(fn, 'w')
            a.writelines(output)
            a.close()
            response = discord.Embed(title="🔒 User unpermitted", color=0xFFCC4d)
        else:
            response = discord.Embed(title='❗ Input must be a user', color=0xBE1931)
    else:
        response = discord.Embed(title='⛔ Access denied: Administrator required', color=0xBE1931)
    await bot.say(embed=response)


@bot.command()
async def perms():
    with open('permissions/channels.txt', 'r') as file:
        a = file.read()
    with open('permissions/roles.txt', 'r') as file:
        b = file.read()
    with open('permissions/users.txt', 'r') as file:
        c = file.read()
    embed = discord.Embed(title='📊 **Poll permissions:**\n', description='**Channels:**\n'
                                                                          '%s'
                                                                          '**Roles:**\n' 
                                                                          '%s'
                                                                          '**Users:**\n'
                                                                          '%s' % (a, b, c), color=0xA5FFF6)
    await bot.say(embed=embed)
    
    
@bot.command()
async def perms2():
    with open('permissions/channels2.txt', 'r') as file:
        a = file.read()
    with open('permissions/roles2.txt', 'r') as file:
        b = file.read()
    with open('permissions/users2.txt', 'r') as file:
        c = file.read()
    embed = discord.Embed(title='📊 **Poll permissions:**\n', description='**Channels:**\n'
                                                                          '%s'
                                                                          '**Roles:**\n' 
                                                                          '%s'
                                                                          '**Users:**\n'
                                                                          '%s' % (a, b, c), color=0xA5FFF6)
    await bot.say(embed=embed)


bot.run("token_removed", bot=True)
