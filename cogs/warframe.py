import asyncio, discord
from discord.ext import commands
import aiohttp

class warframe(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
	
	#make group
	@commands.group(aliases=['wf'], pass_context=True)
	async def warframe(self, ctx):
		if ctx.invoked_subcommand is None:
			await ctx.send('No subcommand passed!')

	@warframe.command()
	async def time(self, ctx):
		async with ctx.typing():
			async with aiohttp.request('GET', 'https://api.warframestat.us/pc') as res:
				if res.status == 200:
					body = await res.json()

					data = []
					data.append("Here are the worldstates:")
					data.append('**Earth:** {} for {}'.format(body['earthCycle']['state'], body['earthCycle']['timeLeft']))
					data.append('**Cetus:** {} for {}'.format(body['cetusCycle']['state'], body['cetusCycle']['state']))
					data.append('**Orb Vallis:** {} for {}'.format(body['vallisCycle']['state'], body['vallisCycle']['state']))

					await ctx.send('\n'.join(data))
	
	@warframe.command()
	async def baro(self, ctx):
		async with ctx.typing():
			async with aiohttp.request('GET', 'https://api.warframestat.us/pc') as res:
				if res.status == 200:
					body = await res.json()
					body = body['voidTrader']

					if not body['active']:
						await ctx.send('Baro arriving in {}'.format(body['startString']))
					else:
						data = []
						data.append("**Baro's inventory:**")
						for item in body['inventory']:
							data.append('__{}__ {} ducats and {}k credits'.format(item['item'], item['ducats'], item['credits'] / 1000))
						data.append('__Leaving in {}~__'.format(body['endString']))

						await ctx.send('\n'.join(data))
	
	@warframe.command()
	async def nightwave(self, ctx):
		async with ctx.typing():
			async with aiohttp.request('GET', 'https://api.warframestat.us/pc') as res:
				if res.status == 200:
					body = await res.json()
					body = body['nightwave']

					if body['active']:
						embed = discord.Embed(title="Today's Nightwave")
						for challenge in body['activeChallenges']:
							embed.add_field(name='**{}**: {}, {}'.format(challenge['title'], "Daily" if 'isDaily' in challenge.keys() and challenge['isDaily'] else "Weekly", challenge['reputation']), value=challenge['desc'])

						await ctx.send(embed=embed)
					else:
						await ctx.send("Nightwave is not active currently.")
	
	@warframe.command()
	async def sortie(self, ctx, full=''):
		async with ctx.typing():
			async with aiohttp.request('GET', 'https://api.warframestat.us/pc') as res:
				if res.status == 200:
					body = await res.json()
					body = body['sortie']['variants']

					if full.lower() == 'full':
						embed = discord.Embed(title="Today's sortie")
						for i in [0, 1, 2]:
							embed.add_field(name='Mission {}: **{}**'.format(i, body[i]['missionType']), value='{}, {}'.format(body[i]['node'], body[i]['modifier']))

						await ctx.send(embed=embed)
					else:
						await ctx.send("Today's sortie: {}, {}, {}".format(body[0]['missionType'], body[1]['missionType'], body[2]['missionType']))

	@warframe.command(aliases=['rj'])
	async def railjack(self, ctx):
		async with ctx.typing():
			async with aiohttp.request('GET', 'https://api.warframestat.us/pc') as res:
				if res.status == 200:
					body = await res.json()
					body = body['sentientOutposts']

					if body['active']:
						await ctx.send('Sentient outpost at **{}**'.format(body['mission']['node']))
					else:
						await ctx.send("No sentient outposts active")

def setup(bot):
	bot.add_cog(warframe(bot))