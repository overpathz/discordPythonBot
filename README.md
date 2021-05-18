# [Python] Discord bot

#### Python bot for personal use on my Discord server

## Features

- own chat ban system
- own permission system

![image](https://lh3.googleusercontent.com/PE3DYSrk8EyPQms6YXrCvVKg25qkFOR770Jyy_B1UnjtNOSMyyV6GBmM92s8lifmIJVpeYtH06bsrzGBF-s9GmiUJgxe7B39vI8M1y-DedfmK7BTXTmAq_cC2JtTUt8JTQ=w1280)

## Set up

You must have Python 3 installed on your PC.

```
git clone 'repo url'
```

After cloning repo:

```
pip install discord
```

###### (Creating a bot account and getting the token: https://discordpy.readthedocs.io/en/stable/discord.html)
To run a bot, you must have the bot token that you received after creating the bot.
Create in your project directory .env file, which will be contain a bot token.

###### After that, you can run the main.py.
###### If the program starts successfully, you will receive a message in the console that the bot is ready for use.

## Development

The project contains 3 .py files (with bot commands)
- admin.py - bot commands for admins, at the beginning of the method it checks whether the user is an admin
- user.py - commands that can be used by default users
- service.py - helpful methods (perform various checks, contain frequently used code blocks, 
and help you better decompose the program)

### Open any of these .py files and start writing new or adding to the current functionality
### Cheers :)
