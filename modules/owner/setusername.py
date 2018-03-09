import discord
from checks import owner_check


async def ex(args, message, bot, invoke):
    if owner_check(message):
        if args:
            try:
                name_input = ' '.join(args)
                await bot.user.edit(username=name_input)
                response = discord.Embed(color=0x77B255, title=f'✅ Changed username to {name_input}.')
            except discord.Forbidden:
                response = discord.Embed(color=0xBE1931, title=f'❗ I was unable to change my username.')
        else:
            response = discord.Embed(title='❗ Give me a username to change to, please.', color=0xBE1931)
    else:
        response = discord.Embed(title="⛔ You are not the owner", color=0xBE1931)
    await message.channel.send(embed=response)
