import asyncio, discord
from discord.ext import commands
import random, re

class misc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    #roll command
    @commands.command()
    async def roll(self, ctx, dice : str):
        #extracts rolling information
        try:
            if '+' in dice or '-' in dice:
                rolls, limit, modifier = map(int, re.split('d|\+|\-', dice))
                if '-' in dice:
                    modifier *= -1
            else:
                rolls, limit = map(int, dice.split('d'))
                modifier = 0
        except:
            await ctx.send('Format has to be in `NdN` or `NdN+N`!')
            return

        #rolls stuff
        nums = []
        for r in range(rolls):
            nums.append(random.randint(1, limit))
        total = 0
        for _, n in enumerate(nums):
            total += n
        total += modifier

        #format output
        result = "`"
        result += ' + '.join(str(n) for _, n in enumerate(nums))
        if not modifier == 0:
            if modifier > 0:
                result += ' + ' + str(modifier)
            else:
                result += ' - ' + str(modifier * -1)
        result += "`\n" + "Result: " + str(total)

        await ctx.send(result)

    #flip a coin command
    @commands.command()
    async def flip(self, ctx):
        flip = random.randint(0,1)
        if flip == 0:
            await ctx.send('Heads!')
        if flip == 1:
            await ctx.send('Tails!')
    
    #8ball command
    @commands.command(aliases=["8ball"])
    async def quest(self, ctx):
            answers = ["No way!",
                       "It is certain",
                       "Ask again later",
                       "It is decidedly so",
                       "Without a doubt",
                       "Yes, definitely",
                       "Sure whatever go ahead",
                       "Don't count on it",
                       "No way Jose",
                       "Outlook not good",
                       "You probably shouldn't, but it's not like I can stop you",
                       "I'm gonna go with a yes on that, but take that with a grain of salt",
                       "As if I care at all",
                       "I don't know, should you?",
                       "Obviouusly",
                       "No dip, Sherlock",
                       "What do you think?",
                       "Why are you asking me, an Internet bot?",
                       "Four score and seven years ago I said that was a VERY bad idea",
                       "Treat yo' self",
                       "No",
                       "Yes",
                       "Maybe",
                       "Definitely not"]
            random.shuffle(answers) #shuffle answers
            await ctx.send(answers[0]) #return first

def setup(bot):
    bot.add_cog(misc(bot))