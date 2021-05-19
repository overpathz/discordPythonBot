from discord.ext import commands

from app.configs.bot_setting import bot
from app.entities.DBUser import DSUser
from app.configs.lists import *
from app.logic.service_methods import *


@bot.command(pass_context=True)
@commands.has_permissions(ban_members=True)
async def ban(message, user):
    temp_user = DSUser(str(message.author))
    banned_user = DSUser(str(user))

    if check_is_in_ban(banned_user):
        await message.channel.send('The user is already in the ban.')
    else:
        if check_is_user_in_list(temp_user, admins):
            ban_list.append(banned_user)
        else:
            await message.channel.send("You're not an admin!")


@bot.command(pass_context=True)
async def unban():
    pass


@bot.command(pass_context=True)
async def banned_users(message):
    await message.channel.send(ban_list)