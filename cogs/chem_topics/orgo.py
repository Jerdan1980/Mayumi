#discord imports
import asyncio, discord
from discord.ext import commands
#rdkit imports
from rdkit import Chem
from rdkit.Chem import Draw
from rdkit.Chem.EnumerateStereoisomers import EnumerateStereoisomers, StereoEnumerationOptions
#standard imports
import random
import os

#class holding questions
class orgo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    #randomizer
    async def rando(self, ctx, question):
        #randomize
        if question == -1:
            question = random.randrange(0, 1)
        
        if question == 0:
            await self.isomers(ctx)

    #isomers
    async def isomers(self, ctx):
        #create list of chemicals here
        isomer_list = []
        with open("resources/isomer_list.txt", "r") as f:
            for line in f:
                isomer_list.append(line)
        f.close()

        #shuffle the list to get a random chemical
        random.shuffle(isomer_list)
        chemical = isomer_list[0]

        # get answer based off of it
        m = Chem.MolFromSmiles(chemical)
        opts = StereoEnumerationOptions(unique=True)
        isomers = tuple(EnumerateStereoisomers(m, options=opts))
        num_isomers = len(isomers)

        #ask the question
        quest = f'Question for **{ctx.author.display_name}**: (1 point)\n'
        quest += f'\tHow many isomers does the drawing below have? Include cis-trans/E-Z isomers and stereoisomers.'
        quest += '\nAnswer in format `submit answer`. Ex. `submit 3`.'
        
        Draw.MolToFile(m, f'images/{ctx.author.id}.png')
        await ctx.send(quest, file=discord.File(f"images/{ctx.author.id}.png"))
        os.remove(f"images/{ctx.author.id}.png")

        #checker method
        def check(msg):
            return msg.content.startswith('submit') and msg.author == ctx.author and msg.channel == ctx.channel

        #grab input and check for correctness
        try:
            msg = await self.bot.wait_for('message', timeout=600.0, check=check)
        except asyncio.TimeoutError:
            await ctx.send(f'Out of time! the correct answer is ||{num_isomers}||')
        else:
            answer = int(msg.content.split()[1])
            if answer == num_isomers:
                await ctx.send(f'**{ctx.author.display_name}** correct.')
                profile = self.bot.get_cog('profile')
                await profile.add_pts(str(ctx.author.id), 1)
            else:
                await ctx.send(f'**{ctx.author.display_name}** incorrect. The correct answer is {num_isomers}')


def setup(bot):
    bot.add_cog(orgo(bot))