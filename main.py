import discord
from discord.ext import commands
from discord import FFmpegPCMAudio

from apikeys import * #This file will not be accessible for the public

from music_cog import music_cog
from help_cog import help_cog

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='.', intents=intents)

bot.remove_command("help") #Remove default help command

#Initialize cogs
@bot.event
async def on_ready():
    await bot.add_cog(music_cog(bot))
    await bot.add_cog(help_cog(bot))
    print("Bot is ready and laoded with cog")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(1269124408786686076)
    await channel.send("Hello! Welcome to the server and we hope you have a matcha time here! :green_heart:")
    
#Commands
    
@bot.command()
async def hello(ctx):
    await ctx.send("Hello! I am Matcha for all the Matcha lovers out there! :green_heart:")

bot.run(BOTTOKEN) #From apikeys