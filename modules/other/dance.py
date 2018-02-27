import asyncio
import itertools


async def ex(args, message, bot, invoke):
    tmp = await message.channel.send("`:D/-<`")
    for _ in itertools.repeat(None, 20):
        await asyncio.sleep(1.5)
        new = "`:D\-<`"
        await tmp.edit(content=new)
        await asyncio.sleep(1.5)
        new = "`:D/-<`"
        await tmp.edit(content=new)
