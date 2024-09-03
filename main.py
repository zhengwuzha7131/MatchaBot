import discord
from discord.ext import commands
from discord import FFmpegPCMAudio
import requests
import json
import os
import asyncio
import re

from music_cog import music_cog
from help_cog import help_cog
from general_cog import general_cog
from events_cog import events_cog
from weather_cog import weather_cog

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv() #To Load the API Keys and Tokens from .env file as I don't want to get leaked :D

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='.', intents=intents, help_command=None)

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

@bot.event
async def on_ready():
    await bot.add_cog(music_cog(bot))
    await bot.add_cog(help_cog(bot))
    await bot.add_cog(general_cog(bot))
    await bot.add_cog(events_cog(bot))
    await bot.add_cog(weather_cog(bot))
    print("Bot is ready and laoded with cog")
    
#ChatGPT Configuration

conversation_history = [{
    "role": "system",
    "content": "You are a helpful assistant and you will be a friendly chatbot."
}]

async def ask_chatgpt(message):
    
    try:
        chat_completion = client.chat.completions.create(
            model="gpt-4o",
            messages= conversation_history
        )

        response_message = chat_completion.choices[0].message.content
            
        return response_message
        
    except Exception as e:
        print(f"Error: {str(e)}")
        return "Sorry, I can't respond at the moment."

# Command to talk to ChatGPT, the usage will be .gpt <message>
@bot.command()
async def gpt(ctx, *, query):
    await ctx.typing()
    
    conversation_history.append({
        "role": "user",
        "content": query
    })

    previous_messages = []
    
    async for message in ctx.channel.history(limit=10):
        previous_messages.append(message)
    
    previous_messages.reverse()
    
    for msg in previous_messages:
        role = "assistant" if msg.author == bot.user else "user"

        username = sanitize_username(msg.author.name) if role == "user" else None
        content = re.sub(r'^\.gpt\s+', '', msg.content)
        
        message_info = {
            "role": role,
            "content": content
        }
        
        if role == "user":
            message_info["name"] = username

        conversation_history.append(message_info)

    response = await ask_chatgpt(query)
    
    CHUNKSIZELIMIT = 2000
        
    for i in range(0, len(response), CHUNKSIZELIMIT):
        chunk = response[i:i+CHUNKSIZELIMIT]
        await ctx.send(chunk)

def sanitize_username(username):
    return re.sub(r'\W+', '_', username)

bot.run(os.environ.get("DISCORD_TOKEN"))