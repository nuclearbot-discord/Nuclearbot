from modules.bot_commands.for_commands import *

@add_egg ('Пища богов')
async def doshurak (message, bot):
    embed = discord.Embed (color = 0xff9900, title = 'ПИЩА БОГОВ')
    embed.set_image (url = 'https://raw.githubusercontent.com/Misha-python/photos/main/doshrak.png')
    
    await message.channel.send (embed = embed)

@add_egg ('Дрочить?')
async def NNN (message, bot):
    m = date.today ().month

    if m == 11:
        embed = discord.Embed (color = 0xff0000, title = 'Нет, НЕДРОЧАБРЬ')
        embed.set_image (url = 'https://media.discordapp.net/attachments/782584274394021890/784111335838711818/1606330982048_images.jpg')

        await message.channel.send (embed = embed)

    else:
        await message.channel.send ('Давай!')

@add_egg ('Vim')
async def vim (message, bot):
    await message.channel.send ('https://omgubuntu.ru/kak-vyiti-iz-vim-nieskolko-sposobov-zakryt-riedaktor-vim/')

@add_egg ('all')
async def all_eggs (message, bot):
    if adm_give (message.author.id):
        p_eggs = ', '.join ([f'`{x}`' for x in list (egg_dict) if x != 'all'])
        await message.author.send (p_eggs)
        
    else:
        await message.author.send ('No')

@add_egg ('log')
async def logger (msg, bot):
    send = msg.channel.send

    print (msg.content)
    await send (msg.content)
    await send (msg.author.id)
    await send (msg.channel.id)

__ver__ = '0.4'

print (f': {__name__}.py {__ver__}')

