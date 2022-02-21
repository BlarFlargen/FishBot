import random
from discord.ext import commands
from flags.red import *


class Redflags(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def redflag(self, ctx):

        user = ctx.message.author
        await ctx.send(f"{user.mention} Your red flag is: " + random.choice(redflags))


def setup(bot):
    bot.add_cog(Redflags(bot))
