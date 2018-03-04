import discord
from checks import server_check


async def ex(args, message, bot, invoke):
    if server_check(message):
        if message.author.permissions_in(message.channel).administrator:
            with open('permissions/registered.txt', 'w') as a:
                a.write('')
            with open('permissions/warlords.txt', 'w') as a:
                a.write('')
            with open('permissions/generals.txt', 'w') as a:
                a.write('')
            with open('permissions/officers.txt', 'w') as a:
                a.write('')
            with open('permissions/channels.txt', 'w') as a:
                a.write('')
            with open('permissions/roles.txt', 'w') as a:
                a.write('')
            with open('permissions/users.txt', 'w') as a:
                a.write('')
            response = discord.Embed(title='🗑️ Cleared', color=0x67757F)
        else:
            response = discord.Embed(title='⛔ Access denied: Administrator required', color=0xBE1931)
    else:
        response = discord.Embed(title='🔒 You can\'t use that command on this server', color=0xFFCC4d)
    await message.channel.send(embed=response)
