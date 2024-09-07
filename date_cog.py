import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions
from dateutil import relativedelta
from datetime import datetime
from datetime import timezone
from datetime import time
import pytz


class date_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
        self.zone = pytz.timezone('America/New_York')
    
    @commands.command()
    async def timezone(self, ctx, tz: str = None):
        if tz:
            try:
                self.zone = pytz.timezone(tz)
                await ctx.send(f"Timezone has been set to **{tz}**")
            except pytz.exceptions.UnknownTimeZoneError:
                await ctx.send("Invalid timezone")
        else:
            current_time = datetime.now(self.zone)
            await ctx.send(f"Current timezone is **{self.zone}** with current time **{current_time.strftime('%I:%M:%S')}**")
    
    @commands.command()
    async def date(self, ctx):
        current_time = datetime.now(self.zone)
        await ctx.send(f"Current date is **{current_time.strftime('%Y-%m-%d')}**")

    @commands.command()
    async def time(self, ctx):
        current_time = datetime.now(self.zone)
        await ctx.send(f"Current time is **{current_time.strftime('%I:%M:%S %p')}**")
    
    @commands.command()
    async def daysSince(self, ctx, date: str):
        try: 
            date = datetime.strptime(date, "%Y-%m-%d")
            current_time = datetime.now(self.zone)
            delta = current_time - date
            await ctx.send(f"Days since {date.strftime('%Y-%m-%d')} is **{delta.days}**")
        except ValueError:
            await ctx.send("Invalid date format. Please use **YYYY-MM-DD**")