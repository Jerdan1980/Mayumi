#discord imports
import asyncio, discord
from discord.ext import commands
#standard imports
import random

#class holding questions
class chem_practice(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    #randomizer
    @commands.command()
    async def quiz(self, ctx, topic: int = -1, question: int = -1):
        #chem_topics
        descriptive = self.bot.get_cog("descriptive")
        equilibrium = self.bot.get_cog("equilibrium")
        matter = self.bot.get_cog("matter")
        acids = self.bot.get_cog("acids")

        #get random
        if topic == -1:
            topic = random.randrange(0, 4)
        
        #activate topic
        if topic == 0:
            await descriptive.rando(ctx, question)
        if topic == 1:
            await equilibrium.rando(ctx, question)
        if topic == 2:
            await matter.rando(ctx, question)
        if topic == 3:
            await acids.rando(ctx, question)


def setup(bot):
    bot.add_cog(chem_practice(bot))
