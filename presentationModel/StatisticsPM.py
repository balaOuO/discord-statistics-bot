from discord.ext import commands
import discord
from typing import Optional

from model.StatisticsModel import StatisticsModel


class StatisticsPM:
    def __init__(self, bot: commands.bot, model: StatisticsModel):
        self.bot = bot
        self.model = model

    async def count_messages(
            self,
            interaction: discord.Interaction,
            start: Optional[str],
            end: Optional[str],
            limit: Optional[int]
    ):
        embed: discord.Embed = self._initialize_embed(interaction)
        try:
            await interaction.response().send_message(embed=embed)
        except Exception as e:
            embed.description = "⚠️there are something wrong⚠️"
            await interaction.edit_original_response(embed=embed)
            print(e)

    def _initialize_embed(self, interaction: discord.Interaction) -> discord.Embed:
        embed: discord.Embed = discord.Embed(title="聊天句數統計", url="https://github.com/balaOuO/discord-statistics-bot", description="計算中...", color=0xffdfa8)
        embed.set_thumbnail(url=self.interaction.user.avatar.url)
        return embed
