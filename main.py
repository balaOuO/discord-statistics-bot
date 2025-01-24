import os
import asyncio
from random import randint

import discord
from discord.ext import commands
from dotenv import load_dotenv
import argparse

load_dotenv()

intents = discord.Intents.all()
bot = commands.Bot(command_prefix = "$", intents = intents)

# 當機器人完成啟動時
@bot.event
async def on_ready():
    slash = await bot.tree.sync()
    print(f"目前登入身份 --> {bot.user}")
    print(f"載入 {len(slash)} 個斜線指令")
    await bot.change_presence(activity=discord.Game(name="西瓜"))

@bot.event
async def on_message(message: discord.Message):
    if (message.author == bot.user):
        return

    send_message = ["叫屁", "幹你娘", "閉嘴"]
    try:
        if bot.user in message.mentions:
            await message.channel.send(send_message[randint(0, len(send_message) - 1)])
        if ("嗨老虎" in message.content):
            await message.reply("閉嘴")
    except Exception as e:
        print(e)

# 載入指令程式檔案
@bot.command()
async def load(ctx : commands.Context , extension):
    if (ctx.author.id != 516971767143858188):
        await ctx.send("no permissions")
        return
    await bot.load_extension(f"cogs.{extension}")
    await ctx.send(f"Loaded {extension} done.")

# 卸載指令檔案
@bot.command()
async def unload(ctx : commands.Context, extension):
    if (ctx.author.id != 516971767143858188):
        await ctx.send("no permissions")
        return
    await bot.unload_extension(f"cogs.{extension}")
    await ctx.send(f"UnLoaded {extension} done.")

# 重新載入程式檔案
@bot.command()
async def reload(ctx : commands.Context, extension):
    if (ctx.author.id != 516971767143858188):
        await ctx.send("no permissions")
        return
    await bot.reload_extension(f"cogs.{extension}")
    await ctx.send(f"ReLoaded {extension} done.")

@bot.command()
async def sync_commands(ctx : commands.Context):
    if (ctx.author.id != 516971767143858188):
        await ctx.send("no permissions")
        return
    await bot.tree.sync()
    await ctx.send("Sync done.")

# 一開始bot開機需載入全部程式檔案
async def load_extensions():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")

async def main():
    parser = argparse.ArgumentParser(description="Start Discord Statistics Bot")
    parser.add_argument(
        "--mode",
        choices=["dev", "prod"],
        help="[dev]: Development Mode, [prod]: Production Mode",
        default="prod"
    )
    args = parser.parse_args()

    async with bot:
        await load_extensions()
        if args.mode == "dev":
            await bot.start(os.getenv("DEV_TOKEN"))
        elif args.mode == "prod":
            await bot.start(os.getenv("TOKEN"))

# 確定執行此py檔才會執行
if __name__ == "__main__":
    asyncio.run(main())