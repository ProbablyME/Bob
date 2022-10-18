import discord
from discord.ext import commands

class help_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
        self.help_message = """
```    
Commandes musicales:

b!help - Affiche toutes les commandes
b!p - Trouve la musique sur youtube et la joue sur le salon vocal au quel tu es connecté 
b!q - Affiche la liste d'attente actuelle
b!skip - Skip la musique actuelle 
b!clear - Vide la file d'attente
b!leave - Quitte le salon vocal
b!pause - Mets en pause la lecture
b!resume - Reprends la lecture
```
"""
        self.text_channel_text = []
        
    @commands.Cog.listener()
    async def on_ready(self):
        for guild in self.bot.guilds:
            for channel in guild.text_channels:
                self.text_channel_text.append(channel)
                
        await self.send_to_all(self.help_message)
        
    async def send_to_all(self, msg):
        for channel in self.text_channel_text:
            await channel.send(msg)
    
    @commands.command(name="help", help="Displays all avaible commands")
    async def help(self,ctx):
        await ctx.send(self.help_message)