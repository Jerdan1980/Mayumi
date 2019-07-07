#discord imports
import asyncio, discord
from discord.ext import commands
#standard imports
import random
import json
import math

#class holding questions
class acids(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        #list of acids
        alist = []
        with open('resources/polyacids.txt', 'r') as f:
            for line in f:
                line = line.split(',')
                alist.append(pH(line[0], line[1], line[2]))
        f.close()
        self.acid_list = alist

    #randomizer
    async def rando(self, ctx, question):
        #randomize
        if question == -1:
            question = random.randrange(0, 1)
        
        if question == 0:
            await self.polyacids(ctx)

    #polyprotic acids
    async def polyacids(self, ctx):
        #shuffle the list to get a random acid
        random.shuffle(self.acid_list)
        acid = self.acid_list[0]

        #randomize the question
        pick_K = bool(random.getrandbits(1))
        pick_pH = random.choice(["pH", "pOH"])

        #print out the question
        quest = f'Question for **{ctx.author.display_name}**. (1 point)\n'
        quest += f'\tA solution of `{acid.name}` has a '
        if pick_K:
            quest += "Ka1 of {:.3e} and the Ka2 of {:.3e}. ".format(acid.Ka1, acid.Ka2)
        elif not pick_K:
            quest += "Kb1 of {:.3e} and the Kb2 of {:.3e}. ".format(acid.Kb1, acid.Kb2)
        quest += f'What is the {pick_pH}? Assume the question does not require the use of the quadratic formula.'
        quest += '\nReply in format `submit <answer>`. Do not include units. Ex: `submit 3`. You have a 2% tolerance'
        await ctx.send(quest)

        #checker method
        def check(msg):
            return msg.content.startswith('submit') and msg.author == ctx.author and msg.channel == ctx.channel

        #check if it's right
        try:
            msg = await self.bot.wait_for('message', timeout=120.0, check=check)
        except asyncio.TimeoutError:
            if pick_pH:
                await ctx.send(f'**{ctx.author.display_name}** out of time! The correct answer is ||{round(acid.pH, 3)}||')
            else:
                await ctx.send(f'**{ctx.author.display_name}** out of time! The correct answer is ||{round(acid.pOH, 3)}||')
        else: 
            answer = float(msg.content.split()[1])
            if pick_pH and (abs(answer-acid.pH) / acid.pH * 100) <= 2:
                await ctx.send(f'**{ctx.author.display_name}** correct.')
                profile = self.bot.get_cog('profile')
                await profile.add_pts(str(ctx.author.id), 1)
            elif not pick_pH and (abs(answer-acid.pOH) / acid.pOH * 100) <= 2:
                await ctx.send(f'**{ctx.author.display_name}** correct.')
                profile = self.bot.get_cog('profile')
                await profile.add_pts(str(ctx.author.id), 1)
            else:
                await ctx.send(f'**{ctx.author.display_name}** incorrect. The correct answer is {round(acid.pH, 3)}')


def setup(bot):
    bot.add_cog(acids(bot))

#class for polyacids
class pH():
    def __init__(self, acid_name, K1, K2):
        self.name = acid_name
        self.Ka1 = float(K1)
        self.Ka2 = float(K2)
        self.Kb1 = 1e-14 / self.Ka1
        self.Kb2 = 1e-14 / self.Ka2
        self.pH = -1 * math.log10(pow(self.Ka1 * self.Ka2, 0.5 ))
        self.pOH = 14 - self.pH
