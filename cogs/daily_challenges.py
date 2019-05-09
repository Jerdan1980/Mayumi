#discord imports
import asyncio, discord
from discord.ext import commands

#class for holding challenges
class challenge:
    def __init__(self, guildID: int, qtype: bool, pts: int, answer, err: float = 0):
        self.guild = guildID
        self.MC = qtype
        self.pts = pts
        self.submitters = []
        if qtype:
            self.ans = str(answer)
            self.err = 0
        else:
            self.ans = answer
            self.err = 0
    
    def checkAnswer(self, query):
        if self.MC:
            return self.ans.lower() == query.lower()
        else:
            return abs(query - self.ans) <= self.err

#cogs
class daily_challenges(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.challenges = []
    
    #create a daily challenge
    @commands.group(pass_context=True)
    async def create(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send("No subcommand passed")
    
    @create.command()
    async def mc(self, ctx, pts: int, ans: str):
        self.challenges.append(challenge(ctx.guild.id, True, pts, ans))
    
    @create.command()
    async def frq(self, ctx, pts: int, ans: float, err: float):
        self.challenges.append(challenge(ctx.guild.id, False, pts, ans, err))


    #submit command
    @commands.command()
    async def submit(self, ctx, submission):
        #look for challenge
        found = False
        counter = 0
        for c in self.challenges:
            if not found and ctx.guild.id == c.guild:
                found = True
            else:
                counter += 1
        
        #tell user no challenge exists
        if not found:
            await ctx.message.delete()
            await ctx.author.send("No challenge available")
        #check to see if user already submitted answer
        elif ctx.author.id in self.challenges[counter].submitters:
            await ctx.message.delete()
            await ctx.author.send("You already submitted an answer")
        #submit answer
        else:
            #let user know that the bot recieved the submission
            await ctx.message.delete()
            await ctx.author.send("Submission recieved!")

            #check for answer and update profile
            correct = self.challenges[counter].checkAnswer(submission)
            if correct:
                profile = self.bot.get_cog('profile')
                if profile is not None:
                    await profile.add_pts(str(ctx.author.id), self.challenges[counter].pts)
                

def setup(bot):
    bot.add_cog(daily_challenges(bot))