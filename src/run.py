from ReisenBot import ReisenBot
from discord.ext import commands
import discord
import settings

token = settings.DISCORD_TOKEN

if __name__ == '__main__':
    bot = ReisenBot(command_prefix=settings.COMMAND_PREFIX)
    bot.run(token)