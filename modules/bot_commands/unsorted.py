from modules.bot_commands.for_commands import *
from modules.bot_funcs.unsorted import all_digits2
import time
import datetime
# at the beginning of the script
startTime = time.time()
__ver__ = '3.2'
global _cd
_cd = commands.CooldownMapping.from_cooldown(1.0, 5.0, commands.BucketType.user)
@add_command ('help') #Пример как делать комманды
async def help (message, bot):
    help_embed = discord.Embed(title="Support server", url="https://discord.gg/UVCAQ5uJRc",
                               colour=discord.Colour(0x624c5c),timestamp=message.created_at)
    help_embed.set_author(name=message.author, icon_url=message.author.avatar_url)
    help_embed.set_footer(text="nuclearbot",
                          icon_url="https://cdn.discordapp.com/attachments/786873657942081556/786873942953689119/logo.png")
    help_embed.add_field(name="unsorted (help unsorted)  <:molotok:795677747883933696>",
                         value="!help\n!img\n!minecraft\n!info\n!invite\n!log\n!setchance\n!server"
                               " ", inline=False)
    help_embed.add_field(name="nsfw (help nsfw)", value="!nsfw\n!furry", inline=False)
    help_embed.add_field(name="economy (help economy)", value="!addcoins\n!profile", inline=False)
    help_embed.add_field(name="emotions (help emotions)", value="!tickle\n!kiss", inline=False)
    await message.channel.send (embed = help_embed)

@add_command ('say')
async def say (message, bot):
    await message.delete ()
    await message.channel.send (get_next (message, 'say'))
    
@add_command ('chat')
async def chat (message, bot):
    msg = get_next (message, 'chat')
    txt = chat_bot (msg, message.author.id)

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
            try:
                print(arg)
                print(all_digits2(arg))
                mem=message.guild.get_member(int(all_digits2(arg)))
                await message.channel.send(f"участник {arg} забанен!")
                await mem.ban()
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
@add_command('server')
async def server(message, bot):
    guild=message.guild
    embed = discord.Embed(title=f"информация о сервере {message.guild.name}", colour=discord.Colour(0xb525e1),
                          timestamp=message.created_at)

    embed.set_thumbnail(url=message.guild.icon_url)
    embed.set_footer(text="nuclearbot",
                     icon_url="https://cdn.discordapp.com/attachments/786873657942081556/786873942953689119/logo.png")


    embed.add_field(name="каналы и категории:", value=f"каналов: {len(message.guild.channels)}\nкатегорий: {len(message.guild.categories)}\nтекстовых каналов: {len(message.guild.text_channels)}\nвойсы: {len(message.guild.voice_channels)}", inline=False)
    embed.add_field(name="участники:", value=f"всего: {guild.member_count}\nлюдей:{sum(not member.bot for member in guild.members)}\nботов:{sum(member.bot for member in guild.members)}", inline=False)
    embed.add_field(name="статусы", value=f"онлайн:{sum(member.status==discord.Status.online for member in guild.members)}\nоффлвйн:{sum(member.status==discord.Status.offline for member in guild.members)}", inline=False)
    embed.add_field(name="остальное:",
                    value=f"ролей:{len(guild.roles)}\nбустов:{guild.premium_subscription_count}\nуровень буста:{guild.premium_tier}\nвладелец:{guild.owner.name}\nрегион:{guild.region}\nсервер создан:{str(guild.created_at)[:-7]}\nуровень проверки:{guild.verification_level}\nязык:{guild.preferred_locale}", inline=False)

    await message.channel.send(embed=embed)
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
@add_command('play')
async def play(message, bot):
    #ctx= bot.get_context (message)
    url = 'https://www.youtube.com/watch?v=syqgA4954bE'
    #server = msg.guild
    #voice = message.author.voice
    #voice_channel = voice.channel
    player = await play(url, bot)
    player.start()
    await asyncio.sleep(100)
@add_command('connect')
async def connect (message, bot):
    voice = message.author.voice
    voice_channel = voice.channel
    await message.channel.send("я дошел")
    await voice_channel.connect(reconnect=True)
    await message.channel.send("я дошел2")
# Патом как нибудь

add_module (__name__, __ver__)
