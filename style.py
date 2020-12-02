from discord import Embed

# TextID          = Val
# Simple TXTs
txt_status_before           = 'версия: '
txt_status_after            = ' | Working correctly'
txt_no_command              = 'Uncorrect command'
txt_help_not_command_before = 'To get help type `'
txt_help_not_command_after  = 'help`.'
txt_bot_online              = 'Bot online! <:online:781567439493660713>'

# Embeds

help_embed = Embed (
    title = 'Help',
    color =  0x45db00
)

info_embed = Embed (
    title = 'Info',
    color = 0x45db00
)
