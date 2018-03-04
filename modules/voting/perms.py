import discord
from checks import server_check


async def ex(args, message, bot, invoke):
    if server_check(message):
        if message.author.permissions_in(message.channel).administrator:
            with open('permissions/channels.txt', 'r') as file:
                a = file.read()
            with open('permissions/roles.txt', 'r') as file:
                b = file.read()
            with open('permissions/users.txt', 'r') as file:
                c = file.read()
            with open('permissions/warlords.txt', 'r') as file:
                d = file.read()
                if "warlords:" in d.lower():
                    warlords = True
                else:
                    warlords = False
                if warlords:
                    dmw = "Warlords"
                else:
                    dmw = ""
            with open('permissions/generals.txt', 'r') as file:
                d = file.read()
                if "generals:" in d.lower():
                    generals = True
                else:
                    generals = False
                if generals:
                    dmg = "Generals"
                else:
                    dmg = ""
            with open('permissions/officers.txt', 'r') as file:
                e = file.read()
                if "officers:" in e.lower():
                    officers = True
                else:
                    officers = False
                if officers:
                    dmo = "Officers"
                else:
                    dmo = ""
            response = discord.Embed(title='🔏 **Poll permissions:**\n',
                                     description='**Channels:**\n'
                                     '%s'
                                     '**Roles:**\n'
                                     '%s'
                                     '**Users:**\n'
                                     '%s'
                                     '**DMs:**\n'
                                     '%s\n%s\n%s' % (a, b, c, dmw, dmg, dmo), color=0xFFCC4D)
        else:
            response = discord.Embed(title='⛔ Access denied: Administrator required', color=0xBE1931)
    else:
        response = discord.Embed(title='🔒 You can\'t use that command on this server', color=0xFFCC4d)
    await message.channel.send(embed=response)
