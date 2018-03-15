import discord


async def ex(args, message, bot, invoke):
    if args:
        all_qry = ' '.join(args).lower()
        rl_qrys = ''.join(all_qry[0:])
        rl_qry = rl_qrys.split('; ')
        members = [[], []]
        rl_num = -1
        err = False
        for qry in rl_qry:
            rl_num += 1
            role_search = discord.utils.find(lambda x: x.name.lower() == qry, message.guild.roles)
            if role_search:
                for member in message.guild.members:
                    member_role_search = discord.utils.find(lambda x: x.id == role_search.id, member.roles)
                    if member_role_search:
                        members[int(f'{rl_num}')].append(member.id)
            else:
                err = True
                break
        if not err:
            matches = 0
            for member in members[0]:
                if member in members[1]:
                    matches += 1
            response = discord.Embed(color=0x696969)
            response.set_author(name=message.guild.name, icon_url=message.guild.icon_url)
            response.add_field(name=f'Population with both roles', value=f'```py\n{matches}\n```')
        else:
            response = discord.Embed(title=f'🔍 I couldn\'t find {qry} on this server', color=0x696969)
    else:
        response = discord.Embed(title='❗ No input', color=0xBE1931)
    await message.channel.send(embed=response)
