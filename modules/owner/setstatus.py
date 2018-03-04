import discord


async def ex(args, message, bot, invoke):
    status = ' '.join(args)
    game = discord.Game(name=status)
    await bot.change_presence(game=game)
    response = discord.Embed(color=0x77B255, title=f'✅ New playing status set to {status}.')
    await message.channel.send(embed=response)
