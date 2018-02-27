import secrets
from koncore import bot


async def on_message(message):
    await bot.process_commands(message)
    flipped_table = '(╯°□°）╯︵ ┻━┻'
    if flipped_table in message.content:
        table = ['┬─┬ ノ( ^_^ノ)',
                 '┬─┬ ﾉ(° -°ﾉ)',
                 '┬─┬ ノ(゜-゜ノ)',
                 '┬─┬ ノ(ಠ\_ಠノ)',
                 '┻━┻~~~~  ╯(°□° ╯)',
                 '┻━┻====  ╯(°□° ╯)',
                 ' ┬──┬﻿ ¯\_(ツ)',
                 '(ヘ･_･)ヘ┳━┳',
                 'ヘ(´° □°)ヘ┳━┳']
        table_resp = secrets.choice(table)
        await message.send.channel(message.channel, table_resp)
    elif 'natsuki' in message.content.lower():
        await message.add_reaction(message, emoji='monika:375824498882117635')
    elif 'sayori' in message.content.lower():
        await message.add_reaction(message, emoji='monika:375824498882117635')
    elif 'yuri' in message.content.lower():
        await message.add_reaction(message, emoji='monika:375824498882117635')
    elif message.content.lower() == 'f':
        await message.add_reaction(message, emoji='🇫')
