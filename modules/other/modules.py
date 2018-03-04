import discord


async def ex(args, message, bot, invoke):
    response = discord.Embed(description='**There are 4 modules**\n'
                                      '```yml\n'
                                      '- MENTORING\n'
                                      '- MODERATIVE\n'
                                      '- OTHER\n'
                                      '- VOTING```', color=0xA5FFF6)
    response.set_footer(text=f'^commands module_name')
    await message.channel.send(embed=response)
