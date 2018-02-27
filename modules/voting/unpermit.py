import discord
from checks import server_check


async def ex(args, message, bot, invoke):
    if server_check(message):
        if message.author.permissions_in(message.channel).administrator:
            if args:
                if len(args) >= 2:
                    mode = args[0].lower()
                    if mode == 'c':
                        if message.channel_mentions:
                            target = "%s" % message.channel_mentions[0].id
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
                            channel = message.channel_mentions[0]
                            response = discord.Embed(title=f"🔒 {channel} unpermitted", color=0xFFCC4d)
                        else:
                            response = discord.Embed(title='❗ Input must be a channel', color=0xBE1931)
                    elif mode == 'u':
                        if message.author.permissions_in(message.channel).administrator:
                            if message.mentions:
                                target = message.mentions[0].id
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
                                user = message.mentions[0]
                                response = discord.Embed(title=f"🔒 {user.display_name} unpermitted", color=0xFFCC4d)
                            else:
                                response = discord.Embed(title='❗ Input must be a user', color=0xBE1931)
                    elif mode == 'r':
                        lookup = ' '.join(args[1:]).lower()
                        target = discord.utils.find(lambda x: x.name.lower() == lookup, message.guild.roles)
                        if message.author.permissions_in(message.channel).administrator:
                            if target is not None:
                                fn = 'permissions/roles.txt'
                                a = open(fn)
                                output = []
                                for line in a:
                                    role = "%s" % target.id
                                    if role not in line:
                                        output.append(line)
                                a.close()
                                a = open(fn, 'w')
                                a.writelines(output)
                                a.close()
                                response = discord.Embed(title=f"🔒 {target} unpermitted", color=0xFFCC4d)
                            else:
                                response = discord.Embed(title='❗ Input must be a role', color=0xBE1931)
                    elif mode == 'dm':
                        lookup = ' '.join(args[1:]).lower()
                        if lookup == 'warlords':
                            with open('permissions/warlords.txt', 'w') as a:
                                a.write('')
                            response = discord.Embed(title="🔒 Warlords unpermitted", color=0xFFCC4d)
                        elif lookup == 'generals':
                            with open('permissions/generals.txt', 'w') as a:
                                a.write('')
                            response = discord.Embed(title="🔒 Generals unpermitted", color=0xFFCC4d)
                        elif lookup == 'officers':
                            with open('permissions/officers.txt', 'w') as a:
                                a.write('')
                            response = discord.Embed(title="🔒 Officers unpermitted", color=0xFFCC4d)
                        else:
                            response = discord.Embed(title="❗ Input must 'generals' or 'officers'", color=0xBE1931)
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
