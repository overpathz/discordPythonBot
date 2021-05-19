import asyncio

from app.configs.bot_setting import bot
from app.entities.DBUser import DSUser
from app.configs.lists import *

# --------------------
#   service methods
# --------------------


# method for minus cooldown chat time for each user in cooldown list
async def minus_cooldown():
    for i in cooldown_list:
        while i.lockdown != 0:
            i.minusTime()
            await asyncio.sleep(1)
        cooldown_list.remove(i)


# returns true if the user is in given list (ban list, admin list, etc)
def check_is_user_in_list(temp_user, lst):
    for i in lst:
        if temp_user.get_name() == i.get_name():
            return True


# returns true if the user is an admin
def check_is_admin(temp_user):
    for i in admins:
        if temp_user.get_name() == i.get_name():
            return True


# returns true if the user is the ban
def check_is_in_ban(temp_user):
    for i in ban_list:
        if temp_user.get_name() == i.get_name():
            return True
