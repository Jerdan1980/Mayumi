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
		async with aiohttp.request('GET', 'https://api.warframestat.us/pc') as r:
			if r.status == 200:
				body = await r.json()

				data = []
				data.append("Here are the worldstates:")
				data.append('**Earth:** {} for {}'.format(body['earthCycle']['state'], body['earthCycle']['timeLeft']))
				data.append('**Cetus:** {} for {}'.format(body['cetusCycle']['state'], body['cetusCycle']['state']))
				data.append('**Orb Vallis:** {} for {}'.format(body['vallisCycle']['state'], body['vallisCycle']['state']))

				await ctx.send('\n'.join(data))

def setup(bot):
	bot.add_cog(warframe(bot))