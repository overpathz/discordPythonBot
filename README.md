# [Python] Discord bot

#### Python bot for personal use on my Discord server

## Features

- own chat ban system
- own permission system

![image](https://lh6.googleusercontent.com/zdwEB-zd18bWNDFHCzqLLciT4ylBntDYrkP-BeMRFs6s0Vq80p5wdDfgvyKaYJ7TfSfg-BnIBxAvDbrsFnzDJpS1MkEt9SF_J_vyRFMH7p-jbKbP9xVbKUplgcypxIxvBA=w1280)

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

The project contains 3 .py files
- admin.py - bot commands for admins, at the beginning of the method it checks whether the user is an admin
- user.py - commands that can be used by default users
- service.py - helpful methods( perform various checks, contain frequently used code blocks, 
- and help you better decompose the program )

### Open any of these .py files and start writing new or adding to the current functionality
### Cheers :)
