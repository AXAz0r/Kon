import json
import os
import discord
import asyncio
from checks import private_check, server_check


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


def role_check(message):
    with open('permissions/roles.txt') as file:
        a = file.read()
    roles = [y.id for y in message.author.roles]
    has_role = False
    for role in a:
        if role in roles:
            has_role = True
            break
    return has_role


async def ex(args, message, bot, invoke):
    if private_check(message):
        with open('permissions/registered.txt', 'r') as file:
            a = file.read()
        with open('permissions/warlords.txt', 'r') as file:
            b = file.read()
        with open('permissions/generals.txt', 'r') as file:
            c = file.read()
        with open('permissions/officers.txt', 'r') as file:
            d = file.read()
        msg = "%s" % message.author.id
        if msg in a:
            auth = True
        elif msg in b:
            auth = True
        elif msg in c:
            auth = True
        elif msg in d:
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
            if message.author.id not in voted:
                msg = ' '.join(args).lower()
                if msg == 'yes':
                    dump_vote(vote_data, 'yes', message.author)
                    response = discord.Embed(title='🗳️ Voted!', color=0xA5FFF6)
                elif msg == 'no':
                    dump_vote(vote_data, 'no', message.author)
                    response = discord.Embed(title='🗳️ Voted!', color=0xA5FFF6)
                else:
                    response = discord.Embed(title="❗ Vote must contain 'yes' or 'no'", color=0xBE1931)
            else:
                response = discord.Embed(title='⛔ You already voted', color=0xBE1931)
        else:
            response = discord.Embed(title='⛔ You must register on the server to vote in a DM', color=0xBE1931)
        await message.channel.send(embed=response)
    else:
        if server_check(message):
            try:
                await message.delete()
            except PermissionError:
                response = discord.Embed(title='❗ I don\'t have Manage Messages in this channel', color=0xBE1931)
            with open('permissions/channels.txt', 'r') as file:
                a = file.read()
            chn = "%s" % message.channel.id
            if chn in a:
                channel = True
            else:
                channel = False
            with open('permissions/users.txt', 'r') as file:
                a = file.read()
            msg = "%s" % message.author.id
            if msg in a:
                user = True
            else:
                user = False
            if channel:
                try:
                    if user or role_check:
                        if os.path.exists('lists/vote_data.json'):
                            with open('lists/vote_data.json', encoding='utf-8') as vote_data_file:
                                vote_data = json.loads(vote_data_file.read())
                        else:
                            vote_data = {}
                        voted = vote_data.get('voters') or []
                        msg = ' '.join(args).lower()
                        if message.author.id not in voted:
                            if msg == 'yes':
                                dump_vote(vote_data, 'yes', message.author)
                                response = discord.Embed(title='🗳️ Voted!', color=0xA5FFF6)
                            elif msg == 'no':
                                dump_vote(vote_data, 'no', message.author)
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
        del_response = await message.channel.send(embed=response)
        await asyncio.sleep(4)
        await del_response.delete()

