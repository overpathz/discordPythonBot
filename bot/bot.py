import asyncio
from os import listdir
from random import *
import discord
import os
import time
from discord import File
from discord.ext import commands
import typing
from DSUser import *

bot = commands.Bot(command_prefix="$")
client = discord.Client()

images_path = os.path.join(os.path.dirname(__file__), "../images/")
images = [images_path + c for c in listdir(images_path)]

TOKEN = 'ODQzNDYwMzkwMzQ4NTIxNDcy.YKELsw.n3XLTxVEwnqC0ungeirmuqAn_yY'

black_list = []
ban_list = []
admins = [DSUser(str('overpathz#7180'))]

orys = ['орищин', 'оришка', 'Орищин', 'Оришин']


@bot.command(pass_context=True)
async def flood(message, body, times):
    timeUser = DSUser(str(message.author))

    if int(times) > 20:
        await message.channel.send('Ти не приахуел??')
    else:
        if checkInLst(timeUser, ban_list):
            await message.channel.send(f'Ти отримав бан на команду "flood".')
            return

        for i in black_list:
            if timeUser.name == i.name:
                print_lock = i.lockdown
                await message.channel.send(f'Кулдаун на 10 сек). {print_lock} залишилося.')
                return
        else:
            for _ in range(int(times)):
                await message.channel.send(str(body))
                await asyncio.sleep(0.5)

            isInLst = False
            for i in black_list:
                if timeUser.name == i.name:
                    isInLst = True

            if not isInLst:
                black_list.append(DSUser(str(message.author)))
                await minus_cooldown()


@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@bot.command(pass_context=True)
async def image(ctx):
    await ctx.send(file=File((choice(images))))


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
async def unban(message, user1):
    pass


@bot.command(pass_context=True)
async def text(message, text1):
    if str(text1).lower() == 'орищин, ти тут?':
        await message.channel.send('Тут! Ти розраху дописав хуїла?')

    elif 'диф' in str(text1).lower():
        await message.channel.send('ДИФ РНЯ ТОП!!')

    elif str(text1).lower().split()[0] in orys or str(text1).lower().split()[1] in orys:
        await message.channel.send('нахуй пішов')


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
