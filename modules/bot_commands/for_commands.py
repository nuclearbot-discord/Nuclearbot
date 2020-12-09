import json
import random
from random import Random
from asyncio import sleep
from datetime import date
from datetime import datetime
import asyncio 
import discord
from discord.ext import commands
from requests import get

from modules.config import settings
from modules.style import *

from modules.bot_funcs.collector import *

__ver__ = '0.1'

commands_dict = {}
egg_dict = {}
def add_command (name): 
    def adder (func):
        commands_dict [name] = func

        return func
    return adder
statusnik=[]
def version(vers):
    statusnik.append(vers)
def add_egg (name): 
    def adder_ (func):
        egg_dict [name] = func

        return func
    return adder_

print (f': {__name__}.py {__ver__}')
