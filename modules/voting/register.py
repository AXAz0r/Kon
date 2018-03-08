import discord
from checks import server_check, private_check


def user_auth(message):
    with open('permissions/users.txt') as file:
        a = file.read()
    user = message.author.id
    user_perm = False
    if f'{user.id}' in a:
        user_perm = True
    return user_perm


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


def reg_auth(message):
    with open('permissions/registered.txt') as file:
        a = file.read()
    target = message.author.id
    if f'{target}' in a:
        reg_perm = True
    else:
        reg_perm = False
    return reg_perm


async def ex(args, message, bot, invoke):
    if not private_check(message):
        if server_check(message):
            try:
                if user_auth or role_check:
                    target = message.author.id
                    if reg_auth:
                        with open('permissions/registered.txt', 'a') as a:
                            a.write(f'<@&{target}>\n')
                        response = discord.Embed(title="✅ Registered", description=" DM me with ^vote yes/no to vote",
                                                 color=0x77b255)
                    else:
                        response = discord.Embed(title="❗ You already resgistered", color=0xBE1931)
            except UnboundLocalError:
                response = discord.Embed(title='🔒 You do not have the required roles', color=0xFFCC4d)
        else:
            response = discord.Embed(title='🔒 You can\'t use that command on this server.', color=0xFFCC4d)
    else:
        response = discord.Embed(title="⛔ You can\'t register in a DM", color=0xBE1931)
    await message.channel.send(embed=response)
