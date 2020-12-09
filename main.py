import discord
from discord.ext import commands
import asyncio
from modules.bot_commands.collector import * # Importing ALL

TOKEN = settings ['token']
ver = '0.4.6 logs final test'
rand = Random ().random
intents = discord.Intents.default ()
intents.members = True
bot = commands.Bot (command_prefix = settings ['prefix'], intents = intents)
@bot.event
async def on_guild_join (guild):
    onjn (guild)

@bot.event
async def on_member_join (member):
    if not dbusrget(member.id):
        onusr(member.id)
    await bot.get_channel (settings ['channel']) \
        .send (txt_hi_before + member.mention + txt_hi_after)

    chat_bot (f'Называй меня {member.nick}', str (member.id))

@bot.event 
async def on_ready ():
    print (': main.py ...')
    print (f':: {ver}') 

    await bot.get_channel (settings ['channel']).send (txt_bot_online.format (ver))
    await bot.get_channel (settings ['logs']).send (f'{logson} пинг: {bot.latency}')
    await bot.get_channel (settings ['logs']).send (statusnik)
    await bot.change_presence (
        status = discord.Status.idle
    )

    #activ_stream = discord.Streaming (name = txt_st atus.format (ver, str (len (bot.guilds))), url = 'https://m.twitch.tv/buster')
    actv_0 = discord.Streaming (name = txt_status_0,                                 url = 'https://m.twitch.tv/buster')
    actv_1 = discord.Streaming (name = txt_status_1.format (ver),                    url = 'https://m.twitch.tv/buster')
    actv_2 = discord.Streaming (name = txt_status_2.format (str (len (bot.guilds))), url = 'https://m.twitch.tv/buster')
    
    while True:
        await bot.change_presence (activity = actv_0)
        await sleep (5)
        await bot.change_presence (activity = actv_1)
        await sleep (5)
        await bot.change_presence (activity = actv_2)
        await sleep (5)
        
@bot.event 
async def on_message (message): 
    if message.author.bot:
        return

    if message.content.lower () == 'help':
        await message.channel.send (
            txt_help_not_command_before + settings ['prefix'] + txt_help_not_command_after
        )

        return

    check = lambda val: message.content.lower().startswith (settings ["prefix"] + val)

    if check (''):
        for command_name in commands_dict:
            if check (command_name):
                await commands_dict [command_name] (message, bot)

                break

        else:
            await message.channel.send (txt_no_command)

        return

    else:
        for egg in egg_dict:
            if message.content.startswith (egg):
                await egg_dict [egg] (message, bot)

                return
            
    msg_part_ment = message.content.split (f'<@!{settings ["id"]}>')
        
    if len (msg_part_ment) - 1:
        try:
            await message.channel.send (chat_bot (''.join (msg_part_ment), str (message.author.id)))
        
        except discord.errors.HTTPException:
            pass
        
        return

    if not message.guild:
        try:
            await message.channel.send (chat_bot (message.content, str (message.author.id)))

        except discord.errors.HTTPException:
            pass
        
        return
    
    chance = db_getchance (message.guild.id)
                                           
    if (rand () * 100) < int(chance):
        try:
            await message.channel.send (chat_bot (message.content, str (message.author.id)))

        except discord.errors.HTTPException:
            pass
        
        return                                         
bot.run (TOKEN)
