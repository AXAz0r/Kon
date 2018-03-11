import discord
import json
from checks import server_check, set_dm


def clear_roles(roles_data):
    roles_str = roles_data.get('roles')
    if roles_str is None:
        roles_str = []
    roles_str.clear()
    with open('permissions/roles.json', 'w', encoding='utf-8') as roles_file:
        json.dump(roles_data, roles_file)


async def ex(args, message, bot, invoke):
    if message.guild:
        if server_check(message):
            if message.author.permissions_in(message.channel).administrator:
                with open('permissions/roles.json', encoding='utf-8') as roles_file:
                    roles_data = json.loads(roles_file.read())
                dm_p = roles_data['dm']
                if 'No' not in dm_p:
                    set_dm(roles_data, 'No')
                with open('permissions/roles.json', encoding='utf-8') as roles_file:
                    roles_data = json.loads(roles_file.read())
                clear_roles(roles_data)
                with open('permissions/channels.txt', 'w') as a:
                    a.write('')
                with open('permissions/users.txt', 'w') as a:
                    a.write('')
                response = discord.Embed(title='🗑️ Cleared', color=0x67757f)
            else:
                response = discord.Embed(title='⛔ Access denied: Administrator required', color=0xBE1931)
        else:
            response = discord.Embed(title='🔒 You can\'t use that command on this server', color=0xFFCC4d)
    else:
        response = discord.Embed(title='🔒 You can\'t use that command in a DM', color=0xFFCC4d)
    await message.channel.send(embed=response)
