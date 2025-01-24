import discord


class StatisticsEmbed:
    def __init__(self):
        self.embed: discord.Embed = discord.Embed(colour = 0xffdfa8)

    def initialize(self, user_url: str) -> discord.Embed:
        self.embed.title = "聊天句數統計"
        self.embed.url = "https://github.com/balaOuO/discord-statistics-bot"
        self.embed.description = "計算中..."
        self.embed.set_thumbnail(url = user_url)

        return self.embed

    def update_progress_bar(self, current: int, total: int, current_channel: discord.TextChannel) -> discord.Embed:
        self.embed.description = f'統計進度({current}/{total})\n'
        self.embed.description += f'正在統計 {current_channel.jump_url}\n'

        return self.embed
