#discord imports
import asyncio, discord
from discord.ext import commands

class tester(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    #ping command
    @commands.command()
    async def ping(self, ctx):
        await ctx.send("pong!")

    #send pfp
    @commands.command()
    async def pfp(self, ctx):
        await ctx.send(file=discord.File("Mayumi pfp.png"))

    #send guild
    @commands.command()
    async def guild(self, ctx):
        await ctx.send(f'ctx.guild {ctx.guild.id} is of type {type(ctx.guild.id)}')

    #delete the message
    @commands.command()
    async def delete(self, ctx):
        await ctx.message.delete()

    #dms
    @commands.command()
    async def dm(self, ctx, message: str):
        await ctx.author.send(message)

    #pesudo-overload
    @commands.command()
    async def inchk(self, ctx, query: str = ""):
        if query == "":
            await ctx.send('Empty string sent.')
        else:
            try:
                auth = ctx.message.mentions[0]
                await ctx.send(f'User: {auth.name}')
            except Exception:
                try:
                    role = ctx.message.role_mentions[0]
                    await ctx.send(f'Role: {role.name}')
                except Exception:
                    await ctx.send("could not parse string")

    #member checker
    @commands.command()
    async def memchk(self, ctx, query: str = ""):
        if query == "":
            await ctx.send("you!")
        else:
            try:
                auth = ctx.message.mentions[0]
                await ctx.send(f'User: {auth.name}')
            except Exception:
                    found = False
                    for mem in ctx.channel.guild.members:
                        if not found and ((query.lower() in mem.name.lower()) or (query.lower() in mem.display_name.lower())):
                            found = True
                            auth = mem
                    if found:
                        await ctx.send(f'User: {auth.name}')
                    else:
                        await ctx.send('Member not found!')
    
    #role checker
    @commands.command()
    async def rolechk(self, ctx, query: str = ""):
        if query == "":
            await ctx.send("No role selected!")
        else:
            try:
                auth = ctx.message.role_mentions[0]
                await ctx.send(f'Role: {auth.name}')
            except Exception:
                    found = False
                    for r in ctx.channel.guild.roles:
                        if not found and (query.lower() in r.name.lower()):
                            found = True
                            auth = r
                    if found:
                        await ctx.send(f'Role: {auth.name}')
                    else:
                        await ctx.send('Member not found!')

def setup(bot):
    bot.add_cog(tester(bot))