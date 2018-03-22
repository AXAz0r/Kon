import discord
import json
from humanfriendly.tables import format_pretty_table as boop


def parser():
    with open('lists/market.json') as file:
        market_data = json.load(file)
    data = market_data['market']
    i = 0
    to_list = []
    for item in data:
        to_data = list(data[i].values())
        to_list.append(to_data)
        i += 1
    return to_list


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
    item_list = parser()
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
