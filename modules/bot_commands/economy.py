from modules.bot_commands.for_commands import *
from modules.bot_funcs.db import db_setchannel, conins, coinsget, coinsgett, coninss

__ver__ = '2.2'

@add_command ('setglcoins')
async def setglcoins (message, bot):
     if adm_give(message.author.id):
         args = get_next (message, 'setglcoins').split (' ')
         await message.channel.send(args)
         await message.channel.send(args[0])
         id = all_digits (args[0])
         await message.channel.send(id)
         addcoint(id, args[1])
@add_command ('setcoins')
async def setcoins (message, bot):
     if True:
         args = get_next (message, 'setcoins').split (' ')
         id = all_digits (args[0])
         coninss(id,message.guild.id, args[1])

@add_command('setchance')
async def set_chance(message, bot):
    args = get_next(message, 'setchance').split(' ')
    print(args)
    print(len(args))
    args2 = list(filter(None, args))
    print(args2)
    if len(args)>1:

        if message.author.guild_permissions.administrator:
            chance = args2[1]#str (all_digits (get_next (message, 'setchance')))
            if args2[1].isdigit():

                db_setchance (chance, all_digits(args2[0]))
                await message.channel.send(
                     txt_shance_now_before +' in '+ str(args2[0])+' '+ str(chance) + txt_shance_now_after
                )
            else:
                await message.channel.send("не число!")
        

        else:
            if adm_give(message.author.id):
                chance = args2[1]#str (all_digits (get_next (message, 'setchance')))
                if args2[1].isdigit():

                    db_setchance(chance, all_digits(args2[0]))
                    await message.channel.send(
                        txt_shance_now_before +' in '+ str(args2[0])+' '+ str(chance) + txt_shance_now_after)

                else:
                    await message.channel.send("не число!")

            else:

                await message.channel.send ("ты не админ!")
    else:
        if message.author.guild_permissions.administrator:
            chance = str(all_digits(get_next(message, 'setchance')))
            if chance.isdigit():
                db_setchance(chance, message.guild.id)
            else:
                await message.channel.send("не число!")


            await message.channel.send(
                txt_shance_now_before +'in '+ message.channel.mention +' '+ str(chance) + txt_shance_now_after
            )
        else:
            if adm_give(message.author.id):
                chance = str(all_digits(get_next(message, 'setchance')))
                if chance.isdigit():
                    db_setchance(chance, message.guild.id)
                else:
                    await message.channel.send("не число!")
                await message.channel.send(
                    txt_shance_now_before +'in '+ message.channel.mention +' '+str(chance) + txt_shance_now_after
                )
            else:

                await message.channel.send("ты не админ!")
@add_command ('setjoinchannel')
async def setjoinchannel (message, bot):
    args = get_next(message, 'setjoinchannel').split(' ')
    print(args)
    args2=list(filter(None, args))
    if message.author.guild_permissions.administrator:
        id =   all_digits(args2[0])  # str (all_digits (get_next (message, 'setchance')))
        db_setchannel(message.guild.id,id)
    else:
        if adm_give(message.author.id):
            id = all_digits(args2[0])  # str (all_digits (get_next (message, 'setchance')))
            db_setchannel(message.guild.id, id)
        else:
            await message.channel.send("не админ")


    print("latrer")
@add_command('profile')
async def profile (message, bot):

    #print(coinsget(str(message.guild.id)))
    if coinsgett(str(message.guild.id)):
        print(str(message.guild.id))
        spcs=coinsget(str(message.guild.id))[str(message.author.id)]
    else:
        conins(str(message.author.id), str(message.guild.id))
        spcs=coinsget(str(message.guild.id))[str(message.author.id)]
    await message.channel.send(f'у {message.author.mention}:\n {spcs} монет\n админка:test.')
#print(coinsget('1'))
add_module (__name__, __ver__)
