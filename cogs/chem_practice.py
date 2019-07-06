#discord imports
import asyncio, discord
from discord.ext import commands
#standard imports
import random

chem_topics = ["descriptive", "equilibrium", "matter", "acids"]

#class holding questions
class chem_practice(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    #randomizer
    @commands.command()
    async def quiz(self, ctx):
        random.shuffle(chem_topics)
        await self.bot.get_cog(chem_topics[0]).rando(ctx)

def setup(bot):
    bot.add_cog(chem_practice(bot))