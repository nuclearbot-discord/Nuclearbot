from modules.bot_commands.for_commands import *
from dpymenus import Page, PaginatedMenu

__ver__ = '0.1'


@add_command('server')

async def server(message, bot):
    guild = message.guild
    bem='<a:no_boost:796375825221550160>'
    if guild.premium_tier == 1:
        bem='1'
    elif guild.premium_tier == 2:
        bem='2'
    elif guild.premium_tier ==3:
        bem='3'

    embed = discord.Embed(title=f"информация о сервере {message.guild.name}", colour=discord.Colour(0xb525e1),
                          timestamp=message.created_at)

    embed.set_thumbnail(url=message.guild.icon_url)
    embed.set_footer(text="nuclearbot",
                     icon_url="https://cdn.discordapp.com/attachments/786873657942081556/786873942953689119/logo.png")

    embed.add_field(name="каналы и категории:",
                    value=f"каналов: {len(message.guild.channels)}\n<:txt_channel:796381251497099356> текстовых каналов: {len(message.guild.text_channels)}\nвойсы: {len(message.guild.voice_channels)}",
                    inline=False)
    embed.add_field(name="участники:",
                    value=f"всего: {guild.member_count}\nлюдей:{sum(not member.bot for member in guild.members)}\nботов:{sum(member.bot for member in guild.members)}",
                    inline=False)
    embed.add_field(name="статусы",
                    value=f"онлайн: {sum(member.status == discord.Status.online for member in guild.members)}\nоффлвйн: {sum(member.status == discord.Status.offline for member in guild.members)}\nне беспокоить: {sum(member.status == discord.Status.dnd for member in guild.members)}\nне активнен: {sum(member.status == discord.Status.idle for member in guild.members)}\n",
                    inline=False)
    embed.add_field(name="остальное:",
                    value=f"ролей:{len(guild.roles)}\nбустов:{guild.premium_subscription_count}\nуровень буста: {guild.premium_tier} {bem}\nвладелец: {guild.owner}\nрегион:{guild.region}\nсервер создан:{str(guild.created_at)[:-7]}\nуровень проверки:{guild.verification_level}\nязык:{guild.preferred_locale}",
                    inline=False)

    await message.channel.send(embed=embed)


@add_command('user')
async def user(message, bot):
    args = None
    args = get_next(message, 'user')
    id = int(all_digits(args))
    user = bot.get_user(id)
    member = message.guild.get_member(id)
    znaki=''

    if args:
        hype = "нет hypesquad! <:hype:795959806615093259> "
        if user.public_flags.hypesquad_bravery:
            hype = 'bravery! <:hypesquad_bravery:795961676444467241>'
        elif user.public_flags.hypesquad_brilliance:
            hype = 'brilliance! <:hypesquad_brilliance:795964552646754324>'
        elif user.public_flags.hypesquad_balance:
            hype = 'balance! <:hypesquad_balance:795965228537348106>'
        global status
        status = 'не знаю'
        if str(member.status) == 'online':
            status = 'онлайн! <:online:796455061151678514>'
        if str(member.status) == 'dnd':
            status = 'не беспокоить! <:dnd:796454991267102720>'
        if str(member.status) == 'idle':
            status = 'не активен! <:idle:796455018974019636>'
        if str(member.status) == 'offline':
            status = 'оффлайн! <:offline:796454958039040060>'
        #if member.profile.premium:
            #znaki=znaki+ '<:nitro:796454828947537920>'
        if member.profile.staff:
            znaki = znaki + '<:staff_blue:796455620046749707>'
        if user.profile.partner:
            znaki = znaki + '<:staff_blue:796455620046749707>'
        await message.channel.send(f'имя:{user} :grinning:\nhypersquad: {hype}\nстатус:{status}\nзначки: {user.profile}')
        print('da')
    else:
        await message.channel.send(message.author.name)






print(f': {__name__}.py {__ver__}')
add_module(__name__, __ver__)
