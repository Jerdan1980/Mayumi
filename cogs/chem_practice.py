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

        #list of acids
        alist = []
        with open('resources/polyacids.txt', 'r') as f:
            for line in f:
                line = line.split(',')
                alist.append(pH(line[0], 1, line[1], line[2], line[3]))
        f.close()
        self.acid_list = alist


    #randomizer
    @commands.command()
    async def quiz(self, ctx):
        pick = random.randrange(0, 3)
        if pick == 0:
            await self.molsol(ctx)
        elif pick == 1:
            await self.solrules(ctx)
        elif pick == 2:
            await self.polyacids(ctx)

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

    #polyprotic acids
    async def polyacids(self, ctx):
        #shuffle the list to get a random acid
        random.shuffle(self.acids_list)
        acid = self.acids_list[0]

        #randomize the question
        pick_K = bool(random.getrandbits(1))
        pick_pH = random.choice(["pH", "pOH"])

        #print out the question
        if pick_K:
            await.ctx.send(f'A solution of {acid.name} has a Ka1 of {acid.Ka1} and the Ka2 of {acid.Ka2}. What is the {pick_pH}? Assume the question does not require the use of the quadratic formula.')
        elif not pick_K:
            await.ctx.send(f'A solution of {acid.name} has a Kb1 of {acid.Kb1} and the Kb2 of {acid.Kb2}. What is the {pick.pH}? Assume the question does not require the use of the quadratic formula.')
        await.ctx.send('Reply in format `submit <answer>`. Do not include units. Ex: `submit 3`. You have a 2% tolerance')
        
        #checker method
        def check(msg):
            return msg.content.startswith('submit') and msg.author == ctx.author and msg.channel == ctx.channel

        #check if it's right
        try:
            msg = await self.bot.wait_for('message', Timeout=600.0, check=check)
        except asyncio.TimeoutError:
            await ctx.send(f'Out of time! the correct answer is {pH}')
        else: 
            answer = double(msg.content.split()[1])
            if pick_pH and (abs(answer-acid.pH) / acid.pH * 100) <= 2:
                await ctx.send('Correct.')
                profile = self.bot.get_cog('profile')
                await profile.add_pts(str(ctx.author.id), 1)
            elif not pick_pH and (abs(answer-acid.pOH) / acid.pH * 100) <= 2:
                await ctx.send('Correct.')
                profile = self.bot.get_cog('profile')
                await profile.add_pts(str(ctx.author.id), 1)
            else:
                await ctx.send(f'Incorrect. The correct answer is {acid.pH}')


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
            self.Ka1 = K1
            self.Ka2 = K2
            self.Kb1 = 1e-14 / self.Ka1
            self.Kb2 = 1e-14 / self.Ka2
            self.pH = -log(pow(K1 * K2, 0.5 ))
            self.pOH = 14 - self.pH
        elif not self.is_acid:
            self.Kb1 = K1
            self.Kb2 = K2
            self.Ka1 = 1e-14 / self.Kb1
            self.Ka2 = 1e-14 / self.Kb2
            self.pOH = -log(pow(K1 * K2, 0.5 ))
            self.pH = 14 - self.pOH
