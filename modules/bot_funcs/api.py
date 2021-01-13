import json

from requests import get, post

from modules.bot_funcs.for_funcs import *

__ver__ = '0.0.3'
__all__ = ['chat_bot', 'joke', 'stat']

def chat_bot (msg, id_):

    params={"query":{"ask":"Привет","userid":"654321","key":""}}
    req=post('https://aiproject.ru/api/',
               data={"query":json.dumps({"ask":msg,"userid":id_[:-5],"key":""})},
               )
    req.encoding='utf-8'
    jsonka=json.loads(req.text)
    if jsonka['status'] == 1:
        if jsonka['emotion']=='':
            return jsonka['aiml']
        else:
            return jsonka['aiml']+ ' | эмоция: :'+ jsonka["emotion"]+":"
    else:
        return jsonka['description'] #desk добавлю окда

def joke ():
    req = get('http://rzhunemogu.ru/RandJSON.aspx?CType=1')
    an=req.text.split(":")
    an2=an[~0]
    an3=an2[1:-2]
    return an3
def stat (nick):
    req = get('http://rzhunemogu.ru/RandJSON.aspx?CType=1%27')
    return req.text

add_module (__name__, __ver__)
