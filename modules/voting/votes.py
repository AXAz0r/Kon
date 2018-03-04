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


def make_bar(points, total):
    try:
        fill = int((points / total) * 10)
    except ZeroDivisionError:
        fill = 0
    empty = 10 - fill
    bar = f'[{fill * "▣"}{empty * "▢"}]'
    return bar


async def ex(args, message, bot, invoke):
    if server_check(message):
        if message.author.permissions_in(message.channel).administrator:
            pswd = password_cfg.get('pswd')
            if args:
                try:
                    msg = ' '.join(args)
                    if msg in pswd:
                        yes_points = votes_cfg.get('yes') or 0
                        no_points = votes_cfg.get('no') or 0
                        total = yes_points + no_points
                        yes_bar = make_bar(yes_points, total)
                        try:
                            yes_perc_base = yes_points / total
                        except ZeroDivisionError:
                            yes_perc_base = 0
                        yes_stat_line = f'[{yes_points}] {yes_bar} {int(yes_perc_base * 100)}% - Yes'
                        no_bar = make_bar(no_points, total)
                        try:
                            no_perc_base = no_points / total
                        except ZeroDivisionError:
                            no_perc_base = 0
                        no_stat_line = f'[{no_points}] {no_bar} {int(no_perc_base * 100)}% - No'
                        response = discord.Embed(title=f'📊 Poll Statistics', color=0xD2DAE1)
                        output = f'{yes_stat_line}\n' \
                                 f'{no_stat_line}'
                        response.description = f'```{output}```'
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
