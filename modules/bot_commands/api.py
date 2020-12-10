from modules.bot_commands.for_commands import *

__ver__ = '1.0'

@add_command('minecraft')
async def minecraft (message, bot):
    args = get_next (message, 'minecraft')
    nickarg=args
    
    if stat (nickarg) ["status"] == "ok":
        datamc = stat(nickarg)["data"]
        
        if datamc["online"]=="1":
            onl = "online"
            
        else:
            onl = "offline"
            
        if datamc["uuid"] !="False":
            uuid = "не найдено"
            
        else:
            uuid=datamc["uuid"]
            
        ts = int(datamc["last_play"])
        
        if stat(nickarg)["status"]=="ok":
        # if you encounter a "year is out of range" error the timestamp
        # may be in milliseconds, try `ts /= 1000` in that case
            lps=datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
            await message.channel.send(f'nick: {datamc["name"]}\nвсего играл (часов): {datamc["total_time_play"]}\nонлайн: {onl}\nпоследняя игра: {lps}\nuuid: {uuid}')

    else:
        await message.channel.send(stat(nickarg)['msg'])

@add_command ('joke')
async def joke_command (message, bot):
    await message.channel.send (joke ())# ['content'])

add_module (__name__, __ver__)
