import discord
from discord.ext import commands

from apikeys import * #This file will not be accessible for the public

#Define intens
intents = discord.Intents.default()
intents.typing = False
intents.presences = True
intents.messages = True
intents.guilds = True
intents.reactions = True
intents.message_content = True
intents.members = True

client = commands.Bot(command_prefix='.', intents=intents)

#Events

@client.event
async def on_ready():
    print("Bot is ready")
    
@client.event
async def on_member_join(member):
    channel = client.get_channel(1269124408786686076)
    await channel.send("Hello! Welcome to the server and we hope you have a matcha time here! :green_heart:")
    
@client.command()
async def hello(ctx):
    await ctx.send("Hello! I am Matcha for all the Matcha lovers out there! :green_heart:")
    
client.run(BOTTOKEN) #From apikeys