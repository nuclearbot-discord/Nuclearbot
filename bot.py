from random import choice as choose

import discord
from discord.ext import commands
from requests import get

from config import settings
from txts import *

global commands_dict

ver = '0.1.1'
commands_dict = {}             #
rand = [True, True, True, True, True, True, True, False, False, False]

bot = commands.Bot (command_prefix = settings ['prefix'])

def add_command (name): #Не трогать: убью
    def adder (func):
        commands_dict [name] = func

        return func
    return adder

def chat_bot (msg):
    req = get('https://mol-programmist.ru/bot/index.php?str=%27' + msg + '%27&id=100000%27')
    req.encoding = 'utf-8'

    return req.text
        
@bot.event #Не трогать: убью
async def on_ready ():
    print (ver)

    game = discord.Game (txt_status_before + ver + txt_status_after)
    await bot.change_presence (
        status = discord.Status.idle, 
        activity = game
    )

@add_command ('help') #Пример как делать комманды
async def help (message):
    await message.channel.send (embed = help_embed)
 
@add_command ('info')
async def info (message):
    await message.channel.send (embed = info_embed)

@add_command ('log')
async def log (message):
    await message.channel.send (commands_dict)

@add_command ('chat')
async def chat (message):
    msg = message.content.split (settings ['prefix'] + 'chat ') [1]
    txt = chat_bot (msq)
    await message.channel.send (txt)



@bot.event #Не трогать: убью
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
        if choose (rand):
            await message.channel.send (chat_bot (message.content))

bot.run (settings ['token'])
