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
        await message.channel.send('такого параметра нет.\nДоступные параметры: propose, bulge, lick, yiff!')

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
        await msg.channel.send(f"категории {arg} не существует.")
@add_command ('kiss')
async def kiss (message, bot):

    args = get_next (message, 'kiss').split (' ')
    if True:
        response = get ('https://nekos.life/api/v2/img/kiss')
        json_data = json.loads (response.text)
        
    
        embed = discord.Embed (color = 0xff9900, title ="kiss!", description= f'{message.author.mention} kiss {args[0]}. ')
        embed.set_image (url = str(json_data["url"]))
        await message.channel.send(args)
        await message.channel.send (embed = embed)
    else:
        await message.channel.send ('ты че, целуй людей!')
@add_command ('tickle')
async def tickle (message, bot):
    args = get_next(message, 'tickle').split(' ')
    print(args)
    if id>5:
        id = all_digits(args[0])
    else:
        await message.channel.send('человека дай')
        pass
    print(id)
    try:
        print(args)

        member=bot.get_user(id)
        response = get('https://nekos.life/api/v2/img/tickle')
        json_data = json.loads(response.text)

        embed = discord.Embed(color=0xff9900, title="tickle!",
                              description=f'{message.author.mention} Защекотал {args[0]}. ')
        embed.set_image(url=str(json_data["url"]))
        await message.channel.send(args)
        await message.channel.send(embed=embed)
    except:
        await message.channel.send('человека дай')




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
            await message.channel.send('такой категории нет.\nесть: boobs"')
    else:
        await message.channel.send("укажи категорию")
@add_command('comment')
async def comment(message, bot):
    args = get_next(message, 'comment').split(' ')
    if args[0] != "":
        embed=discord.Embed(title="коммент!",
                          colour=discord.Colour(0x624c5c), timestamp=message.created_at)
        stroka=str(",".join(args))
        url=f'https://some-random-api.ml/canvas/youtube-comment?avatar={message.author.avatar_url}&username={message.author.name}&comment={stroka.replace(",", "+")}'
        print(url)
        embed.set_image(url=url)
        await message.channel.send(embed=embed)
__ver__ = '2.1'
@add_command('dice')
async def dice(message, bot):
    request = get()
add_module (__name__, __ver__)
