import discord
import asyncio
import arrow


def generate_log_embed(message, target, channel, deleted):
    user = message.author
    avatar = user.avatar_url
    response = discord.Embed(color=0x696969, timestamp=arrow.utcnow().datetime)
    response.set_author(name=f'#{channel.name} Has Been Pruned', icon_url=avatar)
    if target:
        target_text = f'{target.mention}\n{target.name}#{target.discriminator}'
    else:
        target_text = 'No Filter'
    response.add_field(name='🗑 Prune Details',
                       value=f'Amount: {len(deleted)} Messages\nTarget: {target_text}',
                       inline=True)
    author = message.author
    response.add_field(name='🛡 Responsible',
                       value=f'{author.mention}\n{author.name}#{author.discriminator}',
                       inline=True)
    response.set_footer(text=f'ChannelID: {channel.id}')
    return response


async def ex(args: list, message: discord.Message, bot, invoke):
    if not message.author.permissions_in(message.channel).manage_messages:
        response = discord.Embed(title='⛔ Access Denied. Manage Messages needed.', color=0xBE1931)
    else:
        purge_images = 'attachments' in args
        purge_filter = None
        arg_index = 0
        for arg in args:
            if arg.startswith('content:'):
                purge_filter = " ".join([arg.split(':')[1]] + args[arg_index + 1:])
                break
            arg_index += 1
        target = bot.user
        count = 100
        if message.mentions:
            target = message.mentions[0]
            if len(args) == 2:
                try:
                    count = int(args[0])
                except ValueError:
                    count = 100
        else:
            if args:
                target = None
                try:
                    count = int(args[0])
                except ValueError:
                    count = 100
        if count > 100:
            count = 100

        def purge_target_check(msg):
            if not msg.pinned:
                if msg.author.id == target.id:
                    if purge_images:
                        if msg.attachments:
                            clean = True
                        else:
                            clean = False
                    elif purge_filter:
                        if purge_filter.lower() in msg.content.lower():
                            clean = True
                        else:
                            clean = False
                    else:
                        clean = True
                else:
                    clean = False
            else:
                clean = False
            return clean

        def purge_wide_check(msg):
            if not msg.pinned:
                if purge_images:
                    if msg.attachments:
                        clean = True
                    else:
                        clean = False
                elif purge_filter:
                    if purge_filter.lower() in msg.content.lower():
                        clean = True
                    else:
                        clean = False
                else:
                    clean = True
            else:
                clean = False
            return clean

        try:
            await message.delete()
        except discord.NotFound:
            pass
        if target:
            try:
                deleted = await message.channel.purge(limit=count, check=purge_target_check)
            except Exception:
                deleted = []
                pass
        else:
            try:
                deleted = await message.channel.purge(limit=count, check=purge_wide_check)
            except Exception:
                deleted = []
                pass
        response = discord.Embed(color=0x77B255, title=f'✅ Deleted {len(deleted)} Messages')
        if message.guild.id == xxxxxxxxxxxxxxxxxx:
            all_channels = bot.get_all_channels()
            log_embed = generate_log_embed(message, target, message.channel, deleted)
            log_channel = discord.utils.find(lambda x: x.id == xxxxxxxxxxxxxxxxxx, all_channels)
            await log_channel.send(embed=log_embed)
    del_response = await message.channel.send(embed=response)
    await asyncio.sleep(5)
    try:
        await del_response.delete()
    except discord.NotFound:
        pass
