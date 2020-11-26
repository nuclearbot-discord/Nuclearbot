import discord
from discord.ext import commands

from config import settings


ver = '0.0.1'

bot = commands.Bot (command_prefix = settings ['prefix'])


@bot.event
async def on_ready ():
    print (ver)

    activity = discord.Activity (
        name = 'за тобой',
        type = discord.ActivityType.watching
    )
    await bot.change_presence (activity = activity)

bot.run (settings ['token'])
