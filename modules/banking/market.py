import discord
import json
from humanfriendly.tables import format_pretty_table as boop


def sorter():
    with open('lists/market.json') as file:
        market_data = json.load(file)
    market_list = market_data.get('market')
    data = market_data['market']
    a = 0
    to_list = []
    for item in data:
        to_data = list(data[a].values())
        to_list.append(to_data)
        a += 1
    b = 1
    to_sorted = sorted(to_list, key=lambda x: x[1])
    sorted_list = []
    for market_item in to_sorted:
        market_item[0] = f'{b}'
        sorted_list.append(market_item)
        b += 1
    c = 0
    for market_item in market_list:
        if market_item['number']:
            market_item['number'] = f'{sorted_list[c][0]}'
        if market_item['item']:
            market_item['item'] = f'{sorted_list[c][1]}'
        if market_item['price']:
            market_item['price'] = f'{sorted_list[c][2]}'
        if market_item['quantity']:
            market_item['quantity'] = f'{sorted_list[c][3]}'
        c += 1
    d = 0
    output_list = []
    for item in data:
        to_data = list(data[d].values())
        output_list.append(to_data)
        d += 1
    market_data.update({'market': market_list})
    with open('lists/market.json', 'w', encoding='utf-8') as market_file:
        json.dump(market_data, market_file, indent=1)
    return output_list


async def ex(args, message, bot, invoke):
    page_number = 1
    if args:
        try:
            page_number = abs(int(args[0]))
            if page_number == 0:
                page_number = 1
        except TypeError:
            page_number = 1
        except ValueError:
            page_number = 1
    start_range = (page_number - 1) * 10
    end_range = page_number * 10
    headers = ['Num', 'Item', 'Price', 'Qty']
    item_list = sorter()
    to_sorted = sorted(item_list, key=lambda x: int(x[0]))
    inv = to_sorted[start_range:end_range]
    if inv:
        output = boop(inv, column_names=headers)
        response = discord.Embed(color=0xC16A4F)
        response.add_field(name=f'📋 Items currently for sale | Page {page_number}',
                           value=f'```hs\n{output}\n```', inline=False)
        response.set_footer(text='Contact a Banker to purchase something | ^bankers')
    else:
        response = discord.Embed(title='🔍 Just an empty page', color=0x696969)
    await message.channel.send(embed=response)
