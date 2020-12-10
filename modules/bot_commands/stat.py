from modules.bot_commands.for_commands import *

__ver__ = '1.0'

def stat (nick):
    response = get (f'https://minecraft-statistic.net/api/player/info/{nick}/')
    json_data = json.loads (response.text)
    return json_data
def anec (variant):
    response = get (f'ссилка')
    json_data = json.loads (response.text)
    return json_data
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
@add_command('anecdot')
async def anecdot (message, bot):
    await message.channel.send(anec(1)['content']                                       
print (f': {__name__}.py {__ver__}')

