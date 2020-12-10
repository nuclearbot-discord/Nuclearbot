import json

from requests import get

from modules.bot_funcs.for_funcs import *

__ver__ = '0.0.2'
__all__ = ['chat_bot', 'joke', 'stat', 'anec']

def chat_bot (msg, id_):
    req = get('https://mol-programmist.ru/bot/index.php?str=%27' + msg + '%27&id=' + id_ [-5:] + '%27')
    req.encoding = 'utf-8'

    return req.text

def anec ():
    req = get('http://rzhunemogu.ru/RandJSON.aspx?CType=1')
    return req.text
def joke ():
    req = get('http://rzhunemogu.ru/RandJSON.aspx?CType=1')
    an=anec().split(":")
    an2=an[~0]
    an3=an2[1:-1]
    return an3
def stat (nick):
    req = get('http://rzhunemogu.ru/RandJSON.aspx?CType=1%27')
    return req.text

add_module (__name__, __ver__)
