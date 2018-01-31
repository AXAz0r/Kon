import json
import os
import discord
from checks import server_check


if os.path.exists('lists/vote_data.json'):
    with open('lists/vote_data.json') as json_data_file:
        votes_cfg = json.load(json_data_file)


if os.path.exists('lists/password_data.json'):
    with open('lists/password_data.json') as json_data_file:
        password_cfg = json.load(json_data_file)


async def ex(args, message, bot, invoke):
    if server_check(message):
        if message.author.permissions_in(message.channel).administrator:
            if args:
                try:
                    with open('lists/password_data.json', encoding='utf-8') as pswd_data_file:
                        pswd_data = json.loads(pswd_data_file.read())
                    pswd = pswd_data.get('pswd')
                    msg = ' '.join(args)
                    if msg in pswd:
                        voters = votes_cfg.get('voters') or []
                        line_list = []
                        for voter in voters:
                            line_list.append('<@' + voter + '>')
                        a = '\n'.join(line_list)
                        response = discord.Embed(title="**Voters:**", color=0xA5FFF6)
                        response.description = ('%s' % a)
                    else:
                        response = discord.Embed(title='🔒 Incorrect password', color=0xFFCC4d)
                except NameError:
                    response = discord.Embed(title='❗ There is no vote data', color=0xBE1931)
            else:
                response = discord.Embed(title='🔒 A password is required', color=0xFFCC4d)
        else:
            response = discord.Embed(title='⛔ Access denied: Administrator required', color=0xBE1931)
    else:
        response = discord.Embed(title='🔒 You can\'t use that command on this server', color=0xFFCC4d)
    await message.channel.send(embed=response)
