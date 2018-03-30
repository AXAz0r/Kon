import discord
import json
from humanfriendly.tables import format_pretty_table as boop


def sorter():
    i = [1, 0]
    with open('lists/market.json') as file:
        market_data = json.load(file)
    market_list = market_data.get('market')
    m_list = []
    for market_item in market_list:
        to_data = list(market_item.values())
        m_list.append(to_data)
    m_sorted = sorted(m_list, key=lambda x: x[1])
    m_list = []
    for market_item in m_sorted:
        market_item[0] = f'{i[0]}'
        m_list.append(market_item)
        i[0] += 1
    for market_item in market_list:
        market_item['number'] = f'{m_list[i[1]][0]}'
        market_item['item'] = f'{m_list[i[1]][1]}'
        market_item['price'] = f'{m_list[i[1]][2]}'
        market_item['quantity'] = f'{m_list[i[1]][3]}'
        i[1] += 1
    m_out = []
    for market_item in market_list:
        to_data = list(market_item.values())
        m_out.append(to_data[:-1])
    market_data.update({'market': market_list})
    with open('lists/market.json', 'w', encoding='utf-8') as market_file:
        json.dump(market_data, market_file, indent=1)
    return m_out


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
    m_list = sorter()
    m_sorted = sorted(m_list, key=lambda x: int(x[0]))
    inv = m_sorted[start_range:end_range]
    if inv:
        output = boop(inv, column_names=headers)
        response = discord.Embed(color=0xC16A4F)
        response.add_field(name=f'📋 Items currently for sale | Page {page_number}',
                           value=f'```hs\n{output}\n```', inline=False)
        response.set_footer(text='Use the buyitem command to purchase something')
    else:
        response = discord.Embed(title='🔍 Just an empty page', color=0x696969)
    await message.channel.send(embed=response)
