import json
import random
from random import Random
from asyncio import sleep
from datetime import date
import asyncio 
import discord
from discord.ext import commands
from requests import get

from modules.config import settings
from modules.style import *
from modules.db import *

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
    command_all = settings ['prefix'] + command.lower () + ' '
    return command_all.join (message.content.lower ().split (command_all) [1:])

def all_digits (msg):
    int_str = ''

    for char in msg:
        if char.isdigit ():
            int_str += char

    return int (int_str)



print (f': bot_commands.py {__ver__}')
