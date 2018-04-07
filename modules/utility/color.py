import discord
from checks import server_check


def auth_check(message):
    roles = [xxxxxxxxxxxxxxxxxx, xxxxxxxxxxxxxxxxxx]
    auth = False
    for role in roles:
        if role in [y.id for y in message.author.roles]:
            auth = True
            break
    return auth


async def ex(args, message, bot, invoke):
    if message.guild:
        if server_check(message):
            colors = [xxxxxxxxxxxxxxxxxx, xxxxxxxxxxxxxxxxxx]
            if auth_check(message):
                if args:
                    if str.isdigit(args[0]):
                        lookup = int(colors[int(args[0]) - 1])
                        color_role = discord.utils.find(lambda x: x.id == lookup, message.guild.roles)
                        if color_role:
                            target = message.author
                            for role in colors:
                                if role in [y.id for y in target.roles]:
                                    rem_role = discord.utils.get(message.guild.roles, id=role)
                                    await target.remove_roles(rem_role, reason='Role Self Assigned')
                            await message.author.add_roles(color_role, reason='Role Self Assigned')
                            response = discord.Embed(title=f'✅ Vanity role changed to {color_role.name}', color=0x77b255)
                        else:
                            response = discord.Embed(title=f'❗ Error finding that role', color=0xBE1931)
                    else:
                        response = discord.Embed(title='❗ Input must be a number', color=0xBE1931)
                else:
                    i = 1
                    output = ''
                    for color in colors:
                        output += f'#{i} - <@&{color}>\n'
                        i += 1
                    response = discord.Embed(color=0x66757F)
                    response.add_field(name='🎨 Staff Colors', value=output)
                    response.set_footer(text='^color 1 to assign a role')
            else:
                response = discord.Embed(title="⛔ You are not a staff member", color=0xBE1931)
        else:
            response = discord.Embed(title='🔒 You can\'t use that command on this server', color=0xFFCC4d)
    else:
        response = discord.Embed(title='🔒 You can\'t use that command in a DM', color=0xFFCC4d)
    await message.channel.send(embed=response)
