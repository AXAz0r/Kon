import discord


async def ex(args, message, bot, invoke):
    embed = discord.Embed(title="❔ Hi! I can add your name to the Student Requests list!", color=0xA5FFF6)
    embed.description = 'Type `^apply @username UTC #` to be added to the list.\n' \
                        'Type `^requests` to get the current Student Requests list.\n' \
                        'Type `^mentors` to get a list of the current Mentors.\n' \
                        'Type `^modules` to get a list of my modules and their commands.\n' \
                        'If you\'d like your name removed, please ping <@208974392644861952>. 💕'
    await message.channel.send(embed=embed)
