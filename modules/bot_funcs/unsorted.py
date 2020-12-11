from requests import get

from modules.bot_funcs.for_funcs import *
from modules.config import settings

def get_next (message, command):
    command_all = settings ['prefix'] + command.lower () + ' '
    return command_all.join (message.lower ().split (command_all) [1:])

def all_digits (msg):
    int_str = ''

    for char in msg:
        if char.isdigit ():
            int_str += char

    return int (int_str)

__all__ = ['get_next', 'all_digits']
__ver__ = '0.2'

add_module (__name__, __ver__)
