from modules.bot_commands.for_commands import *

__ver__ = 'X.X'

print (f': {__name__}.py {__ver__}')
await bot.get_channel (settings ['logs']).send (f'file ready: {__name__}.py {__ver__}')
