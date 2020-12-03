import json
import random
from random import Random
from asyncio import sleep

import discord
from discord.ext import commands
from requests import get

from config import settings
from style import *
from db import *

TOKEN = settings ['token']
ver = '0.3.0 AA+ build (Activity Animation)'
commands_dict = {} 
rand = Random ().random

intents = discord.Intents.default ()
intents.members = True
bot = commands.Bot (command_prefix = settings ['prefix'], intents = intents)

def add_command (name): 
    def adder (func):
        commands_dict [name] = func

        return func
    return adder

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

@add_command ('help') #Пример как делать комманды
async def help (message):
    await message.channel.send (embed = help_embed)
 
@add_command ('info')
async def info (message):
    await message.channel.send (embed = info_embed)

@add_command ('log')
async def log (message):
    await message.channel.send (', '.join (list (commands_dict)))

@add_command ('chat')
async def chat (message):
    msg = get_next (message, 'chat')
    txt = chat_bot (msg, str (message.author.id))
    await message.channel.send (txt)
    
@add_command('setchance')
async def set_chance(message):
    chance = str (all_digits (get_next (message, 'setchance')))

    db_setchance (chance, message.guild.id) 
        
    await message.channel.send (
        txt_shance_now_before + str (chance) + txt_shance_now_after
    )

@add_command ('clear')
async def clear (message):
    amount = all_digits (message.content) 
    await message.channel.purge (limit = amount)

@add_command ('say')
async def say (message):
    await message.delete ()
    await message.channel.send (get_next (message, 'say'))

@add_command ('minecraft')
async def minecraft (message):
    if adm_give (message.author.id):
        acc = dbmcget ()
        
        await message.author.send (embed = embed_account_minecraft (acc [0], acc [1]))
        await message.channel.send (txt_account_sended)

    else:    
        await message.channel.send (txt_havent_perms)
    
@add_command ('addminecraft')
async def add_minecraft_ds_command (message):
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
async def steam (message):
    author = message.author.id

    if True: # Todo: проверку пользователя
        acc = ['ppap@ppap.ppap', 'ppap']

        await message.channel.send ('Later...')

    else:
        await message.channel.send ('No.')

@add_command ('fox')
async def fox (message):
    response = get ('https://some-random-api.ml/img/fox')
    json_data = json.loads (response.text)

    embed = discord.Embed (color = 0xff9900, title = 'Fox')
    embed.set_image (url = json_data ['link'])
    
    await message.channel.send (embed = embed)

@bot.event
async def on_guild_join (guild):
    onjn (guild)

@bot.event
async def on_member_join (member):
    await member.send ('Hi!')
    await member.send(member.mention)
    await bot.get_channel (settings ['channel']) \
        .send (txt_hi_before + member.mention + txt_hi_after)
    
@bot.event 
async def on_ready ():
    print (ver)

    await bot.get_channel (settings ['channel']).send (txt_bot_online.format (ver))

    await bot.change_presence (
        status = discord.Status.idle
    )

    #activ_stream = discord.Streaming (name = txt_st atus.format (ver, str (len (bot.guilds))), url = 'https://m.twitch.tv/buster')
    actv_0 = discord.Streaming (name = txt_status_0,                                 url = 'https://m.twitch.tv/buster')
    actv_1 = discord.Streaming (name = txt_status_1.format (ver),                    url = 'https://m.twitch.tv/buster')
    actv_2 = discord.Streaming (name = txt_status_2.format (str (len (bot.guilds))), url = 'https://m.twitch.tv/buster')
    
    while True:
        await bot.change_presence (activity = actv_0)
        await sleep (5)
        await bot.change_presence (activity = actv_1)
        await sleep (5)
        await bot.change_presence (activity = actv_2)
        await sleep (5)

@bot.event 
async def on_message (message): 
    if message.author.bot:
        return

    if message.content.lower () == 'help':
        await message.channel.send (
            txt_help_not_command_before + settings ['prefix'] + txt_help_not_command_after
        )

        return

    check = lambda val: message.content.lower().startswith (settings ["prefix"] + val)

    if check (''):
        for command_name in commands_dict:
            if check (command_name):
                await commands_dict [command_name] (message)

                break

        else:
            await message.channel.send (txt_no_command)

        return

    else:
        msg_part_ment = message.content.split (f'<@!{settings ["id"]}>')
        
        if len (msg_part_ment) - 1:
            await message.channel.send (chat_bot (''.join (msg_part_ment), str (message.author.id)))
            return

        chance = db_getchance (message.guild.id)
                                           
        if (rand () * 100) < int(chance):
                                               
            await message.channel.send (chat_bot (message.content, str (message.author.id)))

            return

bot.run (TOKEN)
