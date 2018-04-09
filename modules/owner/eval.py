import discord
import inspect
from checks import owner_check


async def ex(args: list, message: discord.Message, bot, invoke):
    if not owner_check(message):
        await message.channel.send(embed=discord.Embed(title="⛔ You are not the owner", color=0xBE1931))
    else:
        if not args:
            status = discord.Embed(color=0xBE1931, title='❗ Nothing Inputted To Process')
        else:
            try:
                execution = " ".join(args)
                output = eval(execution)
                if inspect.isawaitable(output):
                    output = await output
                status = discord.Embed(title='✅ Executed', color=0x77B255)
                status.add_field(name='Results', value=f'\n```\n{output}\n```')
            except Exception as e:
                status = discord.Embed(color=0xBE1931, title='❗ Error')
                status.add_field(name='Execution Failed', value=f'{e}')
        await message.channel.send(None, embed=status)
