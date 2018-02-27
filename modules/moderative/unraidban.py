import discord


async def ex(args, message, bot, invoke):
    if message.author.permissions_in(message.channel).administrator:
        fn = 'lists/raidbans.txt'
        targetid = "%s" % message.mentions[0].id
        target = message.mentions[0]
        a = open(fn)
        output = []
        temp = 0
        for line in a:
            if targetid not in line:
                output.append(line)
            else:
                temp += 1
        a.close()
        a = open(fn, 'w')
        a.writelines(output)
        a.close()
        raidban_role = discord.utils.get(message.guild.roles, name='Raid Banned')
        await target.remove_roles(raidban_role)
        if not temp == 0:
            response = discord.Embed(title=f"🔓 {target.display_name} is no longer Raid Banned", color=0xFFCC4d)
        else:
            response = discord.Embed(title="❗ That user wasn\'t Raid Banned", color=0xBE1931)
    else:
        response = discord.Embed(title='⛔ Access denied: Administrator required', color=0xBE1931)
    await message.channel.send(embed=response)
