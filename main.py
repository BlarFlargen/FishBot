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

# Loads the bot token and guild token from .env file
load_dotenv()
token = os.getenv('TOKEN')
guild = os.getenv('GUILD')

# Description of the bot
description = "FishBot by the Fish himself"

# Sets discord intents
intents = discord.Intents.default()
intents.members = True

# Defines bot variables
bot = commands.Bot(command_prefix='>', description=description, intents=intents)

# Sets the bot activity
client = discord.Client(activity=discord.Game(name='BOZO'))

# Looks for .py files in /cogs directory to load
for f in os.listdir("./cogs"):
    if f.endswith(".py"):
        bot.load_extension("cogs." + f[:-3])


# Prints in console when the bot is ready
@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send(error)
        return
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Missing a required argument")
        await ctx.send(error)
        return
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You do not have the appropriate permissions to use this command.")
        return
    if isinstance(error, commands.BotMissingPermissions):
        await ctx.send("I don't have sufficient permissions.")
        return
    else:
        await ctx.send("Error not defined.")
        await ctx.send(error)
        return


# Bot token
bot.run(token)
