import discord
from discord.ext import commands
import os 

from help_cog import help_cog
#from music_cog import music_cog
from music import *

bot = commands.Bot(command_prefix='b!', intents=discord.Intents.all())
bot.remove_command('help')

@bot.event
async def on_ready():
    await bot.add_cog(music(bot))
    await bot.add_cog(help_cog(bot))
    await bot.change_presence(activity=discord.Streaming(name='BoB supremacy', url='https://www.twitch.tv/your_channel_here'))




    
    
bot.run('MTAyNjE5NzcwNDc2Nzk3MTQyOA.GFNJBC.c6BA9P-6eTwcLDacjE_JPONs2Y5Gxhx3DqwYVY')