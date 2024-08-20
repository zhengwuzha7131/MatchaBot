import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions

class events_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    