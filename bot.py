from functools import wraps

import discord
from discord.ext import commands

from config import settings

global commands_dict

ver = '0.0.6'
commands_dict = {}

bot = commands.Bot (command_prefix = settings ['prefix'])

def add_command (name): #Не трогать: убью
    def adder (func):
        commands_dict [name] = func

        return func
    return adder
        
@bot.event #Не трогать: убью
async def on_ready ():
    print (ver)

    game = discord.Game (f'Версия: {ver}')
    await bot.change_presence (
        status = discord.Status.idle, 
        activity = game
    )

@add_command ('help') #Пример как делать комманды
async def help (message):
    await message.channel.send ('HELP TXT')
 


@bot.event #Не трогать: убью
async def on_message (message):
    if message.author.bot:
        return

    if message.content == 'help':
        await message.channel.send (f'{settings ["prefix"]}help')

    check = lambda val: message.content.startswith (settings ["prefix"] + val)

    if check (''):
        for command_name in commands_dict:
            if check (command_name):
                await commands_dict [command_name] (message)

                break

        else:
            await message.channel.send ('Net takoy Commandy')

bot.run (settings ['token'])
