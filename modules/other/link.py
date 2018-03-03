import discord


async def ex(args, message, bot, invoke):
    await message.delete()
    if not args:
        response = discord.Embed(title='❗ No input', color=0xBE1931)
        await message.channel.send(embed=response)
        return
    if not len(args) >= 2:
        response = discord.Embed(title='❗ Not enough inputs', color=0xBE1931)
        await message.channel.send(embed=response)
        return
    else:
        err = ''
        desc = ''
        link_num = 0
        all_qry = ' '.join(args)
        hyp_qrys = ' > '.join(all_qry.split(' > ')[0:])
        hyp_qry = hyp_qrys.split(' > ')
        for qry in hyp_qry:
            link_num += 1
            curr_link = link_num
            link_name = ''.join(qry.split('; ')[0])
            url_string = qry.split('; ')[1]
            if link_name is not '':
                if "http" in url_string:
                    if ' ' not in url_string:
                        desc += f'[{link_name}]({url_string})\n'
                    else:
                        err += f'**Link #{curr_link}** `URL cannot contain spaces`\n'
                else:
                    err += f'**Link #{curr_link}** `URL must include http/s`\n'

            else:
                err += f'**Link #{curr_link}** `Format: Google Home; https://www.google.com`\n'
        if err is not '':
            err_header = f'**Error:**'
        else:
            err_header = ''
        response = discord.Embed(description=f'{desc} \n{err_header}\n{err}', color=0x0f80a6)
        response.set_author(name='Hyperlink', icon_url='https://i.imgur.com/tUo5WrQ.png')
        await message.channel.send(embed=response)
