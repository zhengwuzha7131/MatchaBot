import discord
from discord.ext import commands

from yt_dlp import YoutubeDL

import asyncio

class music_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
        self.is_playing = False
        self.is_paused = False
        
        self.music_queue = []
        self.YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True'}
        self.FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
        
        
        self.vc = None
        
    def search_yt(self, item):
        with YoutubeDL(self.YDL_OPTIONS) as ydl:
            try: 
                info = ydl.extract_info(f"ytsearch:{item}", download=False)['entries'][0]
            except Exception:
                return False
            
        return {'source': info['url'], 'title': info['title']}
    
    async def play_next(self, ctx):
        if(len(self.music_queue) > 0):
            self.is_playing = True
            
            m_url = self.music_queue[0][0]['source']
            self.music_queue.pop(0)
            
            await self.play_music(ctx)
            
    async def play_music(self, ctx):
        if len(self.music_queue) > 0:
            self.is_playing = True
            
            m_url = self.music_queue[0][0]['source']
            
            if self.vc == None or not self.vc.is_connected():
                self.vc = await self.music_queue[0][1].connect()
                
                if self.vc == None:
                    await ctx.send("Could not join the voice channel!")
                    return
            else:
                await self.vc.move_to(self.music_queue[0][1])
                        
            self.vc.play(discord.FFmpegPCMAudio(m_url, **self.FFMPEG_OPTIONS), after=lambda e: asyncio.run_coroutine_threadsafe(self.play_next(ctx), self.bot.loop))
            
            embed = discord.Embed(title="Now Playing", url=m_url, description=f"Now playing: {self.music_queue[0][0]['title']}", color=0x74A12E)
            
            await ctx.send(embed=embed)

        else:
            self.is_playing = False
            if self.vc:
                await self.vc.disconnect()
                self.vc = None
            
    @commands.command(name="play", aliases=["p", "playing"], help="Play the selected song from YouTube")
    async def play(self, ctx, *args):
        message = " ".join(args)
        
        voice_channel = ctx.author.voice.channel
        if voice_channel is None:
            await ctx.send("You are not in a voice channel!")
        else:
            song = self.search_yt(message)
            
            if type(song) == type(True):
                await ctx.send("Could not download the song. The song may be too long.")
            else:                             
                if self.is_playing:
                    await ctx.send(f"Added {song['title']} to the queue!")             
                   
                self.music_queue.append([song, voice_channel])

                if self.is_playing == False:
                    await self.play_music(ctx)
                    self.music_queue.pop(0)

    @commands.command(name="pause", help="Pauses the current song")
    async def pause(self, ctx, *args):
        if self.vc and self.vc.is_playing():
            self.vc.pause()
            self.is_paused = True
            await ctx.send("Paused the song!")
        else:
            await ctx.send("I am not playing anything!")
            
    @commands.command(name="resume", aliases=["r"], help="Resumes the current song")
    async def resume(self, ctx, *args):
        if self.vc and self.is_paused:
            self.vc.resume()
            self.is_paused = False
            await ctx.send("Resumed the song!")
        else:
            await ctx.send("I am not paused!")
            
    @commands.command(name="skip", aliases=["s"], help="Skips the current song")
    async def skip(self, ctx, *args):
        if self.vc and self.vc != None:
            self.vc.stop()
            
            if len(self.music_queue) > 0:
                await self.play_music(ctx)
            else:
                await ctx.send("Queue is empty!")
                await asyncio.sleep(5)
                await self.vc.disconnect()
            
    @commands.command(name="queue", aliases=["q"], help="Displays the queue")
    async def queue(self, ctx):
        message = ""
        
        for i in range(0, len(self.music_queue)):
            if i > 4: break
            message += f"{i + 1}. " + self.music_queue[i][0]['title'] + "\n"
        
        if message != "":
            await ctx.send(message)
        else:
            await ctx.send("No songs in queue!")
    
    @commands.command(name="clear", aliases=["c"], help="Stops the current song and clears the queue")
    async def clear(self, ctx, *args):
        self.music_queue = []
        if self.vc != None and self.is_playing:
            self.vc.stop()
        await ctx.send("Cleared the queue!")
        
    @commands.command(name="stop", aliases=["disconnect", "l", "d", "leave"], help="Leaves the voice channel")
    async def stop(self, ctx):
        self.is_playing = False
        self.is_paused = False
        await self.vc.disconnect()
        self.vc = None
        
    @commands.command(name="remove", aliases=["rem"], help="Removes a song from the queue")
    async def remove(self, ctx, *args):
        if len(args) == 0 or not args[0].isdigit() or int(args[0]) > len(self.music_queue):
            await ctx.send("Please enter a valid number from the queue!")
            return
        else:
            await ctx.send(f"Removed ***{self.music_queue[int(args[0]) - 1][0]['title']}*** from the queue!")
            self.music_queue.pop(int(args[0]) - 1)
    