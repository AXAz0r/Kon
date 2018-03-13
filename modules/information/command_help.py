import discord


async def ex(args, message, bot, invoke):
    if args:
        module = args[0].lower()
        if module == 'information':
            response = discord.Embed(title="Infomration commands", description="```md\n"
            "- commands - Returns the current command modules for Kon. If a module is specified, "
            "it will return a list of the commands for that module.\n"
            "- help - View help for the Mentor commands.\n"
            "- info - Returns various info regarding Kon.\n"
            "- members - Returns the total number of members as well as how many are online, offline, other, and active.\n"
            "- ping - Returns the bot latency for Kon.\n"
            "- user - Returns various information on the mentioned user, If no user is mentioned, it returns your own "
            "information.```")
        elif module == 'mentoring':
            response = discord.Embed(color=0xA5FFF6, title="Mentor commands", description="```md\n"
            "- addmentor - Adds the targeted user to the 'Mentors' list.\n"
            "- apply - Adds the targeted user to the 'Students Requests' list.\n"
            "- delline - Removes a line from the 'Student Requests' list.\n"
            "- delmentor - Removes the targeted user from the 'Mentors' list.\n"
            "- mentors - Returns the 'Mentors' list.\n"
            "- requests - Returns the 'Student Requests' list.```")
        elif module == 'owner':
            response = discord.Embed(color=0xA5FFF6, title="Raid ban commands\n", description="```md\n"
            "- reboot - Restarts the bot (Bot Owner only).\n"
            "- setavatar - Sets the avatar of the bot either to the linked or attached image.\n"
            "- setstatus - Sets the playing status of the bot.")
        elif module == 'utility':
            response = discord.Embed(color=0xA5FFF6, title="Other commands\n", description="```md\n"
            "- dance - Makes the bot dance for one minute.\n"
            "- kon - Returns a random image from safebooru with the kitsunemimi tag.\n"
            "- match - Returns a member who is special picked just for you.\n"
            "- mute - Marks the mentioned user as muted and deletes any messages by them. A reason can be stated after "
            "the mention if desired.\n"
            "- purge - Delete a specified number of messages.\n"
            "- link - Generates a hyperlink where text is the first argument and the url is the second argument. "
            "You can enter multiple links by separating them with > (space on both sides of it).\n"
            "- random - Returns a random number below 1000000. If a number is specified, the random number will be "
            "below it.\n"
            "- roll - Role a 6 sided dice and try to guess the outcome.\n"
            "- sleep - Tells Kon to go to sleep.\n"
            "- unmute - Unmarks the mentioned user as muted and stops deleting their messages. A reason can be stated "
            "after the mention if desired.```")
        elif module == 'voting':
            response = discord.Embed(color=0xA5FFF6, title="Poll commands\n", description="```md\n"
            "- clrperms - Deletes all the permissions data pertaining to the poll.\n"
            "- clrvotes - Deletes all voting data pertaining to the current poll.\n"
            "- vote - Vote 'yes' or 'no' on the current poll.\n"
            "- votes - Returns the results of the current poll.\n"
            "- voters - Returns a list of users who voted on the current poll.\n"
            "- password - Returns the password for voting data if it's available. Otherwise it displays how long until "
            "it becomes available.\n"
            "- permit c/dm/r/u - Permits the target to vote or be voted in. c: Channel, dm: "
            "Direct Messages, r: Role, u: User.\n"
            "- perms - Returns the current permissions for the poll.\n"
            "- register - Registers the message author to vote on the poll in a "
            "DM with Kon. Author must be permitted to vote.\n"
            "- setpassword - Resets the password for voting data and makes it available after 24h. The password cannot "
            "be reset before it is made available unless the current password is provided as an argument.\n"
            "- unpermit c/dm/r/u - c: Unpermits the target to vote or be voted in. c: Channel, dm: "
            "Direct Messages, r: Role, u: User.```")
        else:
            response = discord.Embed(title="❗ I couldn't find that module", color=0xBE1931)
    else:
        response = discord.Embed(color=0xA5FFF6, description='**There are 5 modules**\n'
                                 '```yml\n- INFORMATION\n- MENTORING\n- OWNER\n- UTILITY\n-VOTING```')
        response.set_footer(text='^commands module')
    await message.channel.send(embed=response)
