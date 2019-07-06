#discord imports
import asyncio, discord
from discord.ext import commands
#standard imports
import random
import json
import math

#class holding questions
class matter(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    #randomizer
    async def rando(self, ctx):
        await self.solrules(ctx)
    
    #solubility rules
    async def solrules(self, ctx):
        #dict of solubilities
        with open('resources/solubility.json', 'r') as f:
            Formula_dict = json.load(f)
        f.close()        

        #shuffle the dict to get a random key
        temp = list(Formula_dict.keys())
        random.shuffle(temp)
        Formula = temp[0]
        
        #ask the question
        quest = f'Question for **{ctx.author.display_name}**:\n'
        quest += f'\tIs `{Formula}` soluble or insoluble?'
        quest += '\nReply in format `submit <answer>`. Your answer should be either `soluble` or `insoluble`'
        await ctx.send(quest)

        #checker method
        def check(msg):
            return msg.content.startswith('submit') and msg.author == ctx.author and msg.channel == ctx.channel

        #grab input and check for correctness
        try:
            msg = await self.bot.wait_for('message', timeout=45.0, check=check)
        except asyncio.TimeoutError:
            if Formula_dict[Formula]:
                await ctx.send(f'**{ctx.author.display_name}** out of time! the correct answer is: ||Soluble||')
            else:
                await ctx.send(f'**{ctx.author.display_name}** out of time! the correct answer is: ||Insoluble||')
        else:
            answer = msg.content.split()[1]
            if (answer == 'soluble' and Formula_dict[Formula]) or (answer == 'insoluble' and not Formula_dict[Formula]):
                await ctx.send(f'**{ctx.author.display_name}** correct.')
                profile = self.bot.get_cog('profile')
                await profile.add_pts(str(ctx.author.id), 1)
            else:
                await ctx.send(f'**{ctx.author.display_name}** incorrect.')


def setup(bot):
    bot.add_cog(matter(bot))