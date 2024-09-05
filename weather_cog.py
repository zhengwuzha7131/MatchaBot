import requests
import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions
import os

from dotenv import load_dotenv

load_dotenv()

class weather_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    async def weather(self, ctx, *, city: str):
        city_name = city
        complete_url = os.environ.get('BASE_URL') + "appid=" + os.environ.get('WEATHER_API_KEY') + "&q=" + city_name
        response = requests.get(complete_url)
        result = response.json()
        channel = ctx.message.channel

        if result["cod"] != "404":
            async with channel.typing():
                main = result["main"]
                temperatureK = main["temp"]
                temperatureF = str(round(((temperatureK - 273.15) * 1.8) + 32))
                feels_likeK = main["feels_like"]
                feels_likeF = str(round(((feels_likeK - 273.15) * 1.8) + 32))
                pressure = main["pressure"]
                humidity = main["humidity"]
                weather = result["weather"]
                weather_description = weather[0]["description"]

            embed = discord.Embed(title=f"Weather in {city_name}", color=0x00ff00, timestamp=ctx.message.created_at)
            embed.add_field(name="Temperature", value=f"{temperatureF}F", inline=False)
            embed.add_field(name="Feels Like", value=f"{feels_likeF}F", inline=False)
            embed.add_field(name="Pressure", value=f"{pressure}hPa", inline=False)
            embed.add_field(name="Humidity", value=f"{humidity}%", inline=False)
            embed.add_field(name="Weather Description", value=f"{weather_description}", inline=False)
            embed.set_thumbnail(url="https://i.ibb.co/CMrsxdX/weather.png")
            embed.set_footer(text="Powered by OpenWeatherMap")
            await channel.send(embed=embed)
        else:
            await channel.send("City not found!")
