import discord
from checks import private_check


async def ex(args, message, bot, invoke):
    if not private_check(message):
        gld = message.guild
        user_count = 0
        online_count = 0
        dnd_count = 0
        idle_count = 0
        offline_count = 0
        active_count = 0
        for user in gld.members:
            if not user.bot:
                user_count += 1
                if user.status == discord.Status.online:
                    online_count += 1
                if user.status == discord.Status.dnd:
                    dnd_count += 1
                if user.status == discord.Status.idle:
                    idle_count += 1
                if user.status == discord.Status.offline:
                    offline_count += 1
                if user.status != discord.Status.offline:
                    active_count += 1
        active_users = (active_count / user_count) * 100
        active_round = round(active_users, 2)
        other_count = dnd_count + idle_count
        members = f'\nMembers: **{user_count}**'
        members += f'\nOnline: **{online_count}**'
        members += f'\nOffline: **{offline_count}**'
        members += f'\nOther: **{other_count}**'
        members += f'\nActive: **{active_round}%**'
        response = discord.Embed(color=0x66757F)
        response.add_field(name='👥 Member Status', value=members)
        response.set_footer(text='Active is users who are not offline')
    else:
        response = discord.Embed(title='❗ This command is only available in servers', color=0xBE1931)
    await message.channel.send(embed=response)
