import discord


async def ex(args: list, message: discord.Message, bot, invoke):
    if args:
        if len(args) >= 2:
            if ':' in args[0].lower():
                mode, identifier = args[0].split(':')
                identifier = int(identifier)
                mode = mode.lower()
                text = ' '.join(args[1:])
                if mode == 'u':
                    target = discord.utils.find(lambda x: x.id == identifier, bot.get_all_members())
                    title_end = f'{target.name}#{target.discriminator}'
                elif mode == 'c':
                    target = discord.utils.find(lambda x: x.id == identifier, bot.get_all_channels())
                    title_end = f'#{target.name} on {target.guild.name}'
                else:
                    response = discord.Embed(color=0xBE1931, title='❗ Invalid Arguments Given')
                    await message.channel.send(embed=response)
                    return
                await target.send(text)
                response = discord.Embed(color=0x77B255, title=f'✅ Message sent to {title_end}')
            else:
                response = discord.Embed(color=0xBE1931, title='❗ Separate the target type and ID with a colon')
        else:
            response = discord.Embed(color=0xBE1931, title='❗ Not Enough Arguments')
    else:
        response = discord.Embed(color=0xBE1931, title='❗ No Arguments Given')
    await message.channel.send(embed=response)
