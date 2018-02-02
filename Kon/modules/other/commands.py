import discord


async def ex(args, message, bot, invoke):
    module = args[0].lower()
    if module == 'mentoring':
        response = discord.Embed(title="Mentor commands", description=
        "```md\n"
        "- addmentor - Adds the targeted user to the 'Mentors' list.\n"
        "- apply - Apply to the 'Students Requests' list.\n"
        "- delline - Remove a line from the 'Student Requests' list.\n"
        "- delmentor - Removes the targeted user from the 'Mentors' list.\n"
        "- mentors - Returns the 'Mentors' list.\n"
        "- requests - Returns the 'Student Requests' list.```",
                                 color=0xA5FFF6)
    elif module == 'moderative':
        response = discord.Embed(title="Raid ban commands\n", description=
        "```md\n"
        "- purge - Delete a specified number of messages.\n"
        "- raidban - Add the targeted user to the 'Raid Banned' list and\nassigns the"
        " 'Raid Banned' role to them.\n"
        "- raidbans - Returns the 'Raid Banned' list.\n"
        "- reboot - Restarts the bot (Bot Owner only).\n"
        "- unraidban - Remove the targeted user from the 'Raid Banned' list\n"
        "and removes the 'Raid Banned' role from them.```", color=0xA5FFF6)
    elif module == 'other':
        response = discord.Embed(title="Other commands\n", description=
        "```md\n"
        "- commands - View a list of the commands.\n"
        "- dance - Makes the bot dance for one minute.\n"
        "- info - Returns various info regarding Kon.\n"
        "- kon - Returns a random image from safebooru with the kitsunemimi tag.\n"
        "- modules - Shows the current command modules for Kon.\n"
        "- ping - Returns the bot latency for Kon.\n"
        "- help - View help for the Mentor commands.\n"
        "- roll - Role a 6 sided dice and try to guess the outcome.\n"
        "- sleep - Tell Kon to go to sleep.```", color=0xA5FFF6)
    elif module == 'voting':
        response = discord.Embed(title="Poll commands\n", description=
        "```md\n"
        "- clrperms - Deletes all the permissions data pertaining to the poll.\n"
        "- clrvotes - Deletes all voting data pertaining to the current poll.\n"
        "- vote - Vote 'yes' or 'no' on the current poll.\n"
        "- votes - Returns the results of the current poll.\n"
        "- voters - Returns a list of users who voted on the current poll.\n"
        "- permit c/dm/r/u - Permits the target to vote or be voted in. c: Channel, dm: "
        "Direct Messages, r: Role, u: User.\n"
        "- perms - Returns the current permissions for the poll.\n"
        "- register - Registers the message author to vote on the poll in a "
        "DM with Kon. Author must be permitted to vote.\n"
        "- setpassword - Resets the password fore votes/voters and DM's it to the command caller after 24h.\n"
        "- unpermit c/dm/r/u - c: Unpermits the target to vote or be voted in. c: Channel, dm: "
        "Direct Messages, r: Role, u: User.```", color=0xA5FFF6)
    else:
        response = discord.Embed(title='❗ Module not found', color=0xBE1931)
    await message.channel.send(embed=response)
