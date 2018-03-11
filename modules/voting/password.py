import discord
import arrow
import json
from checks import server_check


def get_pswd():
    with open('lists/password_data.json', encoding='utf-8') as pswd_data_file:
        pswd_data = json.loads(pswd_data_file.read())
        pswd_str = pswd_data.get('pswd') or []
    for pswd in pswd_str:
        return pswd


async def ex(args, message, bot, invoke):
    with open('lists/password_data.json', encoding='utf-8') as pass_file:
        pass_data = json.loads(pass_file.read())
    available_stamp = pass_data['time']
    current_stamp = arrow.utcnow().timestamp
    time_diff = arrow.get(available_stamp + 5).humanize(arrow.utcnow())
    if message.guild:
        if server_check(message):
            if message.author.permissions_in(message.channel).manage_guild:
                if current_stamp > available_stamp:
                    response = discord.Embed(title=f'🔑 Here is the password `{get_pswd()}`', color=0xc1694f)
                    response.set_footer(text='^votes/voters password')
                else:
                    response = discord.Embed(title='🔒 The password is not yet available', color=0xFFCC4d)
                    response.set_footer(text=f'It will be available in {time_diff}')
            else:
                response = discord.Embed(title='⛔ Access denied: Manage Server required', color=0xBE1931)
        else:
            response = discord.Embed(title='🔒 You can\'t use that command on this server', color=0xFFCC4d)
    else:
        response = discord.Embed(title='🔒 You can\'t use that command in a DM', color=0xFFCC4d)
    await message.channel.send(embed=response)

