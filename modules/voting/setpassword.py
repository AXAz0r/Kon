import json
import os
import random
import asyncio
import discord
import string
from checks import server_check, private_check


def set_pswd(pswd_data, pswd_str, password: str):
    pswd_str = pswd_data.get('pswd')
    if pswd_str is None:
        pswd_str = []
    pswd_str.clear()
    pswd_str.append(password)
    pswd_data.update({'pswd': pswd_str})
    with open('lists/password_data.json', 'w', encoding='utf-8') as pswd_data_file:
        json.dump(pswd_data, pswd_data_file)


def id_generator(size=6, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def get_pswd():
    with open('lists/password_data.json', encoding='utf-8') as pswd_data_file:
        pswd_data = json.loads(pswd_data_file.read())
        pswd_str = pswd_data.get('pswd') or []
    for pswd in pswd_str:
        return pswd


async def ex(args, message, bot, invoke):
    if private_check:
        if server_check(message):
            if message.author.permissions_in(message.channel).administrator:
                if os.path.exists('lists/password_data.json'):
                    with open('lists/password_data.json', encoding='utf-8') as pswd_data_file:
                        pswd_data = json.loads(pswd_data_file.read())
                else:
                    pswd_data = {}
                if message.mentions:
                    target = message.mentions[0]
                    pronoun = 'them'
                else:
                    target = message.author
                    pronoun = 'you'
                set_pswd(pswd_data, 'pswd', id_generator())
                response = discord.Embed(title=f'🔐 Password reset. It will be DM\'d to {pronoun} in 24h', color=0xFFCC4d)
                await message.channel.send(embed=response)
                target_reply = discord.Embed(title=f'🔑 Here is the password `{get_pswd()}`', color=0xc1694f)
                target_reply.set_footer(text=f'^votes/voters password')
                await asyncio.sleep(86400)
                await bot.send_message(target, embed=target_reply)
                return pswd_data
            else:
                response = discord.Embed(title='⛔ Access denied: Administrator required', color=0xBE1931)
        else:
            response = discord.Embed(title='🔒 You can\'t use that command on this server', color=0xFFCC4d)
    else:
        response = discord.Embed(title='🔒 You can\'t use that command in a DM', color=0xFFCC4d)
    await message.channel.send(embed=response)
