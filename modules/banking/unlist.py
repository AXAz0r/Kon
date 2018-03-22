import discord
import json


def un_lister(market_data, number):
    market_list = market_data.get('market')
    i = 0
    for market_item in market_list:
        listing = market_data['market'][i]
        listing_num = market_data['market'][i]['number']
        i += 1
        if int(listing_num) == number:
            market_list.remove(listing)
            break
    x = 1
    for market_item in market_list:
        if market_item['number']:
            market_item['number'] = f'{x}'
            x += 1
    market_data.update({'market': market_list})
    with open('lists/market.json', 'w', encoding='utf-8') as market_file:
        json.dump(market_data, market_file, indent=1)


async def ex(args, message, bot, invoke):
    if args:
        if str.isdigit(args[0]):
            role = discord.utils.find(lambda x: x.id == xxxxxxxxxxxxxxxxxx, message.guild.roles)
            if role:
                with open('lists/market.json', encoding='utf-8') as file:
                    market_data = json.load(file)
                number = int(args[0])
                un_lister(market_data, number)
                response = discord.Embed(title=f'✅ Your item has been unlisted', color=0x77B255)
            else:
                response = discord.Embed(title="⛔ Access denied: Banker required", color=0xBE1931)
        else:
            response = discord.Embed(title='❗ Input must be a number', color=0xBE1931)
    else:
        response = discord.Embed(title='❗ No input', color=0xBE1931)
    await message.channel.send(embed=response)
