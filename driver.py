#for token input
import json
#for discord
import asyncio
import discord
from discord.ext import commands
import discord.utils
#standard imports
import random
import re

#check owner
def is_owner_check(message):
    return message.author.id == '262425476822204421'
def is_owner():
    return commands.check(lambda ctx: is_owner_check(ctx.message))

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
    await bot.change_presence(game=discord.Game(name=tokens["prefix"] + "help"))

#end this man's whole career
@bot.command(hidden=True)
@is_owner()
async def stop():
    await bot.logout()

#ping command
@bot.command()
async def ping():
    await bot.say("pong!")

#roll command
@bot.command()
async def roll(dice : str):
    #extracts rolling information
    try:
        if '+' in dice or '-' in dice:
            rolls, limit, modifier = map(int, re.split('d|\+|\-', dice))
            if '-' in dice:
                modifier *= -1
        else:
            rolls, limit = map(int, dice.split('d'))
            modifier = 0
    except:
        await bot.say('Format has to be in `NdN` or `NdN+N`!')
        return

    #rolls stuff
    nums = []
    for r in range(rolls):
        nums.append(random.randint(1, limit))
    total = 0
    for _, n in enumerate(nums):
        total += n
    total += modifier

    #format output
    result = "`"
    result += ' + '.join(str(n) for _, n in enumerate(nums))
    if not modifier == 0:
        if modifier > 0:
            result += ' + ' + str(modifier)
        else:
            result += ' - ' + str(modifier * -1)
    result += "`\n" + "Result: " + str(total)

    await bot.say(result)

#bot token
bot.run(tokens['discord'])