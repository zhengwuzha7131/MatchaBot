import discord
from discord.ext import commands

class help_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
        self.help_message = """
        
        ```
        Commands:
        .help - Displays this message
        .hello - Greets the user
        .join - Joins the voice channel
        .leave - Leaves the voice channel
        .play - Plays a song
        .pause - Pauses the song
        .resume - Resumes the song
        .stop - Stops the song
        ```
        """
        
        self.text_channel_text = []
        
        @commands.command(name="help", help="Displays this message")
        async def help(self, ctx):
            await ctx.send(self.help_message)