import asyncio
import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from app.entities.DBUser import DSUser

load_dotenv()
TOKEN = os.getenv('TOKEN')

bot = commands.Bot(command_prefix="$")
client = discord.Client()

black_list = []
ban_list = []
admins = [DSUser(str('overpathz#7180'))]


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


@bot.event
async def on_ready():
    print(f'Ready to use!')


@bot.command(pass_context=True)
async def bl(message):
    await message.channel.send(black_list)


@bot.command(pass_context=True)
async def ban(message, user):
    temp_user = DSUser(str(message.author))
    banned_user = DSUser(str(user))

    if checkInLst(temp_user, admins):
        ban_list.append(banned_user)
    else:
        await message.channel.send('Ти не адмін!')


@bot.command(pass_context=True)
async def unban():
    pass


@bot.command(pass_context=True)
async def text():
    pass


@bot.command(pass_context=True)
async def hello(message):
    await message.channel.send(f'hello, {  str(message.author).split("#")[0]  }')


# --------------------
#   service methods
# --------------------


async def minus_cooldown():
    for i in black_list:
        while i.lockdown != 0:
            i.minusTime()
            await asyncio.sleep(1)
        black_list.remove(i)


def checkInLst(temp_user, lst):
    for i in lst:
        if temp_user.get_name() == i.get_name():
            return True


bot.run(TOKEN)
