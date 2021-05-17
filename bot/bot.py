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

TOKEN = 'ODQzNDYwMzkwMzQ4NTIxNDcy.YKELsw.CuzF0IP3eG8d4L7L3rOvoh0-hCc'

black_list = []

orys = ['орищин', 'оришка', 'Орищин', 'Оришин']


@bot.command(pass_context=True)
async def flood(message, body, times):
    timeUser = DSUser(str(message.author))

    if int(times) > 20:
        await message.channel.send('Ти не приахуел??')
    else:
        for i in black_list:
            if timeUser.name == i.name:
                print_lock = i.lockdown
                await message.channel.send(f'You have 10 sec cooldown. {print_lock} seconds left')
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


@bot.command()
async def ban(ctx, members: commands.Greedy[discord.Member],
                   delete_days: typing.Optional[int] = 0, *,
                   reason: str):

    for member in members:
        await member.ban(delete_message_days=delete_days, reason=reason)

# --------------------
#   service methods
# --------------------


async def minus_cooldown():
    for i in black_list:
        while i.lockdown != 0:
            i.minusTime()
            await asyncio.sleep(1)
        black_list.remove(i)


bot.run(TOKEN)
