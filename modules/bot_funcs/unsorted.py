from requests import get

from modules.config import settings

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

__all__ = ['chat_bot', 'get_next', 'all_digits']
__ver__ = '0.2'

print (f': {__name__}.py {__ver__}')
