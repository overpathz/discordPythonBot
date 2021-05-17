from app.configs.bot_setting import bot
from app.entities.DBUser import DSUser
from app.configs.lists import *
from app.logic.service_methods import *


@bot.command(pass_context=True)
async def text():
    pass


@bot.command(pass_context=True)
async def hello(message):
    await message.channel.send(f'hello, {  str(message.author).split("#")[0]  }')


@bot.command(pass_context=True)
async def flood(message, body, times):
    time_user = DSUser(str(message.author))

    if int(times) > 20:
        await message.channel.send('Ти не приахуел??')
    else:
        if checkInLst(time_user, ban_list):
            await message.channel.send(f'Ти отримав бан на команду "flood".')
            return

        for i in black_list:
            if time_user.name == i.name:
                print_lock = i.lockdown
                await message.channel.send(f'Кулдаун на 10 сек). {print_lock} залишилося.')
                return
        else:
            for _ in range(int(times)):
                await message.channel.send(str(body))
                await asyncio.sleep(0.5)

            is_in_lst = False
            for i in black_list:
                if time_user.name == i.name:
                    is_in_lst = True

            if not is_in_lst:
                black_list.append(DSUser(str(message.author)))
                await minus_cooldown()
