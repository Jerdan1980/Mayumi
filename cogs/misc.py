import asyncio, discord
from discord.ext import commands
import random, re

class misc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    #ping command
    @commands.command()
    async def ping(self, ctx):
        await ctx.send("pong!")

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

def setup(bot):
    bot.add_cog(misc(bot))