from discord import Embed

# TextID          = Val
# Simple TXTs
txt_status_before           = 'Versition: '
txt_status_after            = ' | Working correctly'
txt_no_command              = 'Uncorrect command'
txt_help_not_command_before = 'To get help type `'
txt_help_not_command_after  = 'help`.'

# Embeds

help_embed = Embed (
    title = 'Help',
    color =  0x45db00
)

info_embed = Embed (
    title = 'Info',
    color = 0x45db00
)
