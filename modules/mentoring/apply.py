import discord


async def ex(args, message, bot, invoke):
        if args:
            if len(args) >= 3:
                user = args[0]
                zone = args[1]
                time = args[2]
                with open('lists/requests.txt', 'a') as a:
                    a.write(f'`{zone} {time}`: {user}' + '\n')
                response = discord.Embed(title="✅ I put you on the 'Student Requests' list", color=0xA5FFF6)
            elif len(args) >= 2:
                user = args[0]
                zone = args[1]
                with open('lists/requests.txt', 'a') as a:
                    a.write(f'`{zone}`: {user}' + '\n')
                response = discord.Embed(title="✅ I put you on the 'Student Requests' list", color=0xA5FFF6)
            else:
                response = discord.Embed(title='❗ Not enough inputs', color=0xBE1931)
                response.set_footer(text='@Username UTC #')
        else:
            response = discord.Embed(title="❗ No input", color=0xBE1931)
        await message.channel.send(embed=response)
