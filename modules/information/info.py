import discord


async def ex(args, message, bot, invoke):
    avatar = 'https://i.imgur.com/qAwBsHO.png'
    github_url = 'https://github.com/Shifty6/Kon'
    response = discord.Embed(color=0xA5FFF6)
    response.set_author(name='Kon: Fox Bot', icon_url=avatar)
    response.add_field(name='Information',
                       value=f'ID: **{bot.user.id}**\nCreated on: **Nov 13, 2017**\nSource code: [Github]({github_url})'
                             f'\nOwner: **Shifty9#0995**\nCommands: **36**\nLatency: **{int(bot.latency * 1000)}ms**',
                       inline=True)
    response.set_footer(text='Credit to AXAz0r#0001 for help')
    await message.channel.send(embed=response)