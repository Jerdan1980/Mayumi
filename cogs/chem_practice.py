#discord imports
import asyncio, discord
from discord.ext import commands
#standard imports
import random
import json
import math

#class holding questions
class chem_practice(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
        #list of ksp
        klist = []
        with open('resources/Ksp.txt', 'r') as f:
            for line in f:
                line = line.split(',')
                klist.append(Ksp(line[0], line[1], line[2], line[3]))
        f.close()
        self.Ksp_list = klist

        #list of acids
        alist = []
        with open('resources/polyacids.txt', 'r') as f:
            for line in f:
                line = line.split(',')
                alist.append(pH(line[0], 1, line[1], line[2]))
        f.close()
        self.acid_list = alist


    #randomizer
    @commands.command()
    async def quiz(self, ctx, pick: int = -1):
        #randomize if no user input
        #user input is meant for testing purposes only
        if pick == -1:
            pick = random.randrange(0, 4)

        if pick == 0:
            await self.molsol(ctx)
        elif pick == 1:
            await self.solrules(ctx)
        elif pick == 2:
            await self.polyacids(ctx)
        elif pick == 3:
            await self.flametests(ctx)

    #molar solubility
    async def molsol(self, ctx):
        #shuffle the list to get a random Ksp
        random.shuffle(self.Ksp_list)
        salt = self.Ksp_list[0]

        #ask the question
        quest = f'Question for **{ctx.author.display_name}**:\n'
        quest += f'\tYou have `{salt.name}` with Ksp {salt.Ksp}. What is the molar solubility? Assume the question does not require the use of the quadratic formula.'
        quest += '\nReply in format `submit <answer>`. Do not include units. Ex: `submit 3`. You have a 2% tolerance'
        await ctx.send(quest)

        #checker method
        def check(msg):
            return msg.content.startswith('submit') and msg.author == ctx.author and msg.channel == ctx.channel

        #grab input and check for correctness
        try:
            msg = await self.bot.wait_for('message', timeout=120.0, check=check)
        except asyncio.TimeoutError:
            await ctx.send(f'**{ctx.author.display_name}** out of time! the correct answer is ||{salt.S}||')
        else:
            answer = float(msg.content.split()[1])
            if (abs(answer-salt.S) / salt.S * 100) <= 2:
                await ctx.send(f'**{ctx.author.display_name}** correct.')
                profile = self.bot.get_cog('profile')
                await profile.add_pts(str(ctx.author.id), 1)
            else:
                await ctx.send("**{:}** incorrect. The correct answer is {:.3e}".format(ctx.author.display_name, salt.S))

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

    #polyprotic acids
    async def polyacids(self, ctx):
        #shuffle the list to get a random acid
        random.shuffle(self.acid_list)
        acid = self.acid_list[0]

        #randomize the question
        pick_K = bool(random.getrandbits(1))
        pick_pH = random.choice(["pH", "pOH"])

        #print out the question
        quest = f'Question for **{ctx.author.display_name}**:\n'
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
    bot.add_cog(chem_practice(bot))

#class for Ksp
class Ksp():
    def __init__(self, name_of_salt, Ksp_val, x, y):
        self.name = name_of_salt
        self.Ksp = float(Ksp_val)
        self.x = int(x)
        self.y = int(y)
        self.S = pow(self.Ksp / (pow(self.y, self.y) * pow(self.x, self.x)), 1.0 / (self.x + self.y))

#class for polyacids
class pH():
    def __init__(self, acid_name, acidbool, K1, K2):
        self.name = acid_name
        self.is_acid = acidbool
        
        if self.is_acid:
            self.Ka1 = float(K1)
            self.Ka2 = float(K2)
            self.Kb1 = 1e-14 / self.Ka1
            self.Kb2 = 1e-14 / self.Ka2
            self.pH = -1 * math.log10(pow(self.Ka1 * self.Ka2, 0.5 ))
            self.pOH = 14 - self.pH
        elif not self.is_acid:
            self.Kb1 = float(K1)
            self.Kb2 = float(K2)
            self.Ka1 = 1e-14 / self.Kb1
            self.Ka2 = 1e-14 / self.Kb2
            self.pOH = -1 * math.log10(pow(self.Kb1 * self.Kb2, 0.5 ))
            self.pH = 14 - self.pOH
