import discord
import arrow


def generate_log_embed(message, target, args):
    user = message.author
    avatar = user.avatar_url
    log_embed = discord.Embed(color=0x696969, timestamp=arrow.utcnow().datetime)
    log_embed.set_author(name='A Member Has Been Quarantine', icon_url=avatar)
    log_embed.add_field(name='☣ Quarantine User',
                        value=f'{target.mention}\n{target.name}#{target.discriminator}', inline=True)
    author = message.author
    log_embed.add_field(name='🛡 Responsible',
                        value=f'{author.mention}\n{author.name}#{author.discriminator}', inline=True)
    if len(args) > 1:
        log_embed.add_field(name='📄 Reason', value=f"```\n{' '.join(args[1:])}\n```", inline=False)
    log_embed.set_footer(text=f'UserID: {target.id}')
    return log_embed


def hierarchy_permit(author, target):
    top_author_role = author.top_role.position
    top_target_role = target.top_role.position
    return top_author_role > top_target_role


async def ex(args: list, message: discord.Message, bot, invoke):
    if message.author.permissions_in(message.channel).manage_channels:
        if message.mentions:
            target = message.mentions[0]
            author = message.author
            hierarchy_me = hierarchy_permit(message.guild.me, target)
            if hierarchy_me:
                if hierarchy_permit(author, target):
                    if len(args) > 1:
                        reason = ' '.join(args[1:])
                    else:
                        reason = 'Not stated.'
                    channel = discord.utils.find(lambda x: x.id == xxxxxxxxxxxxxxxxxx, bot.get_all_channels())
                    await channel.set_permissions(target, send_messages=False, add_reactions=False, reason=reason)
                    response = discord.Embed(title=f'✅ {target.display_name} has been banned from {channel}.', color=0x77B255)
                    if message.guild.id == xxxxxxxxxxxxxxxxxx:
                        all_channels = bot.get_all_channels()
                        log_embed = generate_log_embed(message, target, args)
                        log_channel = discord.utils.find(lambda x: x.id == xxxxxxxxxxxxxxxxxx, all_channels)
                        await log_channel.send(embed=log_embed)
                else:
                    response = discord.Embed(title='⛔ That user is equal or above you.', color=0xBE1931)
            else:
                response = discord.Embed(title='⛔ Can\'t quarantine someone equal or above me.', color=0xBE1931)
        else:
            response = discord.Embed(title='❗ No user targeted.', color=0xBE1931)
    else:
        response = discord.Embed(title='⛔ Access Denied. Manage Channels needed.', color=0xBE1931)
    await message.channel.send(embed=response)
