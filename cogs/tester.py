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

def setup(bot):
    bot.add_cog(tester(bot))