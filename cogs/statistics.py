import discord
from discord.ext import commands
from discord import app_commands
from datetime import datetime , timezone
from typing import Optional
from view.ChatNumStatistics import ChatNumStatistics

class Statistics(commands.Cog):
    def __init__(self , bot : commands.bot) -> None:
        self.bot = bot

    @app_commands.command(name="聊天統計" , description="統計所有成員聊天數量 未輸入時間則預設為統計本月訊息數量")
    @app_commands.describe(start = "yyyy-mm-dd (ex : 2024-01-01)")
    @app_commands.describe(end = "yyyy-mm-dd (ex : 2024-01-01)") # TODO 加上end的上限
    @app_commands.describe(limit = "單一頻道最大訊息數量限制 (預設30000)")
    async def chat_statistics(
        self , 
        interaction: discord.Interaction ,
        start : Optional[str] = None ,
        end : Optional[str] = None ,
        limit : Optional[int] = 30000
    ):
        stats = ChatNumStatistics(
            interaction=interaction ,
            start=start ,
            end=end ,
            limit=limit
            )
        await stats.main()


# Cog 載入 Bot 中
async def setup(bot: commands.Bot):
    await bot.add_cog(Statistics(bot))