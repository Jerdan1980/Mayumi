#discord imports
import asyncio, discord
from discord.ext import commands
#standard imports
import random

#class holding questions
class redox(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    #randomizer
    async def rando(self, ctx):
        pass

def setup(bot):
    bot.add_cog(redox(bot))