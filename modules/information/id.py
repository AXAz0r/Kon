async def ex(args, message, bot, invoke):
    if args:
        if message.mentions:
            target = message.mentions[0]
        elif message.channel_mentions:
            target = message.channel_mentions[0]
        else:
            target = message.author
    else:
        target = message.author
    await message.channel.send(target.id)
