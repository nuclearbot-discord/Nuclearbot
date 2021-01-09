import os

from discord import voice_client, VoiceState
from discord.utils import get
from modules.bot_commands.for_commands import *
from modules.bot_funcs.unsorted import all_digits2
# at the beginning of the script
import youtube_dl
startTime = time.time()
__ver__ = '3.2'
global _cd
from discord.voice_client import VoiceClient
_cd = commands.CooldownMapping.from_cooldown(1.0, 5.0, commands.BucketType.user)

@add_command('help')
async def help(message, bot):
    ctx=await bot.get_context(message)
    help_embed = Page(title="Support server", url="https://discord.gg/UVCAQ5uJRc",
                          colour=discord.Colour(0x624c5c), timestamp=message.created_at)
    help_embed.set_author(name=message.author, icon_url=message.author.avatar_url)
    help_embed.set_footer(text="nuclearbot",
                              icon_url="https://cdn.discordapp.com/attachments/786873657942081556/786873942953689119/logo.png")
    help_embed.add_field(name="unsorted (help unsorted)  <:molotok:795677747883933696>",
                        value="!help\n!img\n!minecraft\n!info\n!invite\n!log\n!setchance\n!server"
                                " ", inline=False)
    help_embed2 = Page(title="Support server", url="https://discord.gg/UVCAQ5uJRc",
                      colour=discord.Colour(0x624c5c), timestamp=message.created_at)
    help_embed2.set_author(name=message.author, icon_url=message.author.avatar_url)
    help_embed2.set_footer(text="nuclearbot",
                          icon_url="https://cdn.discordapp.com/attachments/786873657942081556/786873942953689119/logo.png")
    help_embed2.add_field(name="nsfw (help nsfw)", value="!nsfw\n!furry", inline=False)
    help_embed3 = Page(title="Support server", url="https://discord.gg/UVCAQ5uJRc",
                      colour=discord.Colour(0x624c5c), timestamp=message.created_at)
    help_embed3.set_author(name=message.author, icon_url=message.author.avatar_url)
    help_embed3.set_footer(text="nuclearbot",
                          icon_url="https://cdn.discordapp.com/attachments/786873657942081556/786873942953689119/logo.png")
    help_embed3.add_field(name="economy (help economy)", value="!addcoins\n!profile", inline=False)
    help_embed4 = Page(title="Support server", url="https://discord.gg/UVCAQ5uJRc",
                      colour=discord.Colour(0x624c5c), timestamp=message.created_at)
    help_embed4.set_author(name=message.author, icon_url=message.author.avatar_url)
    help_embed4.set_footer(text="nuclearbot",
                          icon_url="https://cdn.discordapp.com/attachments/786873657942081556/786873942953689119/logo.png")
    help_embed4.add_field(name="emotions (help emotions)", value="!tickle\n!kiss", inline=False)
    menu = PaginatedMenu(ctx)
    menu.add_pages([help_embed, help_embed2, help_embed3,help_embed4])

    menu.show_skip_buttons()
    await menu.open()
@add_command ('say')
async def say (message, bot):
    await message.delete ()
    await message.channel.send (get_next (message, 'say'))
    
@add_command ('chat')
async def chat (message, bot):
    msg = get_next (message, 'chat')
    txt = chat_bot (msg, str(message.author.id))

    try:
        await message.channel.send (txt)

    except discord.errors.HTTPException:
        await message.channel.send ('...')

@add_command ('info')
async def info (message, bot):
    await message.channel.send ("lATER")
    
@add_command ('log')
async def log (message, bot):
    await message.channel.send (', '.join (list (commands_dict)))

@add_command ('invite')
async def invite (message, bot):
    await message.channel.send (settings ['link'])
@add_command('ban')
async def ban (message, bot):
    if message.author.guild_permissions.administrator:
        print('bann')
        arg = get_next(message, 'ban')
        if len(arg) > 0:
            print(arg)
            print(all_digits2(arg))


            channel = message.channel
            zapros = message.author
            bms = await channel.send('точно банить?')
            await bms.add_reaction('✅')


            def check(reaction, user):
                return user == zapros and str(reaction.emoji) == '✅'

            try:
                reaction, user = await bot.wait_for('reaction_add', timeout=30.0, check=check)
            except asyncio.TimeoutError:
                await channel.send('бана не будет, реакция не нажата!')
            else:
                try:
                    try:
                        mem = message.guild.get_member(int(all_digits2(arg)))
                        await mem.ban()
                        await message.channel.send(f"участник {mem.name} забанен!")
                    except ValueError:
                        await message.channel.send(f"эээто не человек")
                except discord.errors.Forbidden:
                    await message.channel.send('не хватает разрешений на БАН')

@add_command('uptime')
async def uptime (message, bot):
    sec=int(round(time.time() - startTime))
    upt=(time.gmtime(sec))
    print(upt)

    await message.channel.send(datetime.timedelta(seconds=sec))
@add_command ('clear')
async def clear (message, bot):
    if message.author.guild_permissions.administrator:
        amount = all_digits (message.content) 
        await message.channel.purge (limit = amount)
    else:
        if adm_give(message.author.id):
            amount = all_digits(message.content)
            await message.channel.purge(limit=amount)
            await message.channel.send(f"очищено {amount} сообщений!")
        else:
            await message.channel.send("не админ")
@add_command('math')
async def math (message, bot):
    bucket = _cd.get_bucket(message)
    retry_after = bucket.update_rate_limit()
    if retry_after:
        await message.channel.send('кулдаун! жди '+str(round(retry_after))+' секунд')
    else:

        arg = get_next(message, 'math')
        try:
            await message.channel.send(eval(arg))
        except SyntaxError:
            await message.channel.send(f"проверь твое выражение ({arg}), я не могу его решить!")
        except ZeroDivisionError:
            await message.channel.send(f"выражение {arg} не решаемо, ты делишь на ноль! но в высшей математике яисор стремится к бесконечности!")
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
    await voice_channel.connect(reconnect=True)
    await message.channel.send("я дошел2")
# Патом как нибудь


@add_command('play')
async def play(message, bot):
    url=str(get_next(message, 'play'))
    print(url)
    ctx = await bot.get_context(message)

    global name
    song_there = os.path.isfile("song.mp3")
    try:
        if song_there:
            os.remove("song.mp3")
            print("Removed old song file")
    except PermissionError:
        print("Trying to delete song file, but it's being played")
        await ctx.send("ERROR: Музыка уже играет!")
        return

    #await ctx.send("Ожидайте 5-10 секунд")

    voice = discord.utils.get(bot.voice_clients)#get(bot.voice_clients, ctx.guild)#get(bot.voice_clients, ctx.guild)#get(bot.voice_clients, ctx.guild)

    ydl_opts = {
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
            }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        print("Downloading audio now\n")
        ydl.download([url])

    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            name = file
            print(f"Renamed File: {file}\n")
            os.rename(file, "song.mp3")

    voice.play(discord.FFmpegPCMAudio("song.mp3"), after=lambda e: print("Song done!"))
    voice.source = discord.PCMVolumeTransformer(voice.source)
    voice.source.volume = 20.00

    nname = name.rsplit("-", 2)
    await ctx.send(f"Сейчас играет: {nname[0]}")
    print("playing\n")


add_module (__name__, __ver__)
