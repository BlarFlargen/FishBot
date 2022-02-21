import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

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
