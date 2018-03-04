import discord
from checks import server_check, private_check


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
    if not private_check(message):
        if server_check(message):
            with open('permissions/users.txt', 'r') as file:
                a = file.read()
            user = "%s" % message.author.id
            if user in a:
                user = True
            else:
                user = False
            try:
                if user or role_check:
                    with open('permissions/registered.txt', 'r') as file:
                        a = file.read()
                        target = "%s" % message.author.id
                        if target not in a:
                            perm = True
                        else:
                            perm = False
                        if perm:
                            with open('permissions/registered.txt', 'a') as a:
                                a.write('<@&%s>\n' % target)
                            response = discord.Embed(title="✅ Registered", description=" DM me with ^vote yes/no to vote",
                                                     color=0x77B255)
                        else:
                            response = discord.Embed(title="❗ You already resgistered", color=0xBE1931)
            except UnboundLocalError:
                response = discord.Embed(title='🔒 You do not have the required roles', color=0xFFCC4d)
        else:
            response = discord.Embed(title='🔒 You can\'t use that command on this server.', color=0xFFCC4d)
    else:
        response = discord.Embed(title="⛔ You can\'t register in a DM", color=0xBE1931)
    await message.channel.send(embed=response)
