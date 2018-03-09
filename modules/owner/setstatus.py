import discord
import json
from checks import owner_check


async def ex(args, message, bot, invoke):
    if owner_check(message):
        if args:
            status = ' '.join(args)
            activity = discord.Activity(type=discord.ActivityType.playing, name=status)
            await bot.change_presence(activity=activity)
            response = discord.Embed(title=f'✅ New playing status set to {status}.', color=0x77B255)
            with open('config.json', 'r') as config_data:
                status_data = json.load(config_data)
            status_data['Status'] = f'{status}'
            with open('config.json', 'w') as config_data:
                json.dump(status_data, config_data, sort_keys=True, indent=4)
        else:
            response = discord.Embed(itle='❗ Give me a status to change to, please.', color=0xBE1931)
    else:
        response = discord.Embed(title="⛔ You are not the owner", color=0xBE1931)
    await message.channel.send(embed=response)
