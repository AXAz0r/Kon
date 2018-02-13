import discord


async def ex(args, message, bot, invoke):
    if message.author.permissions_in(message.channel).administrator:
        msg = ' '.join(args)
        a = open('lists/raidbans.txt', 'a')
        a.write('%s' % msg + '\n')
        a.close()
        target = message.mentions[0]
        raidban_role = discord.utils.get(message.guild.roles, name='Raid Banned')
        await target.add_roles(raidban_role)
        response = discord.Embed(title=f"🔒 {target.display_name} is now Raid Banned", color=0xFFCC4d)
    else:        
        response = discord.Embed(title='⛔ Access denied: Administrator required', color=0xBE1931)
    await message.channel.send(embed=response)
