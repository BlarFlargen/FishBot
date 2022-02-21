import os

import discord
import logging
from discord.ext import commands
from dotenv import load_dotenv

# Setting up logging
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

# Loads the bot token and guild token from the .env file
load_dotenv()
token = os.getenv('TOKEN')
guild = os.getenv('GUILD')

description = "FishBot by the Fish himself"

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='>', description=description, intents=intents)

client = discord.Client(activity=discord.Game(name='BOZO'))

for f in os.listdir("./cogs"):
    if f.endswith(".py"):
        bot.load_extension("cogs." + f[:-3])


@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

bot.run(token)
