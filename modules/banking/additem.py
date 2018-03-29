import discord
import json


def dump_list(number, market_data, item, price, qty):
    market_list = market_data.get('market')
    num = 1
    for listing in market_list:
        num += 1
    data = {"number": number, "item": item, "price": price, "quantity": qty}
    market_list.append(data)
    market_data.update({'market': market_list})
    with open('lists/market.json', 'w', encoding='utf-8') as market_file:
        json.dump(market_data, market_file, indent=1)


async def ex(args, message, bot, invoke):
    role = discord.utils.find(lambda x: x.id == 426514392864260107, message.guild.roles)
    if role:
        if role.id in [y.id for y in message.author.roles]:
            if args:
                if len(args) == 3:
                    all_qry = ' '.join(args)
                    item = ''.join(all_qry.split('; ')[0]).title()
                    price = ''.join(all_qry.split('; ')[1])
                    qty = ''.join(all_qry.split('; ')[2])
                    if 'p' in price.lower():
                        price = price
                    else:
                        price = price + 'p'
                    if 'x' in qty.lower():
                        qty = qty
                    else:
                        qty = qty + 'x'
                    if item and price and qty:
                        with open('lists/market.json', encoding='utf-8') as file:
                            market_data = json.load(file)
                            i = 1
                            for x in market_data['market']:
                                i += 1
                            number = f'{i}'
                        dump_list(number, market_data, item, price, qty)
                        response = discord.Embed(title=f'✅ Listing added', color=0x77B255)
                    else:
                        response = discord.Embed(title='❗ Invalid arguments', color=0xBE1931)
                else:
                    response = discord.Embed(title='❗ Invalid number of inputs', color=0xBE1931)
            else:
                response = discord.Embed(title='❗ No input', color=0xBE1931)
        else:
            response = discord.Embed(title="⛔ Access denied: Banker required", color=0xBE1931)
    else:
        response = discord.Embed(title=f'🔍 I couldn\'t find the Banker role', color=0x696969)
    await message.channel.send(embed=response)
