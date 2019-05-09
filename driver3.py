#for token input
import json
#for discord
import asyncio
import discord
from discord.ext import commands
import discord.utils
import logging
#standard imports
import random
import re
#rdkit imports
from rdkit.Chem import AllChem as Chem
from rdkit.Chem import Draw

#check owner
def is_owner_check(message):
    return message.author.id == tokens['author ID']
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
    logging.basicConfig(level=logging.INFO)
    await bot.change_presence(activity=discord.Game(name=tokens["prefix"] + "help"))

#end this man's whole career
@bot.command(hidden=True)
@is_owner()
async def stop(message):
    await bot.logout()

#ping command
@bot.command()
async def ping(message):
    await message.channel.send("pong!")

#roll command
@bot.command()
async def roll(ctx, dice : str):
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
        await ctx.send('Format has to be in `NdN` or `NdN+N`!')
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

    await ctx.send(result)

#send pfp
@bot.command()
async def pfp(message):
    await message.channel.send(file=discord.File("./Mayumi pfp.png"))

#chemdraw command
@bot.command()
async def chemdraw(ctx, smiles : str):
	#attempt generating mol
	mol = Chem.MolFromSmiles(smiles)

	#send file
	if(mol is None):
		await ctx.send("Invalid SMILES.")
	else:
		Chem.Computer2DCoords(mol)
		Draw.MolToFile(mol, 'images/chemdraw.png')
		await ctx.send(file=discord.File("images/chemdraw.png"))

#profile command
@bot.command()
async def profile(ctx):
	author = str(ctx.author.id)
	#import json file
	with open("./profiles.json") as file:
		profiles = json.load(file)
	file.close()
	#check if user exists
	if author not in profiles:
		await ctx.send("you dont have a profile yet")
		profiles[author] = 0
		with open("profiles.json", 'w') as outfile:
			json.dump(profiles, outfile)
	#output
	await ctx.send("You have: " + str(profiles[author]) + " points")

#bot token
bot.run(tokens['discord'])
