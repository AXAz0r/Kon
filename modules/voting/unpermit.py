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


async def ex(args, message, bot, invoke):
    if message.guild:
        if server_check(message):
            if message.author.permissions_in(message.channel).manage_guild:
                if args:
                    mode = args[0].lower()
                    if len(args) >= 2:
                        if mode == 'c':
                            if message.channel_mentions:
                                channel = message.channel_mentions[0]
                                if channel_auth(message):
                                    fn = 'permissions/channels.txt'
                                    a = open(fn)
                                    output = []
                                    for line in a:
                                        if f'{channel.id}' not in line:
                                            output.append(line)
                                    a.close()
                                    a = open(fn, 'w')
                                    a.writelines(output)
                                    a.close()
                                    channel = message.channel_mentions[0]
                                    response = discord.Embed(title=f"🔒 Unpermitted {channel}", color=0xFFCC4d)
                                else:
                                    response = discord.Embed(title=f"❗ {channel} wasn't permitted", color=0xBE1931)
                            else:
                                response = discord.Embed(title='❗ Input must be a channel', color=0xBE1931)
                        elif mode == 'u':
                            user = message.mentions[0]
                            if message.mentions:
                                if user_auth(message):
                                    fn = 'permissions/users.txt'
                                    a = open(fn)
                                    output = []
                                    for line in a:
                                        if f'{user.id}' not in line:
                                            output.append(line)
                                    a.close()
                                    a = open(fn, 'w')
                                    a.writelines(output)
                                    a.close()
                                    response = discord.Embed(title=f"🔒 Unpermitted {user.display_name}", color=0xFFCC4d)
                                else:
                                    response = discord.Embed(title=f"❗ {user.display_name} wasn't permitted", color=0xBE1931)
                            else:
                                response = discord.Embed(title='❗ Input must be a user', color=0xBE1931)
                        elif mode == 'r':
                            lookup = ' '.join(args[1:]).lower()
                            target = discord.utils.find(lambda x: x.name.lower() == lookup, message.guild.roles)
                            if target is not None:
                                with open('permissions/roles.json', encoding='utf-8') as roles_file:
                                    roles_data = json.loads(roles_file.read())
                                rol_p = roles_data['roles']
                                roles = []
                                role_ex = False
                                for role in rol_p:
                                    if role == target.id:
                                        role_ex = True
                                    else:
                                        roles.append(role)
                                if role_ex:
                                    roles_data.update({'roles': roles})
                                    with open('permissions/roles.json', 'w', encoding='utf-8') as roles_file:
                                        json.dump(roles_data, roles_file)
                                    response = discord.Embed(title=f"🔒 Unpermitted {target}", color=0xFFCC4d)
                                else:
                                    response = discord.Embed(title=f"❗ {target} wasn't permitted", color=0xBE1931)
                            else:
                                response = discord.Embed(title=f'🔍 I couldn\'t find {lookup} on this server', color=0x696969)
                        else:
                            response = discord.Embed(title='❗ Invalid input', color=0xBE1931)
                    elif len(args) == 1:
                        if mode == 'dm':
                            with open('permissions/roles.json', encoding='utf-8') as roles_file:
                                roles_data = json.loads(roles_file.read())
                            dm_p = roles_data['dm']
                            if 'No' not in dm_p:
                                set_dm(roles_data, 'No')
                                response = discord.Embed(title="🔒 Unpermitted DMs", color=0xFFCC4d)
                            else:
                                response = discord.Embed(title="❗ DMs wasn't permitted", color=0xBE1931)
                        else:
                            response = discord.Embed(title='❗ Invalid input', color=0xBE1931)
                    else:
                        response = discord.Embed(title='❗ Two inputs are required', color=0xBE1931)
                else:
                    response = discord.Embed(title='❗ No input', color=0xBE1931)
            else:
                response = discord.Embed(title='⛔ Access denied: Manage Server required', color=0xBE1931)
        else:
            response = discord.Embed(title='🔒 You can\'t use that command on this server', color=0xFFCC4d)
    else:
        response = discord.Embed(title='🔒 You can\'t use that command in a DM', color=0xFFCC4d)
    await message.channel.send(embed=response)
