#chat bot module



#-------------------------imports----------------------------#
from modules.bot_commands.for_commands import *
#-------------------------imports----------------------------#


#-------------------------code----------------------------#
@add_command ('chat')
async def chat (message, bot):
    msg = get_next (message, 'chat')
    txt = chat_bot (msg, str (message.author.id))

    try:
        await message.channel.send (txt)

    except discord.errors.HTTPException:
        pass
#-------------------------code----------------------------#
