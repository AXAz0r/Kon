import secrets
import aiohttp
import discord
from lxml import html


async def grab_post_list(tags):
    links = []
    for x in range(0, 20):
        resource = f'http://safebooru.org/index.php?page=dapi&s=post&q=index&tags={tags}&pid={x}'
        async with aiohttp.ClientSession() as session:
            async with session.get(resource) as data:
                data = await data.read()
        posts = html.fromstring(data)
        for post in posts:
            if 'file_url' in post.attrib:
                file_url = post.attrib['file_url']
                extension = file_url.split('.')[-1]
                if extension in ['png', 'jpg', 'jpeg', 'gif']:
                    height = int(post.attrib['height'])
                    width = int(post.attrib['width'])
                    if width < 2000 and height < 2000:
                        links.append(post)
    return links


def generate_embed(post, titles, color=0xff6699, icon='https://i.imgur.com/WQbzk9y.png'):
    image_url = post.attrib['file_url']
    image_source = f'http://safebooru.org/index.php?page=post&s=view&id={post.attrib["id"]}'
    if image_url.startswith('//'):
        image_url = 'https:' + image_url
    embed = discord.Embed(color=color)
    embed.set_author(name=secrets.choice(titles), icon_url=icon, url=image_source)
    embed.set_image(url=image_url)
    embed.set_footer(
        text=f'Score: {post.attrib["score"]} | Size: {post.attrib["width"]}x{post.attrib["height"]}')
    return embed


links = []
embed_titles = ['Fluffy tails are supreme!', 'Touch fluffy tail~', '>:3',
                '乀^｀・´^／', '(ミ`ω´ミ)', '◝(´◝ω◜｀)◜']


async def ex(args, message, bot, invoke):
    global links
    if not links:
        filler_message = discord.Embed(color=0xff3300, title='🦊 One moment, filling Kon with foxes...')
        fill_notify = await message.channel.send(embed=filler_message)
        links = await grab_post_list('fox_tail')
        filler_done = discord.Embed(color=0xff3300, title=f'🦊 We added {len(links)} foxes!')
        await fill_notify.edit(embed=filler_done)
    rand_pop = secrets.randbelow(len(links))
    post_choice = links.pop(rand_pop)
    icon = 'https://static.tvtropes.org/pmwiki/pub/images/Holo_Ears_7860.jpg'
    response = generate_embed(post_choice, embed_titles, 0xff3300, icon=icon)
    await message.channel.send(None, embed=response)
