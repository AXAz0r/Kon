import asyncio
import discord


async def ex(args, message, bot, invoke):
    response = await message.channel.send("`(≧Д≦)` No!!!")
    await asyncio.sleep(3)
    await response.edit(content="Fine...")
