import discord
from discord.utils import get
from discord.ext import commands


class Bozos(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def bozo(self, ctx, user: discord.Member):
        member = ctx.message.author
        role = get(user.guild.roles, name="BOZO THE CLOWN")
        if role in user.roles:
            await ctx.send(f"{member.mention} They are already BOZO'D.")
        else:
            await user.add_roles(role)
            await ctx.send(f"{user.mention} just got BOZO'D by {member.mention}" + "!!!!!")
            await ctx.send(f"https://cdn.vox-cdn.com/thumbor/Z2b-41HMCuVhqtEAkgor1w5iy-E=/1400x1050/filters:format(jpeg)/cdn.vox-cdn.com/uploads/chorus_asset/file/10483479/bozo_RIP_getty_ringer.jpg")

    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def unbozo(self, ctx, user: discord.Member):
        member = ctx.message.author
        role = get(user.guild.roles, name="BOZO THE CLOWN")
        if role in user.roles:
            await user.remove_roles(role)
            await ctx.send(f"{user.mention} was UNBOZO'D by {member.mention}" + ". Don't do it again.")
        else:
            await ctx.send(f"{member.mention} They are not BOZO'D.")


def setup(bot):
    bot.add_cog(Bozos(bot))
