import random

from discord.ext import commands
from flags.quotes import *


class Quotes(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def quote(self, ctx):
        await ctx.send(random.choice(quotes))


def setup(bot):
    bot.add_cog(Quotes(bot))
