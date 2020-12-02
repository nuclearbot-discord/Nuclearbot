from discord import Embed

# TextID          = Val
# Simple TXTs
txt_status                  = 'Version {0}, used on {1} guilds'
txt_no_command              = 'Uncorrect command'
txt_help_not_command_before = 'To get help type `'
txt_help_not_command_after  = 'help`.'
txt_bot_online              = 'Bot online! <:online:781567439493660713> | {0}'
txt_shance_now_before       = 'Shance now is '
txt_shance_now_after        = '%'
txt_account_sended          = 'Account sended'
txt_havent_perms            = 'Haven\'t permissions'
txt_mine_add                = 'Account added'
txt_mine_not_add            = 'Account not added'
txt_hi_before               = 'Hi, it\'s me, '
txt_hi_after                = '!'

# Embeds

help_embed = Embed (
    title = 'Help',
    color =  0x45db00
)

info_embed = Embed (
    title = 'Info',
    color = 0x45db00
)

#Embed generators

def embed_account_minecraft (email, pasw):
    embed = Embed (
        title = 'Лицензия Minecraft',
        color = 0xff0000,
        description = f'Аккаунт: `{email}` \nПароль: ||`{pasw}`||',
    )

    embed.set_thumbnail (url = 'https://cdn.discordapp.com/attachments/779025471252856852/780774815153520670/1606221592221_scale_1200.jpg')
    embed.set_footer (text = 'Все права защищены', icon_url = 'https://cdn.discordapp.com/attachments/779025471252856852/780774814687297586/1604169731070_i.jpg')

    embed.add_field (name = 'А если лицезия не работает?', value = 'Заменим её!')
    embed.add_field (name = 'А куда это пихать - то?', value = 'В оффициальный [лаунчер](https://www.minecraft.net/ru-ru/download)', inline = True)
    embed.add_field (name = 'А откуда вы их берете?', value = 'Мы не расскажем, но всё законно')
    embed.add_field (name = 'А сколька можно получить лицензий?', value = 'Безлимитно, приглашай людей!', inline = True)

    return embed
