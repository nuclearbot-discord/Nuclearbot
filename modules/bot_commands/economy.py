from modules.bot_commands.for_commands import *

@add_command ('setcoins')
async def setcoins (message, bot):
     if True:
         args = get_next (message, 'setcoins').split (' ')
         await message.channel.send(args)
         await message.channel.send(args[0])
         id = all_digits (args[0])
         await message.channel.send(id)
         addcoint(id, args[1])
    
@add_command('setchance')
async def set_chance(message, bot):
    if message.author.guild_permissions.administrator:
        chance = str (all_digits (get_next (message, 'setchance')))

        db_setchance (chance, message.guild.id) 
        
        await message.channel.send (
            txt_shance_now_before + str (chance) + txt_shance_now_after
        )
    else:
        if adm_give(message.author.id):
            chance = str (all_digits (get_next (message, 'setchance')))

            db_setchance (chance, message.guild.id) 
        
            await message.channel.send (
                txt_shance_now_before + str (chance) + txt_shance_now_after
            )
        else:
            await message.channel.send ("ты не админ!")


    
@add_command('profile')
async def profile (message, bot):
    if dbusrget(message.author.id):
        spcs=usrgetc(message.author.id)
    else:
        onusr(message.author.id)
        spcs=usrgetc(message.author.id)
    await message.channel.send(f'у {message.author.mention}:\n {spcs["coins"]} монет\n админка:{spcs["adm"]}.')

__ver__ = '2.2'

print (f': {__name__}.py {__ver__}')
