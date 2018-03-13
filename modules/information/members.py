import discord


async def ex(args, message, bot, invoke):
    if message.guild:
        gld = message.guild
        counts = [0, 0, 0, 0, 0, 0, 0]
        for user in gld.members:
            if not user.bot:
                counts[0] += 1
                if user.status == discord.Status.online:
                    counts[1] += 1
                if user.status == discord.Status.dnd:
                    counts[2] += 1
                if user.status == discord.Status.idle:
                    counts[3] += 1
                if user.status == discord.Status.offline:
                    counts[4] += 1
                if user.status != discord.Status.offline:
                    counts[5] += 1
            else:
                counts[6] += 1
        active_users = (counts[5] / counts[0]) * 100
        active_round = round(active_users, 2)
        other_count = counts[2] + counts[3]
        members = f'\nMembers: **{counts[0]}**'
        members += f'\nOnline: **{counts[1]}**'
        members += f'\nOffline: **{counts[4]}**'
        members += f'\nOther: **{other_count}**'
        members += f'\nBots: **{counts[6]}**'
        members += f'\nActive: **{active_round}%**'
        response = discord.Embed(color=0x66757F)
        response.add_field(name='👥 Member Status', value=members)
        response.set_footer(text='Active is users who are not offline')
    else:
        response = discord.Embed(title='🔒 You can\'t use that command in a DM', color=0xFFCC4d)
    await message.channel.send(embed=response)
