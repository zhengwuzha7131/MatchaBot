import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions

#Commands to take care of a discord server

class general_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
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
            
    @commands.command()
    @has_permissions(manage_messages=True)
    async def purge(self, ctx, limit: int = 100):
        limit = min(limit, 100)
        deleted = await ctx.channel.purge(limit=limit)
        await ctx.send(f"Purged {len(deleted)} messages (I can at most delete 100 messages)")

        
    @purge.error
    async def purge_error(ctx, error):
        if isinstance(error, MissingPermissions):
            await ctx.send("You do not have permissions to delete messages!")