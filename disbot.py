import discord
from discord.ext import commands
from discord.ext.commands import Bot

Bot = commands.Bot(command_prefix='!')

@Bot.event
async def on_ready():
    print('Бот онлайн!')

@Bot.command(pass_context = True)
async def hello(ctx):
    await ctx.send("Hello!!!")

Bot.run("NjgxNTgyNjc3MjQ5NDkwOTk5.Xmkbow.N3qpQjoyp4Qo_Ip5qg1UP1wd_3k")