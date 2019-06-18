#discord imports
import asyncio, discord
from discord.ext import commands
#standard imports
import random
import json

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

    #randomizer
    @commands.command()
    async def quiz(self, ctx):
        pick = random.randrange(0, 2)
        if pick == 0:
            await self.molsol(ctx)
        elif pick == 1:
            await self.solrules(ctx)

    #molar solubility
    async def molsol(self, ctx):
        #shuffle the list to get a random Ksp
        random.shuffle(self.Ksp_list)
        salt = self.Ksp_list[0]

        #ask the question
        await ctx.send(f'You have {salt.name} with Ksp {salt.Ksp}. What is the molar solubility?')
        await ctx.send('Reply in format `submit <answer>`. Do not include units. Ex: `submit 3`. You have a 2% tolerance') 

        #checker method
        def check(msg):
            return msg.content.startswith('submit') and msg.author == ctx.author and msg.channel == ctx.channel

        #grab input and check for correctness
        try:
            msg = await self.bot.wait_for('message', timeout=120.0, check=check)
        except asyncio.TimeoutError:
            await ctx.send(f'Out of time! the correct answer is ||{salt.S}||')
        else:
            answer = float(msg.content.split()[1])
            if (abs(answer-salt.S) / salt.S * 100) <= 2:
                await ctx.send('Correct.')
                profile = self.bot.get_cog('profile')
                await profile.add_pts(str(ctx.author.id), 1)
            else:
                await ctx.send(f'Incorrect. The correct answer is {round(salt.S, 3)}.')

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
        await ctx.send(f'Is {Formula} soluble or insoluble?')
        await ctx.send('Reply in format `submit <answer>`. Your answer should be either \'soluble\' or \'insoluble\'') 

        #checker method
        def check(msg):
            return msg.content.startswith('submit') and msg.author == ctx.author and msg.channel == ctx.channel

        #grab input and check for correctness
        try:
            msg = await self.bot.wait_for('message', timeout=45.0, check=check)
        except asyncio.TimeoutError:
            if Formula_dict[Formula]:
                await ctx.send(f'Out of time! the correct answer is: ||True||')
            else:
                await ctx.send(f'Out of time! the correct answer is: ||False||')
        else:
            answer = msg.content.split()[1]
            if (answer == 'soluble' and answer) or (answer == 'insoluble' and not answer):
                await ctx.send('Correct.')
                profile = self.bot.get_cog('profile')
                await profile.add_pts(str(ctx.author.id), 1)
            else:
                await ctx.send('Incorrect.')


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