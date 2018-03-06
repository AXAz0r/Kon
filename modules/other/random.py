import discord
import secrets


async def ex(args, message, bot, invoke):
    if args:
        try:
            if len(args) == 1:
                high_end = int(args[0])
                if high_end:
                    ran_num = secrets.randbelow(high_end)
                    response = discord.Embed(title=f'🎲 {ran_num}', color=0xEA596E)
                else:
                    response = discord.Embed(title='❗ Invalid number', color=0xBE1931)
            else:
                response = discord.Embed(title='❗ Too many arguments', color=0xBE1931)
        except ValueError:
            response = discord.Embed(title='❗ Invalid number', color=0xBE1931)
    else:
        ran_num = secrets.randbelow(1000000)
        response = discord.Embed(title=f"🎲 Random number: {ran_num}", color=0xEA596E)
    await message.channel.send(embed=response)
