import discord
import json
import arrow


async def ex(args, message, bot, invoke):
    with open('lists/market.json', encoding='utf-8') as file:
        market_data = json.load(file)
    market_list = market_data.get('market')
    for market_item in market_list:
        to_data = list(market_item.values())
        target_id = to_data[-1]

    target = discord.utils.find(lambda x: x.id == target_id, bot.get_all_members())
    if args:
        number = args[0]
        if str.isdigit(number):
            number = int(number)
            if number:
                with open('lists/market.json', encoding='utf-8') as file:
                    market_data = json.load(file)
                market_list = market_data.get('market')
                y = 0
                for market_item in market_list:
                    y += 1
                if number <= y:
                    i = number - 1
                    listing = market_data['market'][i]
                    target = discord.utils.find(lambda x: x.id == int(listing['seller']), bot.get_all_members())
                    tar_response = discord.Embed(color=0xDD2E44, timestamp=arrow.utcnow().datetime)
                    tar_response.add_field(name='🛍 Purchase Request', value=f"Buyer: {message.author.mention}\n"
                                                                             f"Item: {listing['item']}\n"
                                                                             f"Price: {listing['price']}")
                    await target.send(embed=tar_response)
                    response = discord.Embed(color=0x77B255, title='✅ A message has been sent to '
                                                                   'the seller with your request')
                else:
                    response = discord.Embed(title=f'🔍 I couldn\'t find that listing', color=0x696969)
            else:
                response = discord.Embed(title='❗ Invalid arguments', color=0xBE1931)
        else:
            response = discord.Embed(title='❗ Input must be numbers', color=0xBE1931)
    else:
        response = discord.Embed(title='❗ No input', color=0xBE1931)
    await message.channel.send(embed=response)
