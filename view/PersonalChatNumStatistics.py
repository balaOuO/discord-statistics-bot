import discord
from discord.ext import commands
from typing import Optional , AsyncIterator
import logging
import asyncio
from datetime import datetime , timezone
from view.ChatNumStatistics import ChatNumStatistics

class PersonalChatNumStatistics(ChatNumStatistics):

    def __init__(
        self , 
        interaction: discord.Interaction ,
        start : Optional[str] = None ,
        end : Optional[str] = None ,
        member : discord.Member = None ,
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
            self.member = member

    def message_count_result(self):
        return f'{self.member.mention} : {self.msg_dict[self.member.id]}\n'


