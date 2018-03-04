import discord
from checks import private_check


async def ex(args, message, bot, invoke):
    if not private_check(message):
        gld = message.guild
        offline_users = len([x for x in message.guild.members if x.status == discord.Status.offline])
        dnd_users = len([x for x in message.guild.members if x.status == discord.Status.dnd])
        idle_users = len([x for x in message.guild.members if x.status == discord.Status.idle])
        online_users = len([x for x in message.guild.members if x.status == discord.Status.online])
        not_offline = len([x for x in message.guild.members if x.status != discord.Status.offline])
        user_count = 0
        for user in gld.members:
            if not user.bot:
                user_count += 1
        active_users = (not_offline / user_count) * 100
        active_round = round(active_users, 2)
        other_status = dnd_users + idle_users
        members = f'\nMembers: **{user_count}**'
        members += f'\nOnline: **{online_users}**'
        members += f'\nOffline: **{offline_users}**'
        members += f'\nOther: **{other_status}**'
        members += f'\nActive: **{active_round}%**'
        response = discord.Embed(color=0x292F33)
        response.add_field(name='👥 Member Status', value=members)
        response.set_footer(text='Active is users who are not offline')
    else:
        response = discord.Embed(title='❗ This command is only available in servers', color=0xBE1931)
    await message.channel.send(embed=response)
