import json
import random
from random import Random
from asyncio import sleep
from datetime import date

import discord
from discord.ext import commands
from requests import get

from config import settings, __ver__ as config_ver
from style import *
from db import *

reqs = ['sleep', 'Random', 'settings']
__all__ = ['commands_dict', 'egg_dict', 'chat_bot', 'settings', *reqs]
__ver__ = '0.1'

commands_dict = {}
egg_dict = {}
def add_command (name): 
    def adder (func):
        commands_dict [name] = func

        return func
    return adder

def add_egg (name): 
    def adder_ (func):
        egg_dict [name] = func

        return func
    return adder_

def chat_bot (msg, id_):
    req = get('https://mol-programmist.ru/bot/index.php?str=%27' + msg + '%27&id=' + id_ [-5:] + '%27')
    req.encoding = 'utf-8'

    return req.text

def get_next (message, command):
    command_all = settings ['prefix'] + command + ' '
    return command_all.join (message.content.split (command_all) [1:])

def all_digits (msg):
    int_str = ''

    for char in msg:
        if char.isdigit ():
            int_str += char

    return int (int_str)

@add_command ('setcoins')
async def setcoins (message, bot):
     if True:
         args = get_next (message, 'addcoins').split (' ')
         await message.channel.send(args)
         await message.channel.send(args[0])
         id = all_digits (args[0])
         await message.channel.send(id)
         addcoint(id, args[1])
         
@add_command ('help') #Пример как делать комманды
async def help (message, bot):
    await message.channel.send (embed = help_embed)

'''
@add_command('connect')
async def connect (message, bot):
    channel = message.author.voice.channel
    if channel:
        await message.channel.send(channel)
        await 782584272967303209.connect ()
    else:
        await ctx.send('bruh you arent in a vc')
 ''' # Патом как нибудь

@add_command ('info')
async def info (message, bot):
    await message.channel.send (embed = info_embed)
@add_command ('boobs')
async def boobs (message, bot):
    if message.channel.is_nsfw():
        response = get ('https://nekos.life/api/v2/img/boobs')
        json_data = json.loads (response.text)
        
    
        embed = discord.Embed (color = 0xff9900, title = 'boobs')
        embed.set_image (url = str(json_data["url"]))
    
        await message.channel.send (embed = embed)    
    else:
        await message.channel.send("не nsfw!")
@add_command ('log')
async def log (message, bot):
    await message.channel.send (', '.join (list (commands_dict)))
@add_command ('kiss')
async def kiss (message, bot):
    args = get_next (message, 'kiss').split (' ')

    response = get ('https://nekos.life/api/v2/img/kiss')
    json_data = json.loads (response.text)
        
    
    embed = discord.Embed (color = 0xff9900, title = f'{message.author.mention} kiss {args[0]}. ')
    embed.set_image (url = str(json_data["url"]))
    await message.channel.send(args)
    await message.channel.send (embed = embed)    
@add_command ('chat')
async def chat (message, bot):
    msg = get_next (message, 'chat')
    txt = chat_bot (msg, str (message.author.id))

    try:
        await message.channel.send (txt)

    except discord.errors.HTTPException:
        pass
    
@add_command('setchance')
async def set_chance(message, bot):
    if message.author.guild_permissions.administrator:
        chance = str (all_digits (get_next (message, 'setchance')))

        db_setchance (chance, message.guild.id) 
        
        await message.channel.send (
            txt_shance_now_before + str (chance) + txt_shance_now_after
        )
    else:
        if adm_give(message.author.id):
            chance = str (all_digits (get_next (message, 'setchance')))

            db_setchance (chance, message.guild.id) 
        
            await message.channel.send (
                txt_shance_now_before + str (chance) + txt_shance_now_after
            )
        else:
            await message.channel.send ("ты не админ!")

@add_command ('clear')
async def clear (message, bot):
    if message.author.guild_permissions.administrator:
        amount = all_digits (message.content) 
        await message.channel.purge (limit = amount)
    else:
        await message.channel.send("не админ")
        
@add_command ('say')
async def say (message, bot):
    await message.delete ()
    await message.channel.send (get_next (message, 'say'))

@add_command ('minecraft')
async def minecraft (message, bot):
    if adm_give (message.author.id):
        acc = dbmcget ()
        
        await message.author.send (embed = embed_account_minecraft (acc [0], acc [1]))
        await message.channel.send (txt_account_sended)

    else:    
        await message.channel.send (txt_havent_perms)
@add_command ('yiff')
async def yiff (message, bot):
    if message.channel.is_nsfw():
        response = get ('https://api.furry.bot/V2/furry/yiff/gay')
        json_data = json.loads (response.text)
        fs=json_data['images']
    
        embed = discord.Embed (color = 0xff9900, title = 'йифф')
        embed.set_image (url = str(fs[0]['url']))
    
        await message.channel.send (embed = embed)    
    else:
        await message.channel.send("не nsfw!")
@add_command ('addminecraft')
async def add_minecraft_ds_command (message, bot):
    args = get_next (message, 'addminecraft').split (' ')

    if adm_give (message.author.id): #ToDo: роверка пользователя на адменку
        try:
            add_minecraft (args [0], args [1])
            await message.channel.send (txt_mine_add)

        except:
            await message.channel.send (txt_mine_not_add)

    else:
        await  message.channel.send (txt_havent_perms)

@add_command ('steam')
async def steam (message, bot):
    author = message.author.id

    if True: # Todo: проверку пользователя
        acc = ['ppap@ppap.ppap', 'ppap']

        await message.channel.send ('Later...')

    else:
        await message.channel.send ('No.')

'''
@add_command ('fox')
async def fox (message, bot):
    response = get ('https://some-random-api.ml/img/fox')
    json_data = json.loads (response.text)

    embed = discord.Embed (color = 0xff9900, title = 'Fox')
    embed.set_image (url = json_data ['link'])
    
    await message.channel.send (embed = embed)
''' # Уже не нужно
    
@add_command('profile')
async def profile (message, bot):
    if dbusrget(message.author.id):
        spcs=usrgetc(message.author.id)
    else:
        onusr(message.author.id)
        spcs=usrgetc(message.author.id)
    await message.channel.send(f'у {message.author.mention}:\n {spcs["coins"]} монет\n админка:{spcs["adm"]}.')
   
    
@add_command ('invite')
async def invite (message, bot):
    await message.channel.send (settings ['link'])

@add_command ('img')
async def cat (msg, bot):
    arg = get_next (msg, 'img')
    data = {'animal': arg}

    r = get (f'https://some-random-api.ml/img/{arg}')
    dat = json.loads (r.text)

    url = dat ['link']
    
    embed = Embed (name = 'Cat')
    embed.set_image (url = url)

    await msg.channel.send (embed = embed)
        
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

print (f': bot_commands.py {__ver__}')

if __name__ == '__main__':
    import main
