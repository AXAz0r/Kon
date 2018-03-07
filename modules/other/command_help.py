import discord


async def ex(args, message, bot, invoke):
    if args:
        module = args[0].lower()
        if module == 'mentoring':
            response = discord.Embed(title="Mentor commands", description=
            "```md\n"
            "- addmentor - Adds the targeted user to the 'Mentors' list.\n"
            "- apply - Adds the targeted user to the 'Students Requests' list.\n"
            "- delline - Removes a line from the 'Student Requests' list.\n"
            "- delmentor - Removes the targeted user from the 'Mentors' list.\n"
            "- mentors - Returns the 'Mentors' list.\n"
            "- requests - Returns the 'Student Requests' list.```",
                                     color=0xA5FFF6)
        elif module == 'other':
            response = discord.Embed(title="Other commands\n", description=
            "```md\n"
            "- commands - Returns the current command modules for Kon. If a module is specified, "
            "it will return a list of the commands for that module.\n"
            "- dance - Makes the bot dance for one minute.\n"
            "- info - Returns various info regarding Kon.\n"
            "- kon - Returns a random image from safebooru with the kitsunemimi tag.\n"
            "- match - Returns a member who is special picked just for you.\n"
            "- members - Returns the total number of members as well as how many are online, offline, other and active.\n"
            "- ping - Returns the bot latency for Kon.\n"
            "- purge - Delete a specified number of messages.\n"
            "- help - View help for the Mentor commands.\n"
            "- link - Generates a hyperlink where text is the first argument and the url is the second argument. "
            "You can enter multiple links by separating them with > (space on both sides of it).\n"
            "- random - Returns a random number below 1000000. If a number is specified, the random number will be "
            "below it.\n"
            "- roll - Role a 6 sided dice and try to guess the outcome.\n"
            "- sleep - Tell Kon to go to sleep.```", color=0xA5FFF6)
        elif module == 'owner':
            response = discord.Embed(title="Raid ban commands\n", description=
            "```md\n"
            "- reboot - Restarts the bot (Bot Owner only).\n"
            "- setavatar - Sets the avatar of the bot either to the linked or attached image.\n"
            "- setstatus - Sets the playing status of the bot.", color=0xA5FFF6)
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
            response = discord.Embed(title="❗ I couldn't find that module", color=0xBE1931)
    else:
        response = discord.Embed(description='**There are 4 modules**\n'
                                             '```yml\n- MENTORING\n- OTHER\n- OWNER\n- VOTING```', color=0xA5FFF6)
        response.set_footer(text='^commands module_name')
    await message.channel.send(embed=response)
