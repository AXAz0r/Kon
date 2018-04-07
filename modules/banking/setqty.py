import discord
import json


def update_qty(market_data, number: int, qty, seller):
    i = number - 1
    current = market_data['market'][i]['quantity']
    if qty > current:
        market_data['market'][i]['seller'].append(seller)
    market_data['market'][i]['quantity'] = f'{qty}x'
    with open('lists/market.json', 'w', encoding='utf-8') as market_file:
        json.dump(market_data, market_file, indent=1)


async def ex(args, message, bot, invoke):
    role = discord.utils.find(lambda x: x.id == xxxxxxxxxxxxxxxxxx, message.guild.roles)
    if role:
        if role.id in [y.id for y in message.author.roles]:
            if args:
                number, quantity = args[0].split(':')
                if str.isdigit(number) and str.isdigit(quantity):
                    number = int(number)
                    if number and quantity:
                        with open('lists/market.json', encoding='utf-8') as file:
                            market_data = json.load(file)
                        market_list = market_data.get('market')
                        seller = message.author.id
                        y = 0
                        for market_item in market_list:
                            y += 1
                        if number <= y:
                            update_qty(market_data, number, quantity, seller)
                            response = discord.Embed(title=f'✅ Quantity updated', color=0x77B255)
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
