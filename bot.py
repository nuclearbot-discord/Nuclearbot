from random import Random

import discord
from discord.ext import commands
from requests import get
#from firebase import Firebase

from config import settings
from style import *

configfb = {
  "apiKey": "AIzaSyC3vGWkRWrBNLuz5YlysXZMZXGy0gT56LA",
  "authDomain": "164893195950.firebaseapp.com",
  "databaseURL": "https://avroraacha.firebaseio.com/",
  "storageBucket": "avroraacha.appspot.com" 
} # V config nada pihat


ver = '0.2.1 FB'
commands_dict = {} 
rand = Random ().random

#firebase = Firebase (configfb)
#db = firebase.database ()
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

def get_next (message, command):
    command_all = settings ['prefix'] + command + ' '
    return command_all.join (message.content.split (command_all) [1:])

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
    )
    
    await bot.get_channel (settings ['channel']).send (txt_bot_online)

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

@add_command ('clear')
async def clear (message):
    amount = all_digits (message.content) 
    await message.channel.purge (limit = amount)

@add_command ('say')
async def say (message):
    await message.delete ()
    await message.channel.send (get_next (message, 'say'))
@add_command('dbdb')
async def dbdb (message):
  all_users = db.child("timeout").get()
  for user in all_users.each():
    if user.key()=="781409504435896320":
      a=user.val()
      message.channel.send(a["shans"])
@bot.event
async def on_guild_join (guild):
    data = {"shans": "20"}
    #db.child("timeout").child(guild.id).set(data)
    await bot.get_channel (settings ['channel']).send (guild.id)

@bot.event
async def on_error (a, b):
    await bot.get_channel (settings ['channel']).send (txt_bot_online)
    
@bot.event 
async def on_message (message): 
    if message.author.bot:
        return

    if message.content.lower () == 'help':
        await message.channel.send (
            txt_help_not_command_before + settings ['prefix'] + txt_help_not_command_after
        )

        return

    check = lambda val: message.content.startswith (settings ["prefix"] + val)

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
                                        
        if (rand () * 100) < 20:
            await message.channel.send (chat_bot (message.content, str (message.author.id)))

            return

bot.run (settings ['token'])
