import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions

#Commands to take care of a discord server

class general_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.bot.get_channel(1269124408786686076)
        await channel.send("Hello! Welcome to the server and we hope you have a matcha time here! :green_heart:")
        
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.content == "matcha":
            await message.channel.send("Matcha is love! :green_heart:")
        
    @commands.command()
    async def hello(self, ctx):
        await ctx.send("Hello! I am Matcha for all the Matcha lovers out there! :green_heart:")
        
    @commands.command()
    @has_permissions(kick_members=True)
    async def kick(ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)
        await ctx.send(f"{member} has been kicked!")
        
    @kick.error
    async def kick_error(ctx, error):
        if isinstance(error, MissingPermissions):
            await ctx.send("You do not have permissions to kick members!")
            
    @commands.command()
    @has_permissions(ban_members=True)
    async def ban(ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)
        await ctx.send(f"{member} has been banned!")
        
    @ban.error
    async def ban_error(ctx, error):
        if isinstance(error, MissingPermissions):
            await ctx.send("You do not have permissions to ban members!")