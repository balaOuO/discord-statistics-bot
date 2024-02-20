import discord
from discord.ext import commands
from discord import app_commands
import json

class help(commands.Cog):
    def __init__(self , bot : commands.bot) -> None:
        self.bot = bot

    @app_commands.command(name="阿巴阿巴" , description="機器人使用說明")
    async def abaaba(self , interaction: discord.Interaction):
        embed=discord.Embed(title="Bot_La使用說明", url="https://youtu.be/dQw4w9WgXcQ?si=0IY_lXd6UNLsaP9l" , color=0x9577cb )
        embed.set_footer(text="Developed by balaOuO" , icon_url="https://avatars.githubusercontent.com/u/99466599?v=4")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/890563901501087785/1209412335136149544/e_089.jpg?ex=65e6d402&is=65d45f02&hm=26c3cc71a9663e37d77671ce4861641303b1db69f0f93829719ab8d975dbc082&")
        try:
            self.generate_field(embed=embed)
        except Exception as e:
            print(e)
        await interaction.response.send_message(embed=embed)

    def generate_field(self , embed : discord.Embed):
        with open("cogs/help.json", "r" , encoding='utf-8') as f:
            help = json.load(f)

        for command in help['commands']:
            description : str = command['description'] + "\n"
            for parameter in command["parameters"]:
                description += parameter + "\n"
            embed.add_field(name=f"</{command['name']}:{command['id']}>" , value=description , inline=False)

# Cog 載入 Bot 中
async def setup(bot: commands.Bot):
    await bot.add_cog(help(bot))