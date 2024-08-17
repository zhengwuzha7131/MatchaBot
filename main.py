import discord
from discord.ext import commands
from discord import FFmpegPCMAudio
import requests
import json
import os

from music_cog import music_cog
from help_cog import help_cog

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='.', intents=intents, help_command=None)

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

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
    
#ChatGPT Configuration

async def ask_chatgpt(message):
    try:
        chat_completion = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": message}]
        )
        response_message = chat_completion.choices[0].message.content
        return response_message
    except Exception as e:
        print(f"Error: {str(e)}")
        return "Sorry, I can't respond at the moment."

# Command to talk to ChatGPT, the usage will be .gpt <message>
@bot.command()
async def gpt(ctx, *, query):
    response = await ask_chatgpt(query)
    await ctx.send(response)

bot.run(os.environ.get("DISCORD_TOKEN"))