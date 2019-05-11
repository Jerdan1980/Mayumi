#discord imports
import asyncio, discord
from discord.ext import commands
#standard imports
import sys, traceback
import json

class profile(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        with open("profiles.json") as file:
            self.profiles = json.load(file)
        file.close()

    #update json
    async def updateProfiles(self):
        with open("profiles.json", 'w') as outfile:
            json.dump(self.profiles, outfile)

    #points handling
    async def add_pts(self, author: str, pts: int):
        #check if user exists
        if author not in self.profiles:
            self.profiles[author] = 0
        #add pts and then save
        self.profiles[author] += pts
        await updateProfiles()

    async def sub_pts(self, author: str, pts: int):
        #check if user exists
        if author not in self.profiles:
            self.profiles[author] = 0
        #add pts and then save
        self.profiles[author] -= pts
        await updateProfiles()

    #profile command
    @commands.command()
    async def profile(self, ctx):
        author = str(ctx.author.id)
        #check if user exists
        if author not in self.profiles:
            self.profiles[author] = 0
            await updateProfiles()
        #output
        await ctx.send("You have " + str(self.profiles[author]) + " points")

def setup(bot):
    bot.add_cog(profile(bot))