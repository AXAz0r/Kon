import json
import os
import discord
import asyncio
from checks import dm_check, server_check


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


def check_roles(allowed_roles, all_users, user):
    members = []
    for member in all_users:
        if isinstance(member, discord.Member):
            if member.id == user.id:
                members.append(member)
    authorized = False
    for member_item in members:
        for allowed_role in allowed_roles:
            role = discord.utils.find(lambda x: x.id == allowed_role, member_item.roles)
            if role:
                authorized = True
                break
        if authorized:
            break
    return authorized


def auth_check(message):
    if message.guild:
        if server_check(message):
            auth = True
        else:
            auth = False
    else:
        if dm_check():
            auth = True
        else:
            auth = False
    return auth


async def ex(args, message, bot, invoke):
    if message.guild:
        try:
            await message.delete()
        except PermissionError:
            response = discord.Embed(title='❗ I don\'t have Manage Messages in this channel', color=0xBE1931)
            await message.channel.send(embed=response)
    if auth_check(message):
        with open('permissions/channels.txt', 'r') as file:
            a = file.read()
        if f'{message.channel.id}' in a:
            channel = True
        else:
            channel = False
        with open('permissions/users.txt', 'r') as file:
            a = file.read()
        if f'{message.author.id}' in a:
            user = True
        else:
            user = False
        if channel or dm_check():
            with open('permissions/roles.json') as roles_data:
                roles_file = json.loads(roles_data.read())
            rol_p = roles_file['roles']
            if user or check_roles(rol_p, bot.get_all_members(), message.author):
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
                        response = discord.Embed(title='🗳️ Voted!', color=0x9aaab4)
                    elif msg == 'no':
                        dump_vote(vote_data, 'no', message.author)
                        response = discord.Embed(title='🗳️ Voted!', color=0x9aaab4)
                    else:
                        response = discord.Embed(title="❗ Vote must be 'yes' or 'no'", color=0xBE1931)
                else:
                    response = discord.Embed(title='⛔ You already voted', color=0xBE1931)
            else:
                response = discord.Embed(title='🔒 You do not have the required roles', color=0xFFCC4d)
        else:
            response = discord.Embed(title='🔒 You can\'t use that command in this channel', color=0xFFCC4d)
    else:
        if message.guild:
            location = 'on this server'
        else:
            location = 'in a DM'
        response = discord.Embed(title=f'🔒 You can\'t use that command {location}', color=0xFFCC4d)
    del_response = await message.channel.send(embed=response)
    if message.guild:
        await asyncio.sleep(4)
        await del_response.delete()

