**Hey there!** We need your **help**! Come support us on [**Patreon**](https://www.patreon.com/ApexSigma)!

## Module Index
- [DEVELOPMENT](#development)
- [HELP](#help)
- [MUSIC](#music)
- [PERMISSIONS](#permissions)
- [UTILITY](#utility)

### DEVELOPMENT
Commands | Description | Example
----------|-------------|--------
`>>addstatus` | Adds a status message to Sigma's database for automatic status rotation. (Bot Owner Only) | `>>addstatus with tentacles`
`>>awardleaderboards` `>>awardlbs` | Awards all the global leaderboards. Basically gives a large amount of Kud to the top 20 users in each leaderboard category. Currency earned, experience, and cookies. (Bot Owner Only) | `>>awardleaderboards`
`>>blacklistmodule` `>>blackmodule` `>>blackmdl` | Disallows a person from using a specific module category. (Bot Owner Only) | `>>blacklistmodule 0123456789 minigames`
`>>blacklistserver` `>>blacklistguild` `>>blacksrv` `>>blackguild` | Marks a server as blacklisted. This disallows any user on that server from using commands. (Bot Owner Only) | `>>blacklistserver 0123456789`
`>>blacklistuser` `>>blackusr` | Marks a user as blacklisted, disallowing them to use any command. (Bot Owner Only) | `>>blacklistuser 0123456789`
`>>destroycurrency` `>>destroykud` `>>descurr` `>>deskud` | Takes away the inputted amount of corrency from the mentioned user. The currency goes first and then the user mention as shown in the example. (Bot Owner Only) | `>>destroycurrency 150 @person`
`>>eject` | Makes Sigma leave a Discord server. (Bot Owner Only) | `>>eject 0123456789`
`>>evaluate` `>>evaluate` `>>eval` `>>py` `>>python` `>>code` `>>exec` | Executes raw python code. This should be used with caution. You should never use this unless you are certain of what you are doing. (Bot Owner Only) | `>>evaluate print('hello world')`
`>>generatecurrency` `>>generatekud` `>>gencurr` `>>genkud` | Awards the mentioned user with the inputted amount of currency. The currency goes first and then the user mention as shown in the example. (Bot Owner Only) | `>>generatecurrency 150 @person`
`>>geterror` | Gets an error's details using the given token. (Bot Owner Only) | `>>geterror 9a2e9a374ac90294f225782f362e2ab1`
`>>getreaction` `>>getreact` | No description provided. (Bot Owner Only) | `>>getreaction 4242ea69`
`>>reload` | Reloads all of the modules in Sigma. This includes both commands and events. (Bot Owner Only) | `>>reload`
`>>removereaction` `>>removereact` `>>delreact` | Remove a reaction with the inputed ID. (Bot Owner Only) | `>>removereaction 1ba2e263f287522f`
`>>removestatus` | Removes a status with the inputed ID from Sigma's status database. (Bot Owner Only) | `>>removestatus 1d9cae144f`
`>>resetleaderboards` `>>resetlbs` | Resets the global leaderboard data. Global experience, currency and cookies. (Bot Owner Only) | `>>resetleaderboards`
`>>sabotageuser` `>>sabusr` | Sabotages a user making them have extreme bad luck in various modules. (Bot Owner Only) | `>>sabotageuser 0123456789`
`>>send` | Sends a message to a user, channel or server. The first argument needs to be the destination parameter. The destination parameter consists of the destination type and ID. The types are U for User and C for Channel. The type and ID are separated by a colon, or two dots put more simply. (Bot Owner Only) | `>>send u:0123456789 We are watching...`
`>>setavatar` | Sets the avatar of the bot either to the linked or attached image. The officially supported formats for bot avatars are JPG and PNG images. Note that bots, like all users, have limited profile changes per time period. (Bot Owner Only) | `>>setavatar https://my_fomain.net/my_avatar.png`
`>>setstatus` | Sets the current playing status of the bot. To use this, the automatic status rotation needs to be disabled. It can be toggled with the togglestatus command. (Bot Owner Only) | `>>setstatus with fishies`
`>>setusername` | Sets the name of the bot to the inputted text. Note that bots, like all users, have limited profile changes per time period. (Bot Owner Only) | `>>setusername Supreme Bot`
`>>shutdown` | Forces the bot to disconnect from Discord and shut down all processes. (Bot Owner Only) | `>>shutdown`
`>>sysexec` `>>sh` | Executes a shell command. Extreme warning! This executes commands in the Operating System's Shell. Command Prompt on Windows and Bash on Linux. It will execute things on the same level of authority as the program is ran by. Meaning, don't do something stupid and wipe your damn root. (Bot Owner Only) | `>>sysexec echo 'Hello'`
`>>test` | For testing purposes, obviously. Used as a placeholder for testing functions. | `>>test`
`>>togglestatus` | Toggles if the automatic status rotation is enabled or disabled. (Bot Owner Only) | `>>togglestatus`
`>>wipeawards` | Removes a user's currency, experience and cookie data. Used when wanting to remove a blacklisted user's ill gotten gains. (Bot Owner Only) | `>>wipeawards 0123456789`
[Back To Top](#module-index)

### HELP
Commands | Description | Example
----------|-------------|--------
`>>commands` `>>modules` `>>cmds` `>>mdls` | If not module name is inputed, it will show the list of available modules. To see the commands in a module category, input that modules name. | `>>commands minigames`
`>>donate` | Shows donation information for Sigma. | `>>donate`
`>>help` `>>h` | Provides the link to Sigma's website and support server. As well as show information about a command if something in inputted. | `>>help fish`
`>>invite` `>>inv` | Provides Sigma's invitation link to add her to your server. | `>>invite`
[Back To Top](#module-index)

### MUSIC
Commands | Description | Example
----------|-------------|--------
`>>disconnect` `>>stop` | Stops the music, disconnects the bot from the current voice channel, and purges the music queue. | `>>disconnect`
`>>nowplaying` `>>currentsong` `>>playing` `>>np` | Shows information regarding the currently playing song. | `>>nowplaying`
`>>pause` | Pauses the music player. | `>>pause`
`>>play` `>>start` | Starts playing the music queue. | `>>play`
`>>queue` `>>add` | Queues up a song to play from YouTube. Either from a direct URL or text search. Playlists are supported but take a long time to process. | `>>queue Kaskade Disarm You Illenium Remix`
`>>repeat` | Toggles if the current queue should be repeated. Whenever a song is played, it's re-added to the end of the queue. | `>>repeat`
`>>resume` | Resumes the music player. | `>>resume`
`>>shuffle` | Randomizes the current song queue. | `>>shuffle`
`>>skip` `>>next` | Skips the currently playing song. | `>>skip`
`>>summon` `>>move` | If the bot isn't connected to any channel, it'll connect to yours. If it is connected, it will move to you. | `>>summon`
`>>unqueue` `>>remove` | Removes a song from the queue. Minimum number is 1 and the maximum is however many items the queue has. Even though list indexes start at zero. | `>>unqueue 5`
[Back To Top](#module-index)

### PERMISSIONS
Commands | Description | Example
----------|-------------|--------
`>>disablecommand` `>>dcmd` `>>cmdoff` `>>commandoff` | Disallows a command to be used on the server. Disabled commands are then overwritten by one of the permit commands. Those with the Administrator permission are not affected. | `>>disablecommand nyaa`
`>>disablemodule` `>>dmdl` `>>mdloff` `>>moduleoff` | Disallows an entire module to be used on the server. Disabled modules are then overwritten by one of the permit commands. Those with the Administrator permission are not affected. | `>>disablemodule fun`
`>>enablecommand` `>>cmdon` `>>commandon` | Enables a previously disabled command. | `>>enablecommand kitsune`
`>>enablemodule` `>>mdlon` `>>moduleon` | Enables a previously disabled module. | `>>enablemodule minigames`
`>>permitchannel` `>>pch` `>>pchs` `>>permch` `>>permchs` `>>permitc` `>>permitcs` `>>permitchannels` | Allows a previously disabled command or module to be used in the specified channel. Follow the usage example, C for command, M for module. Multiple channels can be tagged. | `>>permitchannel m:fun #channel`
`>>permitrole` `>>prl` `>>permrl` `>>permitr` | Specifies a role that can use a disabled command or module group. It needs to be specified if it is a command or module group. If it is a command use C and if it is a module use M following the example. | `>>permitrole c:csshumor Wizards`
`>>permituser` `>>pusr` `>>pusrs` `>>permusr` `>>permusrs` `>>permitu` `>>permitus` `>>permitusers` | Specifies a user that can use a disabled command or module. It needs to be specified if it's a command or module group. If it is a command use C, if it is a module use M, following the usage example. Multiple users can be tagged. | `>>permituser c:pun @person`
`>>unpermitchannel` `>>upch` `>>upchs` `>>unpermch` `>>unpermchs` `>>unpermitc` `>>unpermitcs` `>>unpermitchannels` | Removes the channel override for a disabled command or module. Follow the usage example, C for command, M for module. Multiple channels can be tagged. | `>>unpermitchannel m:fun #channel`
`>>unpermitrole` `>>uprl` `>>unpermrl` `>>unpermitrl` | Removes permissions from a role that can use a disabled command or module group to do so. It needs to be specified if it is a command or module group. If it is a command use C and if it is a module use M following the example. | `>>unpermitrole m:minigames Gamblers`
`>>unpermituser` `>>upusr` `>>upusrs` `>>unpermusr` `>>unpermusrs` `>>unpermitu` `>>unpermitus` `>>unpermitusers` | Unpermits a user from using a previously overridden command or module. It needs to be specified if it's a command or module group. If it is a command use C, if it is a module use M, following the usage example. Multiple users can be tagged. | `>>unpermituser m:fun @person`
[Back To Top](#module-index)

### UTILITY
Commands | Description | Example
----------|-------------|--------
`>>avatar` `>>av` | Shows the mentioned user's avatar. If no user is mentioned, it shows the author's avatar. You can add "gif" to the end of the command to indicate that it's a gif. Or you can add "auto" to make the color strip the dominant color of the image. You can also add "static" to the end to make it return the full sized static version of your avatar. | `>>avatar @person`
`>>botinformation` `>>botinfo` `>>info` | Shows information about the bot, version, codename, authors, etc. | `>>botinformation`
`>>bots` | Lists the bots on the server where the command is used and shows their status. | `>>bots`
`>>channelid` `>>chid` `>>cid` | Shows the User ID of the mentioned channel. If no channel is mentioned, it will show the ID of the channel the command is used in. If you don't want the return message to be an embed, add "text" at the end. | `>>channelid #channel`
`>>channelinformation` `>>channelinfo` `>>chinfo` `>>cinfo` | Shows information and data about the mentioned channel. If no channel is mentioned, it will show data for the channel that the command is used in. | `>>channelinformation #channel`
`>>ingame` | Shows the top played games on the server. | `>>ingame @person`
`>>owners` | Shows a list of Sigma's owners. Users in this list have access to the administration module. | `>>owners`
`>>permissions` `>>perms` | Shows which permissions a user has and which they do not. If no user is mentioned, it will target the message author. | `>>permissions @person`
`>>roleinformation` `>>roleinfo` `>>rinfo` | Shows information and data about the inputted role. Roles mentions do not work here, lookup is done via role name. | `>>roleinformation`
`>>rolepopulation` `>>rolepop` | Shows the population of the inputted role. If no arguments are provided, it will show the top 20 roles by population. | `>>rolepopulation Warlard`
`>>servericon` `>>srvicon` `>>icon` | Shows the server's icon image. | `>>servericon`
`>>serverid` `>>guildid` `>>srvid` `>>sid` `>>gid` | Shows the Server ID of the server the command is used in. | `>>serverid`
`>>serverinformation` `>>serverinfo` `>>sinfo` | Shows information and data about the server that the command is used in. | `>>serverinformation`
`>>statistics` `>>stats` | Shows Sigma's current statistics. Population, message and command counts, and rates since startup. As well as when the bot last started. | `>>statistics`
`>>status` | Shows the status of Sigma's machine. Processor information, memory, storage, network, etc. | `>>status`
`>>userid` `>>uid` | Shows the User ID of the mentioned user. If no user is mentioned, it will show the author's ID. If you don't want the return message to be an embed, add "text" at the end. | `>>userid @person`
`>>userinformation` `>>userinfo` `>>uinfo` | Shows information and data about the mentioned user. If no user is mentioned, it will show data for the message author. | `>>userinformation @person`
`>>whoplays` | Generates a list of users playing the inputted game. | `>>whoplays Overwatch`
[Back To Top](#module-index)