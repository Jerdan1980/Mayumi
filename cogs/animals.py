import asyncio, discord
from discord.ext import commands
import aiohttp

class animals(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def duck(self, ctx, num=''):
		async with ctx.typing():
			if num == '':
				async with aiohttp.request('GET', 'https://random-d.uk/api/random') as res:
					body = await res.json()

					embed = discord.Embed(title='Random duck!')
					embed.set_image(url=body['url'])
					embed.set_footer(text=body['message'])
					
					await ctx.send(embed=embed)
			else:
				embed = discord.Embed(title='Duck #{}!'.format(num))
				embed.set_image(url='https://random-d.uk/api/{}.jpg'.format(num))
				embed.set_footer(text='Powered by random-d.uk')

				await ctx.send(embed=embed)

	@commands.command()
	async def cat(self, ctx):
		async with ctx.typing():
			async with aiohttp.request('GET', 'https://aws.random.cat/meow') as res:
				body = await res.json()

				embed = discord.Embed(title='Random cat!')
				embed.set_image(url=body['file'])
				embed.set_footer(text='Powered by aws.random.cat')

				await ctx.send(embed=embed)
	
	@commands.command()
	async def dog(self, ctx):
		async with ctx.typing():
			async with aiohttp.request('GET', 'https://random.dog/woof.json') as res:
				body = await res.json()

				embed = discord.Embed(title='Random dog!')
				embed.set_image(url=body['url'])
				embed.set_footer(text='Powered by random.dog')

				await ctx.send(embed=embed)

def setup(bot):
	bot.add_cog(animals(bot))