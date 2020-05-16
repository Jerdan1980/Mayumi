#discord imports
import asyncio, discord
from discord.ext import commands
#standard imports
import sys, traceback
import json

class profile_old(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        with open("profiles.json") as file:
            self.profiles = json.load(file)
        file.close()

    #update json
    async def updateProfiles(self):
        with open("profiles.json", 'w') as outfile:
            json.dump(self.profiles, outfile, indent=4)

    #points handling
    async def add_pts(self, author: str, pts: int):
        #check if user exists
        if author not in self.profiles:
            self.profiles[author] = 0
        #add pts and then save
        self.profiles[author] += pts
        await self.updateProfiles()

    async def sub_pts(self, author: str, pts: int):
        #check if user exists
        if author not in self.profiles:
            self.profiles[author] = 0
        #add pts and then save
        self.profiles[author] -= pts
        await self.updateProfiles()

    #profile command
    @commands.command()
    async def profile_old(self, ctx, query: str = ""):
        if query == "":
            author = str(ctx.author.id)
            #check if user exists
            if author not in self.profiles:
                self.profiles[author] = 0
                await self.updateProfiles()
            #output
            await ctx.send("You have " + str(self.profiles[author]) + " points")

        else:
            try:
                auth = ctx.message.mentions[0]
                #check if user exists
                if str(auth.id) not in self.profiles:
                    self.profiles[str(auth.id)] = 0
                    await self.updateProfiles()
                #output
                await ctx.send(f"**{auth.display_name}** has {str(self.profiles[str(auth.id)])} points")
            except Exception:
                    found = False
                    for mem in ctx.channel.guild.members:
                        if not found and ((query.lower() in mem.name.lower()) or (query.lower() in mem.display_name.lower())):
                            found = True
                            auth = mem
                    if found:
                        #check if user exists
                        if str(auth.id) not in self.profiles:
                            self.profiles[str(auth.id)] = 0
                            await self.updateProfiles()
                        #output
                        await ctx.send(f"**{auth.display_name}** has {str(self.profiles[str(auth.id)])} points")
                    else:
                        await ctx.send('Member not found!')

def setup(bot):
    bot.add_cog(profile_old(bot))