from discord.ext import commands
import traceback
import discord
import settings

class ReisenBot(commands.Bot):
    def __init__(self, command_prefix:str) -> None:
        super().__init__(command_prefix)

    async def on_ready(self):
        print('started' + self.user.name, self.user.id)
        for cog in settings.INITIAL_EXTENSIONS:
            try:
                self.load_extension(cog)
            except Exception:
                pass
                traceback.print_exc()