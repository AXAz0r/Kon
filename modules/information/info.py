import discord
from koncore import commands_list


async def ex(args, message, bot, invoke):
    avatar = 'https://i.imgur.com/qAwBsHO.png'
    github_url = 'https://github.com/Shifty6/Kon'
    cmd_count = len(commands_list)
    info_block = f'ID: **{bot.user.py.id}**\nCreated on: **Nov 13, 2017**\nSource code: [Github]({github_url})'
    info_block += f'\nOwner: **Shifty9#0995**\nCommands: **{cmd_count}**\nLatency: **{int(bot.latency * 1000)}ms**'
    response = discord.Embed(color=0xA5FFF6)
    response.set_author(name='Kon: Fox Bot', icon_url=avatar)
    response.add_field(name='Information', value=info_block, inline=True)
    response.set_footer(text='Credit to AXAz0r#0001 for help')  # <3 love ya shif
    await message.channel.send(embed=response)
