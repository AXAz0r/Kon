import aiohttp
import discord
from checks import owner_check


async def ex(args, message, bot, invoke):
    if owner_check(message):
        if args or message.attachments:
            if message.attachments:
                image_url = message.attachments[0].url
            else:
                image_url = ' '.join(args)
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.get(image_url) as image_response:
                        img_data = await image_response.read()
                await bot.user.edit(avatar=img_data)
                response = discord.Embed(title=f'✅ My avatar has been changed.', color=0x77B255)
            except discord.Forbidden:
                response = discord.Embed(title=f'❗ I was unable to change my avatar.', color=0xBE1931)
        else:
            response = discord.Embed(itle='❗ Give me a link or attach an image, please.', color=0xBE1931)
    else:
        response = discord.Embed(title="⛔ You are not the owner", color=0xBE1931)
    await message.channel.send(embed=response)
