#standard imports
import sys, traceback
import json
import os
import aiohttp
#discord imports
import asyncio, discord
from discord.ext import commands
import discord.utils
import logging
from discord.ext.commands import CommandNotFound

#load config file
with open('config.json') as file:
	config = json.load(file)
file.close()

#dynamically load extensions
extensions = []
for root, directories, files in os.walk('./cogs'):
	#remove pycache
	directories[:] = [d for d in directories if d not in ['__pycache__']]
	#iterate
	[extensions.append('cogs.' + filename.split('.')[0]) for filename in files if filename.endswith('.py')]
	"""
	for filename in files:
		if filename.endswith('.py'):
			extensions.append('cogs.' + filename.split('.')[0])"""

#create bot
bot = commands.Bot(command_prefix=config['prefix'])

#load extensions when bot boots up
@bot.event
async def on_ready():
	print("Loading commands...")

	for ext in extensions:
		try:
			bot.load_extension(ext)
			print(f'\t{ext} loaded')
		except Exception as e:
			print(f'\tFailed to load extension {ext}', file=sys.stderr)
			traceback.print_exc()
		
	print("Done!")
	logging.basicConfig(level=logging.INFO)
	await bot.change_presence(activity=discord.Game(name=config["prefix"] + "help"))

#check owner
def is_owner_check(id):
	try:
		config['authors'].index(str(id))
		return True
	except ValueError as e:
		return False
def is_owner():
	return commands.check(lambda ctx: is_owner_check(ctx.message.author.id))

#reload ALL extensions
@bot.command(hidden=True)
@is_owner()
async def reload(ctx, *, ext=''):
	if(ext == ''):
		print("Reloading commands...")
		counter = 0
		total = 0
		for ext in extensions:
			try:
				bot.reload_extension(ext)
				print(f'\t{ext} loaded')
				counter += 1
			except Exception as e:
				print(f'\tFailed to load extension {ext}', file=sys.stderr)
				await ctx.send(f'Failed to load {ext}')
				traceback.print_exc()
			total += 1
		
		print("Done!")
		await ctx.send(f'{counter} out of {total} extensions loaded')
	else:
		print(f'Reloading {ext}...')
		try:
			bot.reload_extension(ext)
			print(f'\t{ext} loaded')
			await(ctx.send(f'{ext} loaded!'))
		except Exception as e:
			print(f'\tFailed to load extension {ext}', file=sys.stderr)
			await ctx.send(f'Failed to load extension {ext}')
		
		print("Done!")

#end this man's whole career
@bot.command(hidden=True)
@is_owner()
async def stop(ctx):
	await ctx.send('Logging out!')
	await bot.logout()

#command not found listener
@bot.event
async def on_command_error(ctx, error):
	if isinstance(error, CommandNotFound):
		await ctx.send("Command does not exist! Maybe you made a typo?")
		return
	raise error

#start bot
bot.run(config['discord'])