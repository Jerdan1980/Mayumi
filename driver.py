#for token input
import json
#for discord
import asyncio
import discord
from discord.ext import commands
#standard imports
import random

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
    print("Loaded!")

#ping command
@bot.command()
async def ping():
    await bot.say("pong!")

#roll command
#from sample bot
@bot.command()
async def roll(dice : str):
    #Rolls a dice in NdN format.
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await bot.say('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await bot.say(result)

#bot token
bot.run(tokens['discord'])