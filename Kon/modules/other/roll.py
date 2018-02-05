import secrets
import discord


async def ex(args, message, bot, invoke):
    die_value = secrets.randbelow(5) + 1
    if args:
        try:
            guess = abs(int(args[0]))
            if guess < 7:
                if guess > 0:
                    if die_value == guess:
                        sym = '✔'
                    else:
                        sym = '❌'
                    tmp = f'\n**Your Guess** `{guess}`\n**Match:** `{sym}`'
                    desc = f'🎲 **Dice**\n**You Rolled** `{die_value}`{tmp}'
                    color = 0xA5FFF6
                else:
                    desc = '❗ Guess must be positive and not a zero'
                    color = 0xBE1931
            else:
                desc = '❗ Guess cannot be greater than six'
                color = 0xBE1931
        except ValueError:
            desc = '❗ Guess must be a number'
            color = 0xBE1931
    else:
        desc = f'🎲 **Dice**\n**You Rolled** `{die_value}`'
        color = 0xA5FFF6
    response = discord.Embed(description=f'{desc}', color=color)
    await message.channel.send(embed=response)
