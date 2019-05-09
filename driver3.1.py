#standard imports
import sys, traceback
import json
#for discord
import asyncio, discord
from discord.ext import commands
import discord.utils
import logging

extensions = (
    'cogs.misc',
    'cogs.profile',
    'cogs.chem',
    'cogs.daily_challenges',
    'cogs.tester'
)

#load tokens
filePath = input("token json filepath: ")
with open(filePath) as file:
    tokens = json.load(file)
file.close()

#create discord bot
bot = commands.Bot(command_prefix=tokens['prefix'])
#start bot
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
    await bot.change_presence(activity=discord.Game(name=tokens["prefix"] + "help"))

#check owner
def is_owner_check(message):
    return message.author.id == tokens['author ID']
def is_owner():
    return commands.check(lambda ctx: is_owner_check(ctx.message))

#reload extensions
@bot.command(hidden=True)
@is_owner()
async def reload(ctx):
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

    
#end this man's whole career
@bot.command(hidden=True)
@is_owner()
async def stop(ctx):
    await bot.logout()

#bot token
bot.run(tokens['discord'])
