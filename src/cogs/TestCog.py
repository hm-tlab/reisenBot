from discord.ext import commands
import discord
from ReisenBot import ReisenBot

class TestCog(commands.Cog):
    def __init__(self, bot:ReisenBot) -> None:
        self.bot = bot

    @commands.command()
    async def test(self, ctx:commands.Context):
        await ctx.send('loli')

def setup(bot) -> None:
    bot.add_cog(TestCog(bot))
