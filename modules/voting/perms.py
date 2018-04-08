import discord
import json
from checks import server_check


async def ex(args, message, bot, invoke):
    if message.guild:
        if server_check(message):
            if message.author.permissions_in(message.channel).manage_guild:
                with open('permissions/channels.txt', 'r') as file:
                    a = file.read()
                    if '' == a:
                        chn = 'None\n'
                    else:
                        chn = f'\n{a}'
                with open('permissions/roles.json', encoding='utf-8') as vote_data_file:
                    vote_file = json.loads(vote_data_file.read())
                rol_p = vote_file['roles']
                roles = ''
                for role in rol_p:
                    roles += f'<@&{role}>\n'
                if '' == roles:
                    rol = 'None\n'
                else:
                    rol = f'\n{roles}'
                with open('permissions/users.txt', 'r') as file:
                    c = file.read()
                    if '' == c:
                        usr = 'None\n'
                    else:
                        usr = f'\n{c}'
                with open('permissions/roles.json') as roles_data:
                    roles_file = json.loads(roles_data.read())
                dm_p = roles_file['dm']
                if 'Yes' in dm_p:
                    dm = 'Yes\n'
                else:
                    dm = 'No\n'
                response = discord.Embed(title='🔏 **Poll permissions:**\n',
                                         description=f'**DMs Allowed:** {dm}'
                                         f'**Channels:** {chn}'
                                         f'**Roles:** {rol}'
                                         f'**Users:** {usr}', color=0xFFCC4d)
            else:
                response = discord.Embed(title='⛔ Access denied: Manage Server required', color=0xBE1931)
        else:
            response = discord.Embed(title='🔒 You can\'t use that command on this server', color=0xFFCC4d)
    else:
        response = discord.Embed(title='🔒 You can\'t use that command in a DM', color=0xFFCC4d)
    await message.channel.send(embed=response)
