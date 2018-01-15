import asyncio
import json
import logging
import os
import secrets
import string
import random

import discord
from discord.ext import commands

logging.basicConfig(level=logging.INFO)

bot = commands.Bot(command_prefix="^")
bot.remove_command('help')


@bot.event
async def on_ready():
    print('Bot ready.')
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
        embed = discord.Embed(title="⛔ Please use the mentor-chat channel for that command", color=0xBE1931)
    await bot.say(embed=embed)


def dump_vote(vote_data, vote_key, voter):
    voter_list = vote_data.get('voters')
    if voter_list is None:
        voter_list = []
    voter_list.append(voter.id)
    vote_count = vote_data.get(vote_key)
    if vote_count is None:
        vote_count = 0
    vote_count += 1
    vote_data.update({vote_key: vote_count})
    vote_data.update({'voters': voter_list})
    with open('lists/vote_data.json', 'w', encoding='utf-8') as vote_data_file:
        json.dump(vote_data, vote_data_file)


@bot.command(pass_context=True)
async def vote(ctx, msg):
    if ctx.message.server:
        await bot.delete_message(ctx.message)
    if ctx.message.channel.is_private:
        with open('permissions/registered.txt', 'r') as file:
            a = file.read()
        with open('permissions/officers.txt', 'r') as file:
            b = file.read()
        with open('permissions/generalsp.txt', 'r') as file:
            c = file.read()
        if ctx.message.author.id in a:
            auth = True
        elif ctx.message.author.id in b:
            auth = True
        elif ctx.message.author.id in c:
            auth = True
        else:
            auth = False
        if auth:
            if os.path.exists('lists/vote_data.json'):
                with open('lists/vote_data.json', encoding='utf-8') as vote_data_file:
                    vote_data = json.loads(vote_data_file.read())
            else:
                vote_data = {}
            voted = vote_data.get('voters') or []
            if ctx.message.author.id not in voted:
                if msg.lower() == 'yes':
                    dump_vote(vote_data, 'yes', ctx.message.author)
                    response = discord.Embed(title='🗳️ Voted!', color=0xA5FFF6)
                elif msg.lower() == 'no':
                    dump_vote(vote_data, 'no', ctx.message.author)
                    response = discord.Embed(title='🗳️ Voted!', color=0xA5FFF6)
                else:
                    response = discord.Embed(title="❗ Vote must contain 'yes' or 'no'", color=0xBE1931)
            else:
                response = discord.Embed(title='⛔ You already voted', color=0xBE1931)
        else:
            response = discord.Embed(title='⛔ You must register on the server to vote in a DM', color=0xBE1931)
    else:
        if ctx.message.server.id == '138067606119645184':
            with open('permissions/channels.txt', 'r') as file:
                a = file.read()
            if ctx.message.channel.id in a:
                channel = True
            else:
                channel = False
            with open('permissions/users.txt', 'r') as file:
                a = file.read()
            if ctx.message.author.id in a:
                user = True
            else:
                user = False
            with open('permissions/roles.txt') as file:
                a = file.read()
            tmp = [y.id for y in ctx.message.author.roles]
            for line in tmp:
                if line in a:
                    role = True
            if channel:
                try:
                    if user or role:
                        if os.path.exists('lists/vote_data.json'):
                            with open('lists/vote_data.json', encoding='utf-8') as vote_data_file:
                                vote_data = json.loads(vote_data_file.read())
                        else:
                            vote_data = {}
                        voted = vote_data.get('voters') or []
                        if ctx.message.author.id not in voted:
                            if msg.lower() == 'yes':
                                dump_vote(vote_data, 'yes', ctx.message.author)
                                response = discord.Embed(title='🗳️ Voted!', color=0xA5FFF6)
                            elif msg.lower() == 'no':
                                dump_vote(vote_data, 'no', ctx.message.author)
                                response = discord.Embed(title='🗳️ Voted!', color=0xA5FFF6)
                            else:
                                response = discord.Embed(title="❗ Vote must contain 'yes' or 'no'", color=0xBE1931)
                        else:
                            response = discord.Embed(title='⛔ You already voted', color=0xBE1931)
                except UnboundLocalError:
                    response = discord.Embed(title='🔒 You do not have the required roles', color=0xFFCC4d)
            else:
                response = discord.Embed(title='🔒 You can\'t use that command in this channel', color=0xFFCC4d)
        else:
            response = discord.Embed(title='🔒 You can\'t use that command on this server', color=0xFFCC4d)
    await bot.say(embed=response)


@bot.command(pass_context=True)
async def votes(ctx, args):
    if ctx.message.server.id == '138067606119645184':
        if ctx.message.author.permissions_in(ctx.message.channel).administrator:
            with open('lists/pswd_data.json', encoding='utf-8') as pswd_data_file:
                pswd_data = json.loads(pswd_data_file.read())
            pswd = pswd_data.get('pswd')
            if args in pswd:
                if os.path.exists('lists/vote_data.json'):
                    with open('lists/vote_data.json', encoding='utf-8') as vote_data_file:
                        vote_data = json.loads(vote_data_file.read())
                else:
                    vote_data = {}
                yvotes = vote_data.get('yes') or 0
                nvotes = vote_data.get('no') or 0
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
                    ystat_line = f'{yvotes} {ybar} {int((yvotes / tvotes) * 100)}% - Yes'
                    nstat_line = f'{nvotes} {nbar} {int((nvotes / tvotes) * 100)}% - No'
                response = discord.Embed(title=f'📊 Poll Statistics', color=0xA5FFF6)
                output = f'{ystat_line}\n' \
                         f'{nstat_line}'
                response.description = f'```{output}```'
            else:
                response = discord.Embed(title='🔒 Incorrect password', color=0xFFCC4d)
        else:
            response = discord.Embed(title='⛔ Access denied: Administrator required', color=0xBE1931)
    else:
        response = discord.Embed(title='🔒 You can\'t use that command on this server or in a DM', color=0xFFCC4d)
    await bot.say(embed=response)


@bot.command(pass_context=True)
async def voters(ctx, args):
    if ctx.message.server.id == '138067606119645184':
        if ctx.message.author.permissions_in(ctx.message.channel).administrator:
            with open('lists/pswd_data.json', encoding='utf-8') as pswd_data_file:
                pswd_data = json.loads(pswd_data_file.read())
            pswd = pswd_data.get('pswd')
            if args in pswd:
                if os.path.exists('lists/vote_data.json'):
                    with open('lists/vote_data.json', encoding='utf-8') as vote_data_file:
                        vote_data = json.loads(vote_data_file.read())
                else:
                    vote_data = {}
                voter_list = vote_data.get('voters') or []
                line_list = []
                for voter in voter_list:
                    line_list.append('<@' + voter + '>')
                a = '\n'.join(line_list)
                response = discord.Embed(title="**Voters:**", color=0xA5FFF6)
                response.description = ('%s' % a)
            else:
                response = discord.Embed(title='🔒 Incorrect password', color=0xFFCC4d)
        else:
            response = discord.Embed(title='⛔ Access denied: Administrator required', color=0xBE1931)
    else:
        response = discord.Embed(title='🔒 You can\'t use that command on this server or in a DM', color=0xFFCC4d)
    await bot.say(embed=response)


def set_pswd(pswd_data, pswd_str, password: str):
    pswd_str = pswd_data.get('pswd')
    if pswd_str is None:
        pswd_str = []
    pswd_str.clear()
    pswd_str.append(password)
    pswd_data.update({'pswd': pswd_str})
    with open('lists/pswd_data.json', 'w', encoding='utf-8') as pswd_data_file:
        json.dump(pswd_data, pswd_data_file)


def id_generator(size=6, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def get_pswd():
    with open('lists/pswd_data.json', encoding='utf-8') as pswd_data_file:
        pswd_data = json.loads(pswd_data_file.read())
        pswd_str = pswd_data.get('pswd') or []
    for pswd in pswd_str:
        return pswd


@bot.command(pass_context=True)
async def setpassword(ctx):
    if ctx.message.server.id == '138067606119645184':
        if ctx.message.author.permissions_in(ctx.message.channel).administrator:
            if os.path.exists('lists/pswd_data.json'):
                with open('lists/pswd_data.json', encoding='utf-8') as pswd_data_file:
                    pswd_data = json.loads(pswd_data_file.read())
            else:
                pswd_data = {}
            set_pswd(pswd_data, 'pswd', id_generator())
            response = discord.Embed(title='🔐 Password reset. It will be DM\'d to you in 24h', color=0xFFCC4d)
            await bot.say(embed=response)
            if ctx.message.mentions:
                target = ctx.message.mentions[0]
            else:
                target = ctx.message.author
            target_reply = discord.Embed(title=f'🔑 Here is the password `{get_pswd()}`', color=0xc1694f)
            target_reply.set_footer(text=f'^votes/voters password')
            await asyncio.sleep(86400)
            await bot.send_message(target, embed=target_reply)
            return pswd_data
        else:
            response = discord.Embed(title='⛔ Access denied: Administrator required', color=0xBE1931)
    else:
        response = discord.Embed(title='🔒 You can\'t use that command on this server', color=0xFFCC4d)
    await bot.say(embed=response)


@bot.command(pass_context=True)
async def requests(ctx):
    if ctx.message.channel.id == '376194194001100811':
        allow = True
    elif ctx.message.author.id == '208974392644861952':
        allow = True
    else:
        allow = False
    if not allow:
        embed = discord.Embed(title="⛔ Please use the mentor-chat channel for that command", color=0xBE1931)
    else:
        with open('lists/requests.txt', 'r') as file:
            a = file.read()
        embed = discord.Embed(title="**Student Requests:**", color=0xA5FFF6)
        embed.description = ('%s' % a)
    await bot.say(embed=embed)


@bot.command(pass_context=True)
async def delline(ctx, *, msg: str):
    target = discord.utils.find(lambda x: x.name.lower() == 'head mentors', ctx.message.server.roles)
    try:
        if target.id in [y.id for y in ctx.message.author.roles]:
            fn = 'lists/requests.txt'
            a = open(fn)
            output = []
            for line in a:
                if msg.lower() not in line.lower():
                    output.append(line)
            a.close()
            a = open(fn, 'w')
            a.writelines(output)
            a.close()
            response = discord.Embed(title="📝 Updated", color=0xA5FFF6)
        else:
            response = discord.Embed(title="⛔ Access denied: Head Mentor required", color=0xBE1931)
    except AttributeError:
        response = discord.Embed(title="I couldn\'t find the role 'Head Mentors'")
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
        target = ctx.message.mentions[0]
        raidban_role = discord.utils.get(ctx.message.server.roles, name='Raid Banned')
        await ctx.bot.add_roles(ctx.message.mentions[0], raidban_role)
        response = discord.Embed(title=f"🔒 {target.display_name} is now Raid Banned", color=0xFFCC4d)
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
            if target.id not in line:
                output.append(line)
        a.close()
        a = open(fn, 'w')
        a.writelines(output)
        a.close()
        raidban_role = discord.utils.get(ctx.message.server.roles, name='Raid Banned')
        await ctx.bot.remove_roles(ctx.message.mentions[0], raidban_role)
        response = discord.Embed(title=f"🔓 {target.display_name} is no longer Raid Banned", color=0xFFCC4d)
    await ctx.bot.say(embed=response)


@bot.command(pass_context=True)
async def addmentor(ctx):
    target = discord.utils.find(lambda x: x.name.lower() == 'head mentors', ctx.message.server.roles)
    try:
        if target.id in [y.id for y in ctx.message.author.roles]:
            target = ctx.message.mentions[0]
            a = open('lists/mentors.txt', 'a')
            a.write('<@%s>' % target.id + '\n')
            a.close()
            mentor_role = discord.utils.get(ctx.message.server.roles, name='Mentors')
            await bot.add_roles(ctx.message.mentions[0], mentor_role)
            response = discord.Embed(title=f"✅ {target.display_name} is now a Mentor", color=0xA5FFF6)
        else:
            response = discord.Embed(title="⛔ Access denied: Head Mentor required", color=0xBE1931)
    except AttributeError:
        response = discord.Embed(title="I couldn\'t find the role 'Head Mentors'")
    await bot.say(embed=response)


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
    target = discord.utils.find(lambda x: x.name.lower() == 'head mentors', ctx.message.server.roles)
    try:
        if target.id in [y.id for y in ctx.message.author.roles]:
            fn = 'lists/mentors.txt'
            target = ctx.message.mentions[0]
            a = open(fn)
            output = []
            for line in a:
                if target.id not in line:
                    output.append(line)
            a.close()
            a = open(fn, 'w')
            a.writelines(output)
            a.close()
            mentor_role = discord.utils.get(ctx.message.server.roles, name='Mentors')
            await bot.remove_roles(ctx.message.mentions[0], mentor_role)
            response = discord.Embed(title=f"✅ {target.display_name} is no longer a Mentor", color=0xA5FFF6)
        else:
            response = discord.Embed(title="⛔ Access denied: Head Mentor required", color=0xBE1931)
    except AttributeError:
        response = discord.Embed(title="I couldn\'t find the role 'Head Mentors'")
    await bot.say(embed=response)


@bot.command()
async def help():
    embed = discord.Embed(title="❔ Hi! I can add your name to the Student Requests list!", color=0xA5FFF6)
    embed.description = 'Type `^apply YourIGN YourRegion` to be added to the list.\n' \
                        'Type `^requests` to get the current Student Requests list.\n' \
                        'Type `^mentors` to get a list of the current Mentors.\n' \
                        'Type `^modules` to get a list of my modules and their commands.\n' \
                        'If you\'d like your name removed, please ping <@208974392644861952>. 💕'
    await bot.say(embed=embed)


@bot.command()
async def modules():
    embed = discord.Embed(description='**There are 4 modules**\n'
                                      '```yml\n'
                                      '- MENTOR\n'
                                      '- RAIDBAN\n'
                                      '- POLL\n'
                                      '- OTHER```', color=0xA5FFF6)
    embed.set_footer(text=f'^commands module_name')
    await bot.say(embed=embed)


@bot.command()
async def commands(args):
    module = args
    if module == 'mentor':
        response = discord.Embed(title="Mentor commands", description=
        "```md\n"
        "- apply - Apply to the 'Students Requests' list.\n"
        "- requests - Returns the 'Student Requests' list.\n"
        "- delline - Remove a line from the 'Student Requests' list.\n"
        "- addmentor - Adds the targeted user to the 'Mentors' list.\n"
        "- mentors - Returns the 'Mentors' list.\n"
        "- delmentor - Removes the targeted user from the 'Mentors' list.```",
                                 color=0xA5FFF6)
    elif module == 'raidban':
        response = discord.Embed(title="Raid ban commands\n", description=
        "```md\n"
        "- raidban - Add the targeted user to the 'Raid Banned' list and\nassigns the"
        " 'Raid Banned' role to them.\n"
        "- raidbans - Returns the 'Raid Banned' list.\n"
        "- unraidban - Remove the targeted user from the 'Raid Banned' list\n"
        "and removes the 'Raid Banned' role from them.```", color=0xA5FFF6)
    elif module == 'poll':
        response = discord.Embed(title="Poll commands\n", description=
        "```md\n"
        "- vote - Vote 'yes' or 'no' on the current poll.\n"
        "- votes - Returns the results of the current poll.\n"
        "- voters - Returns a list of users who voted on the current poll.\n"
        "- clrvotes - Deletes all voting data pertaining to the current poll.\n"
        "- permit c/u - Permits the target to vote or be voted in. c: channel, u: user.\n"
        "- permitr r/dm - r: permits the specified role to vote on the poll. dm: "
        "permits the targeted role to vote on the poll via DMs.\n"
        "- unpermit c/u - c: unpermits users to vote in the targeted channel. u: "
        "unpermits targeted user to vote on the poll.\n"
        "- unpermitr r/dm - r: unpermits the specified role to vote on the poll. dm: "
        "unpermits the targeted role to vote on the poll via DMs.\n"
        "- perms - Returns the current permissions for the poll.\n"
        "- register - Registers the message author to vote on the poll in a "
        "DM with Kon. Author must be permitted to vote.\n"
        "- clrperms - Deletes all the perms data pertaining to the poll. Also "
        "deletes all registered user data.\n"
        "- setpassword - Resets the password fore votes/voters and DM's it to the command caller after 24h."
        "```", color=0xA5FFF6)
    elif module == 'other':
        response = discord.Embed(title="Other commands\n", description=
        "```md\n"
        "- help - View help for the Mentor commands.\n"
        "- commands - View a list of the commands.\n"
        "- purge - Delete a specified number of messages.\n"
        "- github - View the GitHub link for Kon's source code.\n"
        "- roll - Role a 6 sided dice and try to guess the outcome.\n"
        "- sleep - Tell Kon to go to sleep.```", color=0xA5FFF6)
    else:
        response = discord.Embed(title='❗ Module not found', color=0xBE1931)
    await bot.say(embed=response)


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
        if ctx.message.server.id == '138067606119645184':
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


@bot.command(pass_context=True)
async def clrvotes(ctx):
    if ctx.message.server.id == '138067606119645184':
        if ctx.message.author.permissions_in(ctx.message.channel).administrator:
            if os.path.exists('lists/vote_data.json'):
                os.remove('lists/vote_data.json')
            response = discord.Embed(title='🗑️ Cleared', color=0xA5FFF6)
        else:
            response = discord.Embed(title='⛔ Access denied: Administrator required', color=0xBE1931)
    else:
        response = discord.Embed(title='🔒 You can\'t use that command on this server or in a DM', color=0xFFCC4d)
    await bot.say(embed=response)


@bot.command(pass_context=True)
async def perms(ctx):
    if ctx.message.server.id == '138067606119645184':
        if ctx.message.author.permissions_in(ctx.message.channel).administrator:
            with open('permissions/channels.txt', 'r') as file:
                a = file.read()
            with open('permissions/roles.txt', 'r') as file:
                b = file.read()
            with open('permissions/users.txt', 'r') as file:
                c = file.read()
            with open('permissions/generalsp.txt', 'r') as file:
                d = file.read()
                if "warlords:" in d.lower():
                    gen = True
                else:
                    gen = False
                if gen:
                    dmg = "Generals+"
                else:
                    dmg = ""
            with open('permissions/officers.txt', 'r') as file:
                e = file.read()
                if "officers:" in e.lower():
                    offi = True
                else:
                    offi = False
                if offi:
                    dmo = "Officers"
                else:
                    dmo = ""
            response = discord.Embed(title='📊 **Poll permissions:**\n',
                                     description='**Channels:**\n'
                                     '%s'
                                     '**Roles:**\n'
                                     '%s'
                                     '**Users:**\n'
                                     '%s'
                                     '**DMs:**\n'
                                     '%s'
                                     '\n%s' % (a, b, c, dmg, dmo), color=0xA5FFF6)
        else:
            response = discord.Embed(title='⛔ Access denied: Administrator required', color=0xBE1931)
    else:
        response = discord.Embed(title='🔒 You can\'t use that command on this server or in a DM', color=0xFFCC4d)
    await bot.say(embed=response)


@bot.command(pass_context=True)
async def clrperms(ctx):
    if ctx.message.server.id == '138067606119645184':
        if ctx.message.author.permissions_in(ctx.message.channel).administrator:
            with open('permissions/registered.txt', 'w') as a:
                a.write('')
            with open('permissions/channels.txt', 'w') as a:
                a.write('')
            with open('permissions/roles.txt', 'w') as a:
                a.write('')
            with open('permissions/users.txt', 'w') as a:
                a.write('')
            response = discord.Embed(title='🗑️ Cleared', color=0xA5FFF6)
        else:
            response = discord.Embed(title='⛔ Access denied: Administrator required', color=0xBE1931)
    else:
        response = discord.Embed(title='🔒 You can\'t use that command on this server or in a DM', color=0xFFCC4d)
    await bot.say(embed=response)


@bot.command(pass_context=True)
async def register(ctx):
    if not ctx.message.channel.is_private:
        if ctx.message.server.id == '138067606119645184':
            with open('permissions/users.txt', 'r') as file:
                a = file.read()
            if ctx.message.author.id in a:
                user = True
            else:
                user = False
            with open('permissions/roles.txt') as file:
                a = file.read()
            tmp = [y.id for y in ctx.message.author.roles]
            for line in tmp:
                if line in a:
                    role = True
            try:
                if user or role:
                    with open('permissions/registered.txt', 'r') as file:
                        a = file.read()
                        target = ctx.message.author.id
                        if target not in a:
                            perm = True
                        else:
                            perm = False
                        if perm:
                            with open('permissions/registered.txt', 'a') as a:
                                a.write('<@&%s>\n' % target)
                            response = discord.Embed(title="✅ Registered", description=" DM me with '^vote yes/no' to vote",
                                                     color=0xA5FFF6)
                        else:
                            response = discord.Embed(title="❗ You already resgistered", color=0xBE1931)
            except UnboundLocalError:
                response = discord.Embed(title='🔒 You do not have the required roles', color=0xFFCC4d)
        else:
            response = discord.Embed(title='🔒 You can\'t use that command on this server.', color=0xFFCC4d)
    else:
        response = discord.Embed(title="⛔ You cannot register in a DM", color=0xBE1931)
    await bot.say(embed=response)


@bot.command(pass_context=True)
async def permit(ctx, args):
    if ctx.message.server.id == '138067606119645184':
        mode = args
        if ctx.message.author.permissions_in(ctx.message.channel).administrator:
            if mode == 'c':
                if ctx.message.channel_mentions:
                    with open('permissions/channels.txt', 'r') as file:
                        a = file.read()
                        for line in ctx.message.channel_mentions:
                            if line.id not in a:
                                perm = True
                            else:
                                perm = False
                            if perm:
                                channel = ctx.message.channel_mentions[0]
                                with open('permissions/channels.txt', 'a') as a:
                                    a.write('<#%s>\n' % line.id)
                                response = discord.Embed(title=f"🔓 {channel} permitted", color=0xFFCC4d)
                            else:
                                response = discord.Embed(title=f"❗ {channel} already permitted", color=0xBE1931)
                else:
                    response = discord.Embed(title='❗ Input must be a channel', color=0xBE1931)
            elif mode == 'u':
                if ctx.message.mentions:
                    with open('permissions/users.txt', 'r') as file:
                        a = file.read()
                        for line in ctx.message.mentions:
                            if line.id not in a:
                                perm = True
                            else:
                                perm = False
                            if perm:
                                user = ctx.message.mentions[0]
                                with open('permissions/users.txt', 'a') as a:
                                    a.write('<@%s>\n' % line.id)
                                response = discord.Embed(title=f"🔓 {user.display_name} permitted", color=0xFFCC4d)
                            else:
                                response = discord.Embed(title=f"❗ {user.display_name} already permitted", color=0xBE1931)
                else:
                    response = discord.Embed(title='❗ Input must be a user', color=0xBE1931)
        else:
            response = discord.Embed(title='⛔ Access denied: Administrator required', color=0xBE1931)
    else:
        response = discord.Embed(title='🔒 You can\'t use that command on this server or in a DM', color=0xFFCC4d)
    await bot.say(embed=response)


@bot.command(pass_context=True)
async def permitr(ctx, args, msg):
    if ctx.message.server.id == '138067606119645184':
        if ctx.message.author.permissions_in(ctx.message.channel).administrator:
            mode = args
            if mode == 'r':
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
                            with open('permissions/roles.txt', 'a') as a:
                                a.write('<@&%s>\n' % target.id)
                            response = discord.Embed(title=f"🔓 {target} permitted", color=0xFFCC4d)
                        else:
                            response = discord.Embed(title=f"❗ {target} already permitted", color=0xBE1931)
                else:
                    response = discord.Embed(title='❗ Input must be a role', color=0xBE1931)
            elif mode == 'dm':
                if msg.lower() == 'generals':
                    with open('lists/generalstmp.txt', 'r') as file:
                        b = file.readlines()
                        with open('permissions/generalsp.txt', 'w') as a:
                            for line in b:
                                a.write(line)
                        response = discord.Embed(title="🔓 Generals permitted", color=0xFFCC4d)
                elif msg.lower() == 'officers':
                    with open('lists/officerstmp.txt', 'r') as file:
                        b = file.readlines()
                        with open('permissions/officers.txt', 'w') as a:
                            for line in b:
                                a.write(line)
                        response = discord.Embed(title="🔓 Officers permitted", color=0xFFCC4d)
                else:
                    response = discord.Embed(title="❗ Input must 'generals' or 'officers'", color=0xBE1931)
            else:
                response = discord.Embed(title='❗ Invalid input', color=0xBE1931)
        else:
            response = discord.Embed(title='⛔ Access denied: Administrator required', color=0xBE1931)
    else:
        response = discord.Embed(title='🔒 You can\'t use that command on this server or in a DM', color=0xFFCC4d)
    await bot.say(embed=response)


@bot.command(pass_context=True)
async def unpermit(ctx, args):
    if ctx.message.server.id == '138067606119645184':
        if ctx.message.author.permissions_in(ctx.message.channel).administrator:
            mode = args
            if mode == 'c':
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
                    channel = ctx.message.channel_mentions[0]
                    response = discord.Embed(title=f"🔒 {channel} unpermitted", color=0xFFCC4d)
                else:
                    response = discord.Embed(title='❗ Input must be a channel', color=0xBE1931)
            elif mode == 'u':
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
                        user = ctx.message.mentions[0]
                        response = discord.Embed(title=f"🔒 {user.display_name} unpermitted", color=0xFFCC4d)
                    else:
                        response = discord.Embed(title='❗ Input must be a user', color=0xBE1931)
            else:
                response = discord.Embed(title='❗ No input', color=0xBE1931)
        else:
            response = discord.Embed(title='⛔ Access denied: Administrator required', color=0xBE1931)
    else:
        response = discord.Embed(title='🔒 You can\'t use that command on this server or in a DM', color=0xFFCC4d)
    await bot.say(embed=response)


@bot.command(pass_context=True)
async def unpermitr(ctx, args, msg):
    if ctx.message.server.id == '138067606119645184':
        if ctx.message.author.permissions_in(ctx.message.channel).administrator:
            mode = args
            if mode == 'r':
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
                        response = discord.Embed(title=f"🔒 {target} unpermitted", color=0xFFCC4d)
                    else:
                        response = discord.Embed(title='❗ Input must be a role', color=0xBE1931)
            elif mode == 'dm':
                if msg.lower() == 'generals':
                    with open('permissions/generalsp.txt', 'w') as a:
                        a.write('')
                    response = discord.Embed(title="🔒 Generals unpermitted", color=0xFFCC4d)
                elif msg.lower() == 'officers':
                    with open('permissions/officers.txt', 'w') as a:
                        a.write('')
                    response = discord.Embed(title="🔒 Officers unpermitted", color=0xFFCC4d)
                else:
                    response = discord.Embed(title="❗ Input must 'generals' or 'officers'", color=0xBE1931)
            else:
                response = discord.Embed(title='❗ Invalid input', color=0xBE1931)
        else:
            response = discord.Embed(title='⛔ Access denied: Administrator required', color=0xBE1931)
    else:
        response = discord.Embed(title='🔒 You can\'t use that command on this server or in a DM', color=0xFFCC4d)
    await bot.say(embed=response)


@bot.command()
async def sleep():
    tmp = await bot.say("`(≧Д≦)` No!!!")
    await asyncio.sleep(3)
    await bot.edit_message(tmp, "Fine...")


@bot.command()
async def github():
    embed = discord.Embed(title=':information_source: GitHub for Kon:', color=0xA5FFF6)
    embed.description = 'https://github.com/Shifty6/Kon'
    await bot.say(embed=embed)


@bot.command()
async def roll(args):
    try:
        guess = abs(int(args[0]))
        if guess < 7:
            if guess > 0:
                die_value = secrets.randbelow(5) + 1
                if die_value == guess:
                    sym = '✔'
                else:
                    sym = '❌'
                response = discord.Embed(color=0xA5FFF6)
                response.add_field(name='🎲 Dice',
                                   value=f'**You Rolled** `{die_value}`\n**Your Guess** `{guess}`\n**Match:** `{sym}`')
            else:
                response = discord.Embed(description='❗ Guess must be positive and not a zero', color=0xBE1931)
        else:
            response = discord.Embed(description='❗ Guess cannot be greater than six', color=0xBE1931)
    except ValueError:
        response = discord.Embed(description='❗ Guess must be a number', color=0xBE1931)
    await bot.say(embed=response)


@bot.event
async def on_message(message):
    await bot.process_commands(message)
    flipped_table = '(╯°□°）╯︵ ┻━┻'
    if flipped_table in message.content:
        table = ['┬─┬ ノ( ^_^ノ)',
                 '┬─┬ ﾉ(° -°ﾉ)',
                 '┬─┬ ノ(゜-゜ノ)',
                 '┬─┬ ノ(ಠ\_ಠノ)',
                 '┻━┻~~~~  ╯(°□° ╯)',
                 '┻━┻====  ╯(°□° ╯)',
                 ' ┬──┬﻿ ¯\_(ツ)',
                 '(ヘ･_･)ヘ┳━┳',
                 'ヘ(´° □°)ヘ┳━┳']
        table_resp = secrets.choice(table)
        await bot.send_message(message.channel, table_resp)
    elif 'natsuki' in message.content.lower():
        await bot.add_reaction(message, emoji='monika:375824498882117635')
    elif 'sayori' in message.content.lower():
        await bot.add_reaction(message, emoji='monika:375824498882117635')
    elif 'yuri' in message.content.lower():
        await bot.add_reaction(message, emoji='monika:375824498882117635')
    elif message.content.lower() == 'f':
        await bot.add_reaction(message, emoji='🇫')
    elif message.author.id == '150060705662500864':
        react = secrets.randbelow(9)
        if react == 0:
            await bot.add_reaction(message, emoji='🍛')


bot.run("token", bot=True)
