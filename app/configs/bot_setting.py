import os
from discord.ext import commands
from dotenv import load_dotenv
import asyncio
from app.entities.DBUser import DSUser

load_dotenv()
TOKEN = os.getenv('TOKEN')

bot = commands.Bot(command_prefix="$")
