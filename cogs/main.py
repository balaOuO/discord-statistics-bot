import discord
from discord.ext import commands
from discord import app_commands

# 定義名為 Main 的 Cog
class Main(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    # 前綴指令
    # @commands.command()
    # async def Hello(self, ctx: commands.Context):
    #     await ctx.send("Hi~")

    # 關鍵字觸發
    # @commands.Cog.listener()
    # async def on_message(self, message: discord.Message):
    #     if message.author == self.bot.user:
    #         return
    #     if "嗚" in message.content:
    #         await message.channel.send("嗚你媽")
    #     if "嗨" in message.content:
    #         await message.channel.send("我絕對不會回嗨老虎的๛ก(ｰ̀ωｰ́ก) ")

    # name指令顯示名稱，description指令顯示敘述
    # name的名稱，中、英文皆可，但不能使用大寫英文
    # @app_commands.command(name = "咩咩咩咩", description = "聊天統計使用說明")
    # async def hello(self, interaction: discord.Interaction):
    #     await interaction.response.send_message("閉嘴")

# Cog 載入 Bot 中
async def setup(bot: commands.Bot):
    await bot.add_cog(Main(bot))