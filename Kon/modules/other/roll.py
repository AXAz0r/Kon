import secrets
import discord


async def ex(args, message, bot, invoke):
    try:
        guess = abs(int(args[0]))
        if guess < 7:
            if guess > 0:
                die_value = secrets.randbelow(5) + 1
                if die_value == guess:
                    sym = '✔'
                else:
                    sym = '❌'
                response = discord.Embed(color=0xA5FFF6)
                response.add_field(name='🎲 Dice',
                                   value=f'**You Rolled** `{die_value}`\n**Your Guess** `{guess}`\n**Match:** `{sym}`')
            else:
                response = discord.Embed(description='❗ Guess must be positive and not a zero', color=0xBE1931)
        else:
            response = discord.Embed(description='❗ Guess cannot be greater than six', color=0xBE1931)
    except ValueError:
        response = discord.Embed(description='❗ Guess must be a number', color=0xBE1931)
    await message.channel.send(embed=response)
