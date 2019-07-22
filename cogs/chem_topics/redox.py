#discord imports
import asyncio, discord
from discord.ext import commands
#standard imports
import random
import json
import math

#class holding questions
class redox(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    #randomizer
    async def rando(self, ctx, question):
        if question == -1:
            question = random.randrange(0, 1)

        if question == 0:
            await self.reagents(ctx)

    #redox reagents
    async def reagents(self, ctx):
        #dict of reagents
        with open('resources/redox.json', 'r') as f:
            reagents_dict = json.load(f)
        f.close()
  
        #get the whether the question is asking for the reducing agent or oxidizing agent
        pick_redox = random.choice(["a reducing agent", "an oxidizing agent"])

        #set the vars
        reagents = list(reagents_dict.keys())
        pick = random.randrange(0, 5)
        choices = [None] * 5

        #get the right answer choice
        while True:
            random.shuffle(reagents)
            if pick_redox == reagents_dict[reagents[0]]:
                choices[pick] = f"**{pick}**) {reagents[0]}"
                break

        #get the wrong answer choices
        counter = 0
        while True:
            #skip the section if already filled
            if choices[counter] != None:
                counter += 1
                continue
            else:
                random.shuffle(reagents)
                if pick_redox != reagents_dict[reagents[0]]:
                    choices[counter] = f"**{counter}**) {reagents[0]}"
                    counter += 1
                if counter >= 5:
                    break

        #ask question and print list
        quest = f'Question for **{ctx.author.display_name}**. (1 point)\n'
        quest += f'Which of these choices is {pick_redox}?\n\t\t'
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
    bot.add_cog(redox(bot))


 

      	


