import discord
import json


def update_qty(market_data, number: int, qty):
    i = number - 1
    market_data['market'][i]['quantity'] = f'{qty}x'
    with open('lists/market.json', 'w', encoding='utf-8') as market_file:
        json.dump(market_data, market_file, indent=1)


async def ex(args, message, bot, invoke):
    role = discord.utils.find(lambda x: x.id == 404736328387919882, message.guild.roles)
    if args:
        if role:
            number, quantity = args[0].split(':')
            if str.isdigit(number) and str.isdigit(quantity):
                number = int(number)
                if number and quantity:
                    with open('lists/market.json', encoding='utf-8') as file:
                        market_data = json.load(file)
                    market_list = market_data.get('market')
                    x = 0
                    for market_item in market_list:
                        x += 1
                    if number <= x:
                        update_qty(market_data, number, quantity)
                        response = discord.Embed(title=f'✅ Quantity updated', color=0x77B255)
                    else:
                        response = discord.Embed(title=f'🔍 I couldn\'t find that listing', color=0x696969)
                else:
                    response = discord.Embed(title='❗ Invalid arguments', color=0xBE1931)
            else:
                response = discord.Embed(title='❗ Input must be numbers', color=0xBE1931)
        else:
            response = discord.Embed(title="⛔ Access denied: Banker required", color=0xBE1931)
    else:
        response = discord.Embed(title='❗ No input', color=0xBE1931)
    await message.channel.send(embed=response)
