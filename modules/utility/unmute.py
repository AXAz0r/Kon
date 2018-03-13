import discord
import arrow


def hierarchy_permit(author, target):
    top_author_role = author.top_role.position
    top_target_role = target.top_role.position
    return top_author_role > top_target_role


def mute_check(message):
    target = message.mentions[0]
    mute_list = open('lists/muted.txt', 'r')
    muted = False
    for line in mute_list:
        if f'{target.id}' in line.lower():
            muted = True
            break
    mute_list.close()
    return muted


def generate_log_embed(message, target, args):
    user = message.author
    avatar = user.avatar_url
    log_embed = discord.Embed(color=0x696969, timestamp=arrow.utcnow().datetime)
    log_embed.set_author(name='A Member Has Been Unmuted', icon_url=avatar)
    log_embed.add_field(name='🔊 Unmuted User',
                        value=f'{target.mention}\n{target.name}#{target.discriminator}', inline=True)
    author = message.author
    log_embed.add_field(name='🛡 Responsible',
                        value=f'{author.mention}\n{author.name}#{author.discriminator}', inline=True)
    if len(args) > 1:
        log_embed.add_field(name='📄 Reason', value=f"```\n{' '.join(args[1:])}\n```", inline=False)
    log_embed.set_footer(text=f'UserID: {target.id}')
    return log_embed


async def ex(args, message, bot, invoke):
    if not message.guild:
        response = discord.Embed(title='🔒 You can\'t use that command in a DM', color=0xFFCC4d)
    elif not message.author.permissions_in(message.channel).manage_messages:
        response = discord.Embed(title='⛔ Access Denied. Manage Messages needed.', color=0xBE1931)
    else:
        if not message.mentions:
            response = discord.Embed(title='❗ No user targeted.', color=0xBE1931)
        else:
            author = message.author
            target = message.mentions[0]
            if author.id == target.id:
                response = discord.Embed(title='❗ Can\'t unmute yourself.', color=0xBE1931)
            else:
                above_hier = hierarchy_permit(author, target)
                if not above_hier:
                    response = discord.Embed(title='⛔ Can\'t unmute someone equal or above you.', color=0xBE1931)
                else:
                    fn = 'lists/muted.txt'
                    mute_list = open(fn)
                    output = []
                    for line in mute_list:
                        if f'{target.id}' not in line.lower():
                            output.append(line)
                    mute_list.close()
                    if mute_check(message):
                        response = discord.Embed(title=f'✅ {target.display_name} has been unmuted.', color=0x77B255)
                        if message.guild.id == 138067606119645184:
                            all_channels = bot.get_all_channels()
                            log_embed = generate_log_embed(message, target, args)
                            log_channel = discord.utils.find(lambda x: x.id == 302665883849850881, all_channels)
                            await log_channel.send(embed=log_embed)
                    else:
                        response = discord.Embed(title=f'❗ {target.display_name} is not text muted.',
                                                 color=0xBE1931)
                    mute_list = open(fn, 'w')
                    mute_list.writelines(output)
                    mute_list.close()
    await message.channel.send(embed=response)
