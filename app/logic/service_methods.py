import asyncio

from app.configs.bot_setting import bot
from app.entities.DBUser import DSUser
from app.configs.lists import *

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