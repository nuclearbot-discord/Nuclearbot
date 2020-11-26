import discord
from discord.ext import commands

from config import settings


ver = '0.0.4'

bot = commands.Bot (command_prefix = settings ['prefix'])


@bot.event
async def on_ready ():
    print (ver)

    game = discord.Game (f'Версия: {ver}')
    await bot.change_presence (
        status = discord.Status.idle, 
        activity = game
    )

@bot.event
async def on_message (message):
    if message.author.bot:
        return

    

bot.run (settings ['token'])
