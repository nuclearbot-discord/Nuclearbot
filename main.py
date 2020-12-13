import asyncio
import discord
from discord.ext import commands

from modules.bot_commands.collector import * # Importing ALL
from modules.bot_funcs.db import db_setchannel, db_getchannel, db_getchannelt
from modules.bot_funcs.for_funcs import modules_dict

TOKEN = settings ['token']
ver = '0.4.9 L&M build (Logs &nd Modules) jokes'
__ver__ = '0.3.1'
rand = Random ().random

intents = discord.Intents.default ()
intents.members = True
bot = commands.Bot (command_prefix = settings ['prefix'], intents = intents)

@bot.event
async def on_guild_join (guild):
    onjn (guild.id)
    db_setchannel('', guild.id)
@bot.event
async def on_member_join (member):
    if not dbusrget(member.id):
        onusr(member.id)
    #print(member.guild)
    print(db_getchannelt(member.guild.id))
    if db_getchannelt(member.guild.id):
        print('okay')
        embed = discord.Embed(title="добро пожаловать к нам!", colour=discord.Colour(0x624c5c))
        embed.set_author(name=member, icon_url=member.avatar_url)
        embed.set_footer(text="nuclearbot | " + str(datetime.now().strftime("%d.%m.%Y %H:%M:%S")),
                              icon_url="https://cdn.discordapp.com/attachments/786873657942081556/786873942953689119/logo.png")
        embed.set_thumbnail(url=member.avatar_url)
        await bot.get_channel(db_getchannel(member.guild.id)) \
            .send(embed=embed)

    else:
        print('okay2')
        global isis
        isis = True
        for channel in member.guild.channels:
            print(channel.type)
            if isis:
                type=channel.type
                if str(type).lower() == 'text':
                    db_setchannel(member.guild.id,channel.id)
                    print('finded')
                    print('lololol')
                    isis=False
                else:
                    print(channel.type)
        embed = discord.Embed(title="добро пожаловать к нам!", colour=discord.Colour(0x624c5c))
        embed.set_author(name=member, icon_url=member.avatar_url)
        embed.set_footer(text="nuclearbot | " + str(datetime.now().strftime("%d.%m.%Y %H:%M:%S")),
                              icon_url="https://cdn.discordapp.com/attachments/786873657942081556/786873942953689119/logo.png")
        embed.set_thumbnail(url=member.avatar_url)
        await bot.get_channel(db_getchannel(member.guild.id)) \
            .send(embed=embed)



    chat_bot (f'Называй меня {member}', str (member.id))

@bot.event
async def on_ready ():
    log_channel = bot.get_channel (settings ['logs'])

    print (f'\n::: {ver}')

    await bot.get_channel (settings ['channel']).send (txt_bot_online.format (ver))
    await log_channel.send (f'{logson}\nпинг: {bot.latency}')
    await log_channel.send ('```' + '\n'.join ([f': {i}\n:: {modules_dict [i]}' for i in modules_dict]) + '```')

    await bot.change_presence (
        status = discord.Status.idle
    )

    #activ_stream = discord.Streaming (name = txt_status.format (ver, str (len (bot.guilds))), url = 'https://m.twitch.tv/buster')
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

    if message.content.lower() == 'help':
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

    chance = db_getchance (message.channel.id)
    if db_getchance(message.channel.id):
        if (rand () * 100) < int(chance):
            try:
                await message.channel.send (chat_bot (message.content, str (message.author.id)))

            except discord.errors.HTTPException:
                pass

            return
    else:
        db_setchance(100, message.channel.id)

add_module (__name__, __ver__)

bot.run (TOKEN)
