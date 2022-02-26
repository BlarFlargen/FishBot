import random

from discord.ext import commands
from flags.red import *


# Defines Redflag cog
class Redflags(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Redflag command. Flags are imported from /flags directory
    # Takes a random red flag and gives it to the message author
    @commands.command()
    async def redflag(self, ctx):
        user = ctx.message.author
        await ctx.send(f"{user.mention}" + "'s " + "red flag: " + random.choice(redflags))


def setup(bot):
    bot.add_cog(Redflags(bot))
