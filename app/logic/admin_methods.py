from app.configs.bot_setting import bot
from app.entities.DBUser import DSUser
from app.configs.lists import *
from app.logic.service_methods import *


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
async def bl(message):
    await message.channel.send(black_list)