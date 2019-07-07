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
    async def rando(self, ctx, question):
        if question == -1:
            question = random.randrange(0,2)
        
        if question == 0:
            await self.solrules(ctx)
        elif question == 1:
            await self.solrulesMC(ctx)
    
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
        quest = f'Question for **{ctx.author.display_name}**. (1 point)\n'
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

    #solubility rules multiple choice questions
    async def solrulesMC(self, ctx):
        #dict of solubilities
        with open('resources/solubility.json') as f:
            Formula_dict = json.load(f)
        f.close()        

        #get the answer (sol/insol)
        pick_sol = random.randrange(0, 1)

        #set the vars
        solubility = list(Formula_dict.keys())
        pick = random.randrange(0, 5)
        choices = [None] * 5

        #get the right answer choice
        while True:
            random.shuffle(solubility)
            if pick_sol == Formula_dict[solubility[0]]:
                choices[pick] = f"**{pick}**) {solubility[0]}"
            break

        #get the wrong answer choices
        counter = 0
        while counter < 5:
            #skip the section if already filled
            if counter == pick:
                counter += 1
                continue
            else:
                random.shuffle(solubility)
                if pick_sol != Formula_dict[solubility[0]]:
                    choices[counter] = f"**{counter}**) {solubility[0]}"
                    counter += 1

        #ask question and print list
        quest = f'Question for **{ctx.author.display_name}**. (1 point)\n'
        if pick_sol:
            quest += f'\tWhich of these choices is soluble?\n\t\t'
        else:
            quest += '\tWhich of these choices is insoluble?\n\t\t'
        quest += "\n\t\t".join(choices)
        quest += '\nAnswer in format `submit answer`. Ex: `submit 1`'
        await ctx.send(quest)

        #checker method
        def check(msg):
            return msg.content.startswith('submit') and msg.author == ctx.author and msg.channel == ctx.channel

        #grab input and check for correctness
        try:
            msg = await self.bot.wait_for('message', timeout=45.0, check=check)
        except asyncio.TimeoutError:
            await ctx.send(f'**{ctx.author.display_name}** out of time! the correct answer is ||{pick}||')
        else:
            answer = int(msg.content.split()[1])
            if answer == pick:
                await ctx.send(f'**{ctx.author.display_name}** correct.')
                profile = self.bot.get_cog('profile')
                await profile.add_pts(str(ctx.author.id), 1)
            else:
                await ctx.send(f'**{ctx.author.display_name}** incorrect. The correct answer is {pick}.')


def setup(bot):
    bot.add_cog(matter(bot))