from modules.bot_commands.for_commands import *
import datetime
import time
start_time=time.time()

@add_command ('help') #Пример как делать комманды
async def help (message, bot):
    await message.channel.send (embed = help_embed)

'''
@add_command('connect')
async def connect (message, bot):
    channel = message.author.voice.channel
    if channel:
        await message.channel.send(channel)
        await 782584272967303209.connect ()
    else:
        await ctx.send('bruh you arent in a vc')
 ''' # Патом как нибудь
@add_command('uptime')
async def uptime(message, bot):
    current_time = time.time()
    difference = int(round(current_time - start_time))
    text = str(datetime.timedelta(seconds=difference))
    embed = discord.Embed(colour=ctx.message.author.top_role.colour)
    embed.add_field(name="Uptime", value=text)
    embed.set_footer(text="Sponsored by altcointrain.com - Choo!!! Choo!!!")
    messsage.channel.send(embed=embed)
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
        pass
    
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

@add_command ('minecraft')
async def minecraft (message, bot):
    if adm_give (message.author.id):
        acc = dbmcget ()
        
        await message.author.send (embed = embed_account_minecraft (acc [0], acc [1]))
        await message.channel.send (txt_account_sended)

    else:    
        await message.channel.send (txt_havent_perms)

@add_command ('addminecraft')
async def add_minecraft_ds_command (message, bot):
    args = get_next (message, 'addminecraft').split (' ')

    if adm_give (message.author.id):
        try:
            add_minecraft (args [0], args [1])
            await message.channel.send (txt_mine_add)

        except:
            await message.channel.send (txt_mine_not_add)

    else:
        await  message.channel.send (txt_havent_perms)

@add_command ('steam')
async def steam (message, bot):
    author = message.author.id

    if True: # Todo: проверку пользователя
        acc = ['ppap@ppap.ppap', 'ppap']

        await message.channel.send ('Later...')

    else:
        await message.channel.send ('No.')
