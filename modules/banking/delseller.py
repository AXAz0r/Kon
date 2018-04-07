import discord
import json


def update_slr(market_data, number: int, seller):
    market_list = market_data.get('market')
    i = number - 1
    listing = market_data['market'][i]['seller']
    for seller_id in listing:
        if int(seller) == seller_id:
            listing.remove(seller_id)
            break
    market_data.update({'market': market_list})
    with open('lists/market.json', 'w', encoding='utf-8') as market_file:
        json.dump(market_data, market_file, indent=1)


async def ex(args, message, bot, invoke):
    role = discord.utils.find(lambda x: x.id == xxxxxxxxxxxxxxxxxx, message.guild.roles)
    if role:
        if role.id in [y.id for y in message.author.roles]:
            if args:
                number, seller = args[0].split(':')
                if str.isdigit(number) and str.isdigit(seller):
                    number = int(number)
                    if number and seller:
                        with open('lists/market.json', encoding='utf-8') as file:
                            market_data = json.load(file)
                        market_list = market_data.get('market')
                        seller = message.author.id
                        y = 0
                        for market_item in market_list:
                            y += 1
                        if number <= y:
                            update_slr(market_data, number, seller)
                            response = discord.Embed(title=f'✅ Seller removed', color=0x77B255)
                        else:
                            response = discord.Embed(title=f'🔍 I couldn\'t find that listing', color=0x696969)
                    else:
                        response = discord.Embed(title='❗ Invalid arguments', color=0xBE1931)
                else:
                    response = discord.Embed(title='❗ Input must be numbers', color=0xBE1931)
            else:
                response = discord.Embed(title='❗ No input', color=0xBE1931)
        else:
            response = discord.Embed(title="⛔ Access denied: Banker required", color=0xBE1931)
    else:
        response = discord.Embed(title=f'🔍 I couldn\'t find the Head Mentor role', color=0x696969)
    await message.channel.send(embed=response)
