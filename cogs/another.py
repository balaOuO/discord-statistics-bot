from discord.ext import commands

class Another(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot: commands.Bot = bot

async def setup(bot):
    await bot.add_cog(Another(bot))