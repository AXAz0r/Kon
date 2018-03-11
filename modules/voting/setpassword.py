import json
import random
import arrow
import discord
import string
from checks import server_check


def set_pswd(pswd_data, password: str):
    pswd_str = pswd_data.get('pswd')
    if pswd_str is None:
        pswd_str = []
    pswd_str.clear()
    pswd_str.append(password)
    pswd_data.update({'pswd': pswd_str})
    with open('lists/password_data.json', 'w', encoding='utf-8') as pswd_data_file:
        json.dump(pswd_data, pswd_data_file)


def id_gen(size=6, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def set_time(pass_data, time_auth: str):
    time_str = pass_data.get('time')
    if time_str is None:
        time_str = []
    del time_str
    pass_data.update({'time': time_auth})
    with open('lists/password_data.json', 'w', encoding='utf-8') as pass_file:
        json.dump(pass_data, pass_file)


async def ex(args, message, bot, invoke):
    if message.guild:
        if server_check(message):
            if message.author.permissions_in(message.channel).manage_guild:
                with open('lists/password_data.json', encoding='utf-8') as pswd_data_file:
                    pswd_data = json.loads(pswd_data_file.read())
                set_pswd(pswd_data, id_gen())
                response = discord.Embed(title=f'🔐 Password reset. It will be available in 24h', color=0xFFCC4d)
                with open('lists/password_data.json', encoding='utf-8') as pass_file:
                    pass_data = json.loads(pass_file.read())
                available_stamp = arrow.utcnow().timestamp + 86400
                set_time(pass_data, available_stamp)
            else:
                response = discord.Embed(title='⛔ Access denied: Manage Server required', color=0xBE1931)
        else:
            response = discord.Embed(title='🔒 You can\'t use that command on this server', color=0xFFCC4d)
    else:
        response = discord.Embed(title='🔒 You can\'t use that command in a DM', color=0xFFCC4d)
    await message.channel.send(embed=response)

