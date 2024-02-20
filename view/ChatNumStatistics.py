import discord
from discord.ext import commands
from typing import Optional , AsyncIterator
import logging
import asyncio
from datetime import datetime , timezone

class ChatNumStatistics:
    def __init__(
        self , 
        interaction: discord.Interaction ,
        start : Optional[str] = None ,
        end : Optional[str] = None ,
        limit : Optional[int] = 30000
        ) -> None:
            self.interaction = interaction
            self.embed : discord.Embed
            self.limit = limit
            self.start_date : Optional[datetime] = None
            self.end_date : Optional[datetime] = None
            self.create_time_interval(start_date_str=start , end_date_str=end)
            self.msg_dict : dict = {}
            self.frist_msg_time = datetime(year=3000 , month=12 , day=31 , tzinfo=timezone.utc)
            self.last_msg_time = datetime(year=500 , month=1 , day=1 , tzinfo=timezone.utc)
            self.overflow_channel : list[discord.VoiceChannel | discord.Thread | discord.TextChannel] = []

    # main function
    async def main(self):
        try:
            await self.initialize_embed()
            # await self.interaction.response.defer() #可將interaction有效時間延長為15分鐘
            await self.calculate_message_count()
            await self.response_result()
        except Exception as e:
            self.embed.description = "⚠️there are something wrong⚠️"
            await self.interaction.edit_original_response(embed=self.embed)
            print(e)

    # 初始化embed
    async def initialize_embed(self):
        """
        初始化embed
        """
        self.embed=discord.Embed(title="聊天句數統計", url="https://youtu.be/dQw4w9WgXcQ?si=0IY_lXd6UNLsaP9l", description="計算中...", color=0xffdfa8)
        self.embed.set_thumbnail(url=self.interaction.user.avatar.url)
        await self.interaction.response.send_message(embed=self.embed)

    # 計算統計時間區間
    def create_time_interval(self , start_date_str : str | None , end_date_str : str | None):
        """
        計算統計時間區間
        """
        if (start_date_str is None and end_date_str is None):
            today = datetime.now()
            self.start_date = datetime(year=today.year , month=today.month , day=1 , tzinfo=timezone.utc)
            self.end_date = None
        else:
            self.start_date = datetime.strptime(start_date_str , '%Y-%m-%d') if not(start_date_str is None) else None
            self.end_date = datetime.strptime(end_date_str , '%Y-%m-%d') if not(end_date_str is None) else None

    # 計算guild內所有member的message數量
    async def calculate_message_count(self):
        """
        計算guild內所有member的message數量
        """
        for member in self.interaction.guild.members:
            self.msg_dict.setdefault(member.id , 0)

        all_channels = self.interaction.guild.text_channels + list(self.interaction.guild.threads) + self.interaction.guild.voice_channels
        total = 1
        for channel in all_channels:
            self.embed.description = f'統計進度({total}/{len(all_channels)})\n正在統計 {channel.jump_url}'
            # 多線程
            progress_task = asyncio.create_task(self.interaction.edit_original_response(embed=self.embed))
            calculate_task = asyncio.create_task(self.calculate_single_channel(channel=channel))
            await calculate_task
            await progress_task
            total += 1

    # 記算單一頻道訊息數
    async def calculate_single_channel(self , channel : discord.VoiceChannel | discord.Thread | discord.TextChannel):
        channel_messages = channel.history(limit=self.limit , after=self.start_date , before=self.end_date)
        message_num = 0
        async for msg in channel_messages:
            self.frist_msg_time = msg.created_at if msg.created_at < self.frist_msg_time else self.frist_msg_time
            self.last_msg_time = msg.created_at if msg.created_at > self.last_msg_time else self.last_msg_time
            self.msg_dict.setdefault(msg.author.id , 0)
            self.msg_dict[msg.author.id] += 1
            message_num += 1
        if message_num >= self.limit:
            self.overflow_channel.append(channel)

    # 回覆使用者計算結果
    async def response_result(self):
        """
        回覆使用者計算結果
        """
        return_str = ''
        sorted_msg_list = sorted(self.msg_dict.items() , key=lambda x : x[1] , reverse=True)
        for data in sorted_msg_list:
            member = self.interaction.guild.get_member(data[0])
            return_str += f'{member.mention} : {data[1]}\n' if not(member is None) else f'{data[0]} (已退出) : {data[1]}\n'
        
        if len(self.overflow_channel) != 0:
            return_str += "`超過訊息上限` "
            for channel in self.overflow_channel:
                return_str += channel.jump_url + " "
        
        self.embed.description = return_str
        if self.frist_msg_time.year != 3000:
            self.embed.set_footer(text=f"[from] : {self.frist_msg_time.date()}\n[to]   : {self.last_msg_time.date()}\n")
        else:
            self.embed.set_footer(text="[無聊天紀錄]")
        await self.interaction.edit_original_response(embed=self.embed)