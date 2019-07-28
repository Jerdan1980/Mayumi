#standard imports
import sys, traceback
import json
#for discord
import asyncio, discord
from discord.ext import commands
import discord.utils
import logging

extensions = open('loader.txt').read().splitlines()

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
    
#end this man's whole career
@bot.command(hidden=True)
async def stop(ctx):
    if ctx.author.id == tokens['author ID']:
        await ctx.send('Logging out!')
        await bot.logout()
    else:
        await ctx.send("You can't tell me what to do!")

#bot token
bot.run(tokens['discord'])
