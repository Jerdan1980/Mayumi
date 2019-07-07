#discord imports
import asyncio, discord
from discord.ext import commands
#standard imports
import random
import json
import math

#class holding questions
class equilibrium(commands.Cog):
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
    async def rando(self, ctx, question):
        if question == -1:
            question = random.randrange(0,1)

        if question == 0:
            await self.molsol(ctx)
    
    #molar solubility
    async def molsol(self, ctx):
        #shuffle the list to get a random Ksp
        random.shuffle(self.Ksp_list)
        salt = self.Ksp_list[0]

        #ask the question
        quest = f'Question for **{ctx.author.display_name}**. (1 point)\n'
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
    
def setup(bot):
    bot.add_cog(equilibrium(bot))

#class for Ksp
class Ksp():
    def __init__(self, name_of_salt, Ksp_val, x, y):
        self.name = name_of_salt
        self.Ksp = float(Ksp_val)
        self.x = int(x)
        self.y = int(y)
        self.S = pow(self.Ksp / (pow(self.y, self.y) * pow(self.x, self.x)), 1.0 / (self.x + self.y))