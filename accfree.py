import random
import json
from asyncio import sleep
from config import settings
import requests
import discord
from discord.ext import commands


admins = [732571199913328691, 704560097610825828, 609318080300187648]
accs_text = '''
mauriceliedtke@gmx.net:Floh1998
alanjrsmith@gmail.com:Naruto2009!
'''
accss_text='''
D:a
S:r
J:d
'''
accs = accs_text.split ('\n') [:-1]
accss = accs_text.split ('\n') [:-1]

bot = commands.Bot (command_prefix = ',')

@bot.event
async def on_ready ():
    game = discord.Game (',img ааfox FIXED | Отдам аккаунты')
    await bot.change_presence (status = discord.Status.idle, activity = game)

@bot.group (invoke_without_command = True)
async def give (ctx):
    await ctx.send ('Укажите параметры')

@give.command ()
async def minecraft (ctx):
    author_id = ctx.message.author.id

    if author_id in admins:
        acc = random.choice (accs).split (':')

        print (accs)
        
        embed = discord.Embed (
            title = 'Лицензия Minecraft',
            color = discord.Colour(0xff0000),
            description = f'Аккаунт: `{acc [0]}` \nПароль: ||`{acc [1]}`||',
        )

        embed.set_thumbnail (url = 'https://cdn.discordapp.com/attachments/779025471252856852/780774815153520670/1606221592221_scale_1200.jpg')
        embed.set_footer (text = 'Все права защищены', icon_url = 'https://cdn.discordapp.com/attachments/779025471252856852/780774814687297586/1604169731070_i.jpg')

        embed.add_field (name = 'А если лицезия не работает?', value = 'Заменим её!')
        embed.add_field (name = 'А куда это пихать - то?', value = 'В оффициальный [лаунчер](https://www.minecraft.net/ru-ru/download)', inline = True)
        embed.add_field (name = 'А откуда вы их берете?', value = 'Мы не расскажем, но всё законно')
        embed.add_field (name = 'А сколька можно получить лицензий?', value = 'Безлимитно, приглашай людей!', inline = True)

        await ctx.send (embed = embed)

    else:
        await ctx.send ('Вы не обладаете правами администратора')
@give.command ()
async def steam (ctx):
    author_id2 = ctx.message.author.id

    if author_id2 in admins:
        acc2 = random.choice (accss).split (':')

        print (accss)
        
        embed2 = discord.Embed (
            title = 'Лицензия Minecraft',
            color = discord.Colour(0xff0000),
            description = f'Аккаунт: `{acc2 [0]}` \nПароль: ||`{acc2 [1]}`||',
        )

        embed2.set_thumbnail (url = 'https://cdn.discordapp.com/attachments/779025471252856852/780774815153520670/1606221592221_scale_1200.jpg')
        embed2.set_footer (text = 'Все права защищены', icon_url = 'https://cdn.discordapp.com/attachments/779025471252856852/780774814687297586/1604169731070_i.jpg')

        embed2.add_field (name = 'А если лицезия не работает?', value = 'Заменим её!')
        embed2.add_field (name = 'А куда это пихать - то?', value = 'В оффициальный [лаунчер](https://www.minecraft.net/ru-ru/download)', inline = True)
        embed2.add_field (name = 'А откуда вы их берете?', value = 'Мы не расскажем, но всё законно')
        embed2.add_field (name = 'А сколька можно получить лицензий?', value = 'Безлимитно, приглашай людей!', inline = True)

        await ctx.send (embed = embed2)

    else:
        await ctx.send ('Вы не обладаете правами администратора')

@bot.command (pass_contex = True)
async def all (ctx):
    author_id = ctx.message.author.id

    if author_id in admins:
        await ctx.send ('\n'.join (accs))

    else:
        await ctx.send ('ВЫ не облодаете правами администратора')

@bot.group (invoke_without_command = True)
async def img (ctx):
    await ctx.send ('Укажите параметры')

@img.command ()
async def fox (ctx):
    response = requests.get ('https://some-random-api.ml/img/fox')
    json_data = json.loads (response.text)

    embed = discord.Embed (color = 0xff9900, title = 'лиса')
    embed.set_image (url = json_data ['link'])
    
    await ctx.send (embed = embed)

@img.command ()
async def cat (ctx):
    response = requests.get ('https://some-random-api.ml/img/cat')
    json_data = json.loads (response.text)

    embed = discord.Embed (color = 0xff9900, title = 'котяра')
    embed.set_image (url = json_data['link']) 
    
    await ctx.send (embded=embded)

@img.command ()
async def dog (ctx):
    response = requests.get ('https://some-random-api.ml/img/dog')
    json_data = json.loads (response.text)

    embed = discord.Embed (color = 0xff9900, title = 'песель')
    embed.set_image (url = json_data ['link'])
    
    await ctx.send (embed = embed)

bot.run (settings ['token'])


