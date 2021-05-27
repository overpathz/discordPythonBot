import discord

from app.configs.bot_setting import bot
from app.entities.DBUser import DSUser
from app.configs.lists import *
from app.logic.service_methods import *

@bot.command(pass_context=True)
async def hello(message):
    await message.channel.send(f'hello, {  str(message.author).split("#")[0]  }')


@bot.command()
async def java(ctx):
    emb = discord.Embed(title="JavaTop", colour=discord.Colour.dark_green())
    emb.set_image(url="https://lh3.googleusercontent.com/-zz3Jhmhsbcw/YKNjp02JAnI/AAAAAAAABuU/hpyvBOVPzPcFVu61iJaqUkCNFx8EdN_TQCLcBGAsYHQ/image.png")
    await ctx.send(embed=emb)


@bot.command(pass_context=True)
async def flood(message, body, times):
    time_user = DSUser(str(message.author))

    if int(times) > 20:
        await message.channel.send('Ти не приахуел??')
    else:
        if check_is_user_in_list(time_user, ban_list):
            await message.channel.send(f'You got a ban on the "flood" command.')
            return
        if check_is_user_in_list(time_user, cooldown_list):
            await message.channel.send(f'You got a 10 second cooldown.')
            return

        else:
            for _ in range(int(times)):
                await message.channel.send(str(body))
                await asyncio.sleep(0.5)

            is_in_lst = False
            if check_is_user_in_list(time_user, cooldown_list):
                is_in_lst = True

            if not is_in_lst:
                if check_is_admin(time_user):
                    pass
                else:
                    cooldown_list.append(DSUser(str(message.author)))
                    await minus_cooldown()
