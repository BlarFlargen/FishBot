from discord.ext import commands


class Clear(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='clear')
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount: int):
        authors = {}
        async for message in ctx.channel.history(limit=amount + 1):
            if message.author not in authors:
                authors[message.author] = 1
            else:
                authors[message.author] += 1
            await message.delete()

        msg = "\n".join([f"Cleared {amount} messages."])
        ### msg = "\n".join([f"{author}:{amount}" for author, amount in authors.items()])
        await ctx.channel.send(msg)


def setup(bot):
    bot.add_cog(Clear(bot))
