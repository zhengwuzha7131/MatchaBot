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
    async def timezone(self, ctx):
        current_time = datetime.now(self.zone)
        await ctx.send(f"Current timezone is {self.zone} with current time {current_time.strptime('%I:%M:%S')}")
    
    @commands.command()
    async def date(self, ctx):
        current_time = datetime.now(self.zone)
        await ctx.send(f"Current date is {current_time.strftime('%Y-%m-%d')}")