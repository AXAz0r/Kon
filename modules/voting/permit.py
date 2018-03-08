import discord
from checks import server_check


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
    with open('permissions/roles.txt') as file:
        a = file.read()
    role_perm = False
    if f'{target.id}' in a:
        role_perm = True
    return role_perm


async def ex(args, message, bot, invoke):
    if server_check(message):
        if message.author.permissions_in(message.channel).administrator:
            if args:
                if len(args) >= 2:
                    mode = args[0].lower()
                    if mode == 'c':
                        if message.channel_mentions:
                            channel = message.channel_mentions[0]
                            if not channel_auth(message):
                                with open('permissions/channels.txt', 'a') as a:
                                    a.write(f'<#{channel.id}>\n')
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
                                    a.write(f'<@{user.id}>\n')
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
                            if not user_auth(message):
                                with open('permissions/roles.txt', 'a') as a:
                                    a.write(f'<@&{target.id}>\n')
                                response = discord.Embed(title=f"🔓 Permitted {target}", color=0xFFCC4d)
                            else:
                                response = discord.Embed(title=f"❗ {target} is already permitted", color=0xBE1931)
                        else:
                            response = discord.Embed(title=f'❗ I couldn\'t find {lookup} on this server', color=0xBE1931)
                    elif mode == 'dm':
                        lookup = ' '.join(args[1:]).lower()
                        if lookup == 'warlords':
                            with open('lists/warlords.txt', 'r') as file:
                                a = file.readlines()
                                with open('permissions/warlords.txt', 'w') as b:
                                    for line in a:
                                        b.write(line)
                                response = discord.Embed(title="🔓 Warlods permitted", color=0xFFCC4d)
                        elif lookup == 'generals':
                            with open('lists/generals.txt', 'r') as file:
                                a = file.readlines()
                                with open('permissions/generals.txt', 'w') as b:
                                    for line in a:
                                        b.write(line)
                                response = discord.Embed(title="🔓 Generals permitted", color=0xFFCC4d)
                        elif lookup == 'officers':
                            with open('lists/officers.txt', 'r') as file:
                                b = file.readlines()
                                with open('permissions/officers.txt', 'w') as a:
                                    for line in b:
                                        a.write(line)
                                response = discord.Embed(title="🔓 Officers permitted", color=0xFFCC4d)
                        else:
                            response = discord.Embed(title="❗ Input must warlords, generals or officers", color=0xBE1931)
                    else:
                        response = discord.Embed(title='❗ Invalid input', color=0xBE1931)
                else:
                    response = discord.Embed(title='❗ Two inputs are required', color=0xBE1931)
            else:
                response = discord.Embed(title='❗ No input', color=0xBE1931)
        else:
            response = discord.Embed(title='⛔ Access denied: Administrator required', color=0xBE1931)
    else:
        response = discord.Embed(title='🔒 You can\'t use that command on this server or in a DM', color=0xFFCC4d)
    await message.channel.send(embed=response)
