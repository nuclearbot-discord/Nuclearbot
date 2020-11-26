from random import Random

import discord
from discord.ext import commands
from requests import get

from config import settings
from txts import *

global commands_dict

ver = '0.1.8'
commands_dict = {} 
rand = Random ()

bot = commands.Bot (command_prefix = settings ['prefix'])

def add_command (name): 
    def adder (func):
        commands_dict [name] = func

        return func
    return adder

def chat_bot (msg, id_):
    req = get('https://mol-programmist.ru/bot/index.php?str=%27' + msg + '%27&id=' + id_ [-5:] + '%27')
    req.encoding = 'utf-8'

    return req.text

def all_digits (msg):
    int_str = ''

    for char in msg:
        if char.isdigit ():
            int_str += char

    return int (int_str)
        
@bot.event 
async def on_ready ():
    print (ver)

    game = discord.Game (txt_status_before + ver + txt_status_after)
    await bot.change_presence (
        status = discord.Status.idle, 
        activity = game
    Id = 781550030976450601
    Channel().get_channel_by_id (id).send ('djjsjfj')
    )


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
    msg = ''.join (message.content.split (settings ['prefix'] + 'chat ') [1:])
    txt = chat_bot (msg, str (message.author.id))
    await message.channel.send (txt)

@add_command ('clear')
async def clear (message):
    amount = all_digits (message.content) 
    await message.channel.purge (limit = amount)

@add_command ('say')
async def say (message):
    await message.channel.send (''.join (message.content.split (settings ['prefix'] + 'say ') [1:]))
    await message.delete ()

@bot.event 
async def on_message (message):
    if message.author.bot:
        return

    if message.content == 'help':
        await message.channel.send (
            txt_help_not_command_before + settings ['prefix'] + txt_help_not_command_after
        )

    check = lambda val: message.content.startswith (settings ["prefix"] + val)

    if check (''):
        for command_name in commands_dict:
            if check (command_name):
                await commands_dict [command_name] (message)

                break

        else:
            await message.channel.send (txt_no_command)

    else:
        msg_part_ment = message.content.split (f'<@!{settings ["id"]}>')
        
        if len (msg_part_ment) - 1:
            await message.channel.send (chat_bot (''.join (msg_part_ment), str (message.author.id)))
            return
            
        if choose ((rand () * 100) < 20):
            await message.channel.send (chat_bot (message.content, str (message.author.id)))

bot.run (settings ['token'])
