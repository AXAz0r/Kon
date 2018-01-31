import discord
from checks import server_check


async def ex(args, message, bot, invoke):
    if server_check(message):
        mode = ' '.join(args)
        if message.author.permissions_in(message.channel).administrator:
            if args:
                if len(args) >= 2:
                    mode = args[0].lower()
                    if mode == 'c':
                        if message.channel_mentions:
                            with open('permissions/channels.txt', 'r') as file:
                                a = file.read()
                                for line in message.channel_mentions:
                                    trg = "%s" % line.id
                                    if trg not in a:
                                        perm = True
                                    else:
                                        perm = False
                                    channel = message.channel_mentions[0]
                                    if perm:
                                        with open('permissions/channels.txt', 'a') as a:
                                            a.write('<#%s>\n' % line.id)
                                        response = discord.Embed(title=f"🔓 {channel} permitted", color=0xFFCC4d)
                                    else:
                                        response = discord.Embed(title=f"❗ {channel} already permitted", color=0xBE1931)
                        else:
                            response = discord.Embed(title='❗ Input must be a channel', color=0xBE1931)
                    elif mode == 'u':
                        if message.mentions:
                            with open('permissions/users.txt', 'r') as file:
                                a = file.read()
                                for line in message.mentions:
                                    trg = "%s" % line.id
                                    if trg not in a:
                                        perm = True
                                    else:
                                        perm = False
                                    if perm:
                                        user = message.mentions[0]
                                        with open('permissions/users.txt', 'a') as a:
                                            a.write('<@%s>\n' % line.id)
                                        response = discord.Embed(title=f"🔓 {user.display_name} permitted", color=0xFFCC4d)
                                    else:
                                        response = discord.Embed(title=f"❗ {user.display_name} already permitted",
                                                                 color=0xBE1931)
                        else:
                            response = discord.Embed(title='❗ Input must be a user', color=0xBE1931)
                    elif mode == 'r':
                        lookup = ' '.join(args[1:]).lower()
                        target = discord.utils.find(lambda x: x.name.lower() == lookup, message.guild.roles)
                        if target is not None:
                            with open('permissions/roles.txt', 'r') as file:
                                a = file.read()
                                trg = "%s" % target.id
                                if trg not in a:
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
