from app.configs.bot_setting import *
from app.configs.lists import *
from app.logic.service_methods import *
from app.logic.admin_methods import *
from app.logic.user_methods import *


@bot.event
async def on_ready():
    print(f'Ready to use!')


bot.run(TOKEN)
