from modules.bot_commands.for_commands import *
@add_command ('furry')
async def furry (message, bot):
    arg = get_next(message, 'furry')
    if arg == 'yiff':
        if message.channel.is_nsfw():
            response = get('https://api.furry.bot/V2/furry/yiff/straight')
            json_data = json.loads(response.text)
            fs = json_data['images']

            embed = discord.Embed(color=0xff9900, title='йифф')
            embed.set_image(url=str(fs[0]['url']))

            await message.channel.send(embed=embed)
        else:
            await message.channel.send("не nsfw!")

    elif arg == 'lick':
        if message.channel.is_nsfw():
            response = get('https://api.furry.bot/V2/furry/lick/')
            json_data = json.loads(response.text)
            fs = json_data['images']

            embed = discord.Embed(color=0xff9900, title='LICK')
            embed.set_image(url=str(fs[0]['url']))

            await message.channel.send(embed=embed)

        else:
            await message.channel.send("не nsfw!")
    elif arg == "bulge":
        if message.channel.is_nsfw():
            response = get('https://api.furry.bot/V2/furry/bulge/')
            json_data = json.loads(response.text)
            fs = json_data['images']

            embed = discord.Embed(color=0xff9900, title='BULGE')
            embed.set_image(url=str(fs[0]['url']))

            await message.channel.send(embed=embed)

        else:
            await message.channel.send("не nsfw!")
    elif arg == 'propose':
        if message.channel.is_nsfw():
            response = get('https://api.furry.bot/V2/furry/propose/')
            json_data = json.loads(response.text)
            fs = json_data['images']

            embed = discord.Embed(color=0xff9900, title='PROPOSE')
            embed.set_image(url=str(fs[0]['url']))

            await message.channel.send(embed=embed)

        else:
            await message.channel.send("не nsfw!")
    else:
        await message.channel.send('такого параметра нет')

@add_command ('img')
async def cat (msg, bot):
    arg = get_next (msg, 'img')
    data = {'animal': arg}
    try:
        r = get (f'https://some-random-api.ml/img/{arg}')
        dat = json.loads (r.text)

        url = dat ['link']
    
        embed = Embed (name = 'Cat')
        embed.set_image (url = url)

        await msg.channel.send (embed = embed)
    except:
        await msg.channel.send(f"категории {arg} не существует")
@add_command ('kiss')
async def kiss (message, bot):
    args = get_next (message, 'kiss').split (' ')

    response = get ('https://nekos.life/api/v2/img/kiss')
    json_data = json.loads (response.text)
        
    
    embed = discord.Embed (color = 0xff9900, title ="kiss!", description= f'{message.author.mention} kiss {args[0]}. ')
    embed.set_image (url = str(json_data["url"]))
    await message.channel.send(args)
    await message.channel.send (embed = embed)
@add_command ('tickle')
async def tickle (message, bot):
    args = get_next (message, 'tickle').split (' ')

    response = get ('https://nekos.life/api/v2/img/tickle')
    json_data = json.loads (response.text)
        
    
    embed = discord.Embed (color = 0xff9900, title= "tickle!", description= f'{message.author.mention} Защекотал {args[0]}. ')
    embed.set_image (url = str(json_data["url"]))
    await message.channel.send(args)
    await message.channel.send (embed = embed)

@add_command ('nsfw')
async def nsfw (message, bot):
    args = get_next(message, 'nsfw').split(' ')
    if args[0] != "":
        if args[0] == 'boobs':
            if message.channel.is_nsfw():
                response = get('https://nekos.life/api/v2/img/boobs')
                json_data = json.loads(response.text)

                embed = discord.Embed(color=0xff9900, title='boobs')
                embed.set_image(url=str(json_data["url"]))

                await message.channel.send(embed=embed)
            else:
                await message.channel.send("не nsfw!")
        else:
            await message.channel.send('такой категории нет')
    else:
        await message.channel.send("укажи категорию")

__ver__ = '2.1'

add_module (__name__, __ver__)
