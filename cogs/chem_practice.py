#discord imports
import asyncio, discord
from discord.ext import commands
#standard imports
import random

#class holding questions
class chem_practice(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
        #list of ksp
        self.Ksp_list = []
        with open('Ksp.txt', 'r') as f:
            for line in f:
                line = line.split(',')
                self.Ksp_list.append(Ksp(line[0], line[1], line[2], line[3]))
        file.close()


    #molar solubility
    @commands.command()
    async def molar_solubility(self, ctx):
        #shuffle the list to get a random Ksp
        salt = random.shuffle(self.Ksp_list)[0]
        
        #ask the question
        await ctx.send('You have {salt.name} with Ksp {salt.Ksp}. What is the molar solubility?')
        await ctx.send('Reply in format `submit <answer>`. Do not include units. Ex: `submit 3`. You have a 2% tolerance') 

        #checker method
        def check(msg, user):
            return msg.content.startswith('submit') and user == ctx.author:

        #grab input and check for correctness
        try:
            msg = await ctx.wait_for('message', Timeout=120.0, check=check)
        except asyncio.TimeoutError:
            await ctx.send(f'Out of time! the correct answer is ||{salt.S}||')
        else:
            answer = msg.content.split()[1]
            if (abs(answer-salt.S) / salt.S * 100) <= 2:
                await ctx.send('Correct.')
                profile = self.bot.get_cog('profile')
                await profile.add_pts(str(ctx.author.id), 1)
            else:
                await ctx.send(f'Incorrect. The correct answer is {salt.S}.')

    #solubility rules
    @commands.command()
    async def solublitiy_rules(self, ctx):
        #dict of solubilities
        with open('solubility.json' as f:
            Formula_dict = json.load(f)
        f.close()        

        #shuffle the dict to get a random key
        Formula = random.shuffle(Formula_dict)[0]
        
        #ask the question
        await ctx.send(f'Is {Formula} soluble or insoluble?')
        await ctx.send('Reply in format `submit <answer>`. Your answer should be either \'soluble\' or \'insoluble\'') 

        #checker method
        def check(msg, user):
            return msg.content.startswith('submit') and user == ctx.author:

        #grab input and check for correctness
        try:
            msg = await ctx.wait_for('message', Timeout=45.0, check=check)
        except asyncio.TimeoutError:
            await ctx.send(f'Out of time! the correct answer is ||{Formula_dict[Formula]}||')
        else:
            answer = msg.content.split()[1]
		    if (ans == 'soluble' and answer) or (ans == 'insoluble' and not answer):
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
        self.name = name
        self.Ksp = Ksp_val
        self.x = x
        self.y = y
        self.S = pow(Ka/(pow(y,y) * pow(x,x)),1/(x+y))