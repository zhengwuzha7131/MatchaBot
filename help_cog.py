import discord
from discord.ext import commands

class help_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.help_message = """
```
Available commands:
.hello - Greets the user    
.gpt <message> - Ask a bot a question (Currently it does not have memory)
.play <song> - Play the selected song from YouTube
.pause - Pause the current song
.resume - Resume the current song
.remove <index> - Remove the ith index from the queue
.queue - Displays the current queue
```
        """

    @commands.command(name="help", help="Displays this message")
    async def help(self, ctx):
        await ctx.send(self.help_message)