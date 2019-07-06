#discord imports
import asyncio, discord
from discord.ext import commands
#standard imports
import random
import json
import math

#class holding questions
class descriptive(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def rando(self, ctx, question):
        if question == -1:
            question = random.randrange(0, 1)
        
        if question == 0:
            await self.flametests(ctx)

    #flame tests
    async def flametests(self,ctx):
        #dict of chemicals
        with open('resources/flametests.json', 'r') as f:
            Ion_dict = json.load(f)
        f.close()
            
        #shuffle the dict
        temp = list(Ion_dict.keys())
        random.shuffle(temp)
        ion = temp[0]

        #ask the question
        quest = f'Question for **{ctx.author.name}**\n'
        quest += f'\tWhat color is the flame test of {ion}?\n'
        quest += 'Reply in format `submit <answer>`.Please respond either a color of the rainbow or white, brown, or black. Ex: `submit red`.\n'
        quest += 'Any one of possible colors will be accepted as correct.'
        await ctx.send(quest)
        
        #checker method
        def check(msg):
            return msg.content.startswith('submit') and msg.author == ctx.author and msg.channel == ctx.channel

        #check the answer
        try:
            msg = await self.bot.wait_for('message', timeout=30.0, check=check)
        except asyncio.TimeoutError:
            await ctx.send(f'**{ctx.author.display_name}** out of time! the correct answer(s) are ||{", ".join(Ion_dict[ion])}||')
        else:
            answer = msg.content.split()[1]
            if answer.lower() in Ion_dict[ion]:
                await ctx.send(f'**{ctx.author.display_name}** correct.')
                profile = self.bot.get_cog('profile')
                await profile.add_pts(str(ctx.author.id), 1)
            else:
                await ctx.send(f'**{ctx.author.display_name}** incorrect. The correct answer(s) are {", ".join(Ion_dict[ion])}.')


def setup(bot):
    bot.add_cog(descriptive(bot))