import discord


async def ex(args, message, bot, invoke):
    if message.author.permissions_in(message.channel).administrator:
        allow = True
    else:
        allow = False
    if not allow:
        response = discord.Embed(title='⛔ Access denied: Administrator required', color=0xBE1931)
    else:
        fn = 'lists/raidbans.txt'
        target = message.mentions[0]
        a = open(fn)
        output = []
        for line in a:
            if target.id not in line:
                output.append(line)
        a.close()
        a = open(fn, 'w')
        a.writelines(output)
        a.close()
        raidban_role = discord.utils.get(message.guild.roles, name='Raid Banned')
        await target.remove_roles(raidban_role)
        response = discord.Embed(title=f"🔓 {target.display_name} is no longer Raid Banned", color=0xFFCC4d)
    await message.channel.send(embed=response)
