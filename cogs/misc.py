import asyncio, discord
from discord.ext import commands
import random

class misc(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
	
	#flip a coin command
	@commands.command()
	async def flip(self, ctx):
		flip = random.randint(0,1)
		if flip == 0:
			await ctx.send('Heads!')
		if flip == 1:
			await ctx.send('Tails!')

	#ping command
	@commands.command()
	async def ping(self, ctx):
		await ctx.send("pong!")

	#send pfp
	@commands.command(aliases=['pfp'])
	async def avatar(self, ctx):
		await ctx.send(file=discord.File("Mayumi pfp.png"))

def setup(bot):
	bot.add_cog(misc(bot))