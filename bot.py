import discord
from discord.ext import commands

TOKEN = 'NzgxNDA0OTE1MTQyNDkyMTcx.X79KCQ.vcdevmaaRYCADgMagz0iAJX7VTo'
bot = commands.Bot(command_prefix='!')


@bot.command(pass_context=True)  # разрешаем передавать агрументы
async def test(ctx, arg):  # создаем асинхронную фунцию бота
    await ctx.send(arg)  # отправляем обратно аргумент


bot.run(TOKEN)
