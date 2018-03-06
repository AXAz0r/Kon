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
                    title = '🎲 **Dice**'
                    tmp = f'\n**Your Guess** `{guess}`\n**Match:** `{sym}`'
                    desc = f'**You Rolled** `{die_value}`{tmp}'
                    color = 0xEA596E
                else:
                    title = '❗ Guess must be positive and not a zero'
                    desc = ''
                    color = 0xBE1931
            else:
                title = '❗ Guess cannot be greater than six'
                desc = ''
                color = 0xBE1931
        except ValueError:
            title = '❗ Guess must be a number'
            desc = ''
            color = 0xBE1931
    else:
        title = '🎲 **Dice**'
        desc = f'**You Rolled** `{die_value}`'
        color = 0xEA596E
    response = discord.Embed(title=f'{title}', description=f'{desc}', color=color)
    await message.channel.send(embed=response)
