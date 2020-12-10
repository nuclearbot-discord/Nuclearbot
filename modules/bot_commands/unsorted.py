from modules.bot_commands.for_commands import *

__ver__ = '3.2'

@add_command ('help') #Пример как делать комманды
async def help (message, bot):
    await message.channel.send (embed = help_embed)

@add_command ('say')
async def say (message, bot):
    await message.delete ()
    await message.channel.send (get_next (message, 'say'))
    
@add_command ('chat')
async def chat (message, bot):
    msg = get_next (message, 'chat')
    txt = chat_bot (msg, str (message.author.id))

    try:
        await message.channel.send (txt)

    except discord.errors.HTTPException:
        await message.channel.send ('...')
    
@add_command ('info')
async def info (message, bot):
    await message.channel.send (embed = info_embed)
    
@add_command ('log')
async def log (message, bot):
    await message.channel.send (', '.join (list (commands_dict)))

@add_command ('invite')
async def invite (message, bot):
    await message.channel.send (settings ['link'])

@add_command ('clear')
async def clear (message, bot):
    if message.author.guild_permissions.administrator:
        amount = all_digits (message.content) 
        await message.channel.purge (limit = amount)
    else:
        await message.channel.send("не админ")

@add_command ('steam')
async def steam (message, bot):
    author = message.author.id

    if True: # Todo: проверку пользователя
        acc = ['ppap@ppap.ppap', 'ppap']

        await message.channel.send ('Later...')

    else:
        await message.channel.send ('No.')

@add_command('connect')
async def connect (message, bot):
    voice = message.author.voice
    voice_channel = voice.channel
    await message.channel.send("я дошел")
    await voice_channel.connect()
    await message.channel.send("я дошел2")
# Патом как нибудь

add_module (__name__, __ver__)
