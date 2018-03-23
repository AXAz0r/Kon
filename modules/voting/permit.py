import discord
import json
from checks import server_check, set_dm


def channel_auth(message):
    with open('permissions/channels.txt') as file:
        a = file.read()
    if message.channel_mentions:
        channel = message.channel_mentions[0]
        channel_perm = False
        if f'{channel.id}' in a:
            channel_perm = True
    else:
        channel_perm = None
    return channel_perm


def user_auth(message):
    with open('permissions/users.txt') as file:
        a = file.read()
    if message.mentions:
        user = message.mentions[0]
        user_perm = False
        if f'{user.id}' in a:
            user_perm = True
    else:
        user_perm = None
    return user_perm


def role_auth(args, message):
    lookup = ' '.join(args[1:]).lower()
    target = discord.utils.find(lambda x: x.name.lower() == lookup, message.guild.roles)
    with open('permissions/roles.json', encoding='utf-8') as vote_data_file:
        vote_file = json.loads(vote_data_file.read())
    rol_p = vote_file['roles']
    role_perm = False
    for role in rol_p:
        if role == target.id:
            role_perm = True
            break
    return role_perm


async def ex(args, message, bot, invoke):
    if message.guild:
        if server_check(message):
            if message.author.permissions_in(message.channel).administrator:
                if args:
                    mode = args[0].lower()
                    if len(args) >= 2:
                        if mode == 'c':
                            if message.channel_mentions:
                                channel = message.channel_mentions[0]
                                if not channel_auth(message):
                                    with open('permissions/channels.txt', 'a') as a:
                                        a.write(f'{channel.mention}\n')
                                    response = discord.Embed(title=f"🔓 Permitted {channel}", color=0xFFCC4d)
                                else:
                                    response = discord.Embed(title=f"❗ {channel} is already permitted", color=0xBE1931)
                            else:
                                response = discord.Embed(title='❗ Input must be a channel', color=0xBE1931)
                        elif mode == 'u':
                            if message.mentions:
                                user = message.mentions[0]
                                if not user_auth(message):
                                    with open('permissions/users.txt', 'a') as a:
                                        a.write(f'{user.mention}\n')
                                    response = discord.Embed(title=f"🔓 Permitted {user.display_name}", color=0xFFCC4d)
                                else:
                                    response = discord.Embed(title=f"❗ {user.display_name} is already permitted",
                                                             color=0xBE1931)
                            else:
                                response = discord.Embed(title='❗ Input must be a user', color=0xBE1931)
                        elif mode == 'r':
                            lookup = ' '.join(args[1:]).lower()
                            target = discord.utils.find(lambda x: x.name.lower() == lookup, message.guild.roles)
                            if target is not None:
                                with open('permissions/roles.json', encoding='utf-8') as vote_data_file:
                                    vote_file = json.loads(vote_data_file.read())
                                rol_p = vote_file['roles']
                                if not role_auth(args, message):
                                    rol_p.append(target.id)
                                    vote_file.update({'roles': rol_p})
                                    with open('permissions/roles.json', 'w', encoding='utf-8') as vote_data_file:
                                        json.dump(vote_file, vote_data_file)
                                    response = discord.Embed(title=f"🔓 Permitted {target}", color=0xFFCC4d)
                                else:
                                    response = discord.Embed(title=f"❗ {target} is already permitted", color=0xBE1931)
                            else:
                                response = discord.Embed(title=f'🔍 I couldn\'t find {lookup} on this server', color=0x696969)
                        else:
                            response = discord.Embed(title='❗ Invalid input', color=0xBE1931)
                    elif len(args) == 1:
                        if mode == 'dm':
                            with open('permissions/roles.json', encoding='utf-8') as roles_file:
                                roles_data = json.loads(roles_file.read())
                            dm_p = roles_data['dm']
                            if 'Yes' not in dm_p:
                                set_dm(roles_data, 'Yes')
                                response = discord.Embed(title="🔓 Permitted DMs", color=0xFFCC4d)
                            else:
                                response = discord.Embed(title="❗ DMs already permitted", color=0xBE1931)
                        else:
                            response = discord.Embed(title='❗ Invalid input', color=0xBE1931)
                    else:
                        response = discord.Embed(title='❗ Two inputs are required', color=0xBE1931)
                else:
                    response = discord.Embed(title='❗ No input', color=0xBE1931)
            else:
                response = discord.Embed(title='⛔ Access denied: Administrator required', color=0xBE1931)
        else:
            response = discord.Embed(title='🔒 You can\'t use that command on this server', color=0xFFCC4d)
    else:
        response = discord.Embed(title='🔒 You can\'t use that command in a DM', color=0xFFCC4d)
    await message.channel.send(embed=response)
