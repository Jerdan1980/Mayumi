#for token input
import json
#standard imports
import random
#for discord
import asyncio
import discord


#import token file
with open('tokens.json') as file:
  tokens = json.load(file)
file.closed

#start of code discord implementation
client = discord.Client()

#upon startup of client
@client.event
async def on_ready():
  print('reafy!')

#Jeremy's code
@client.event
async def on_message(message):
  msg = message.content.lower()
  if "mayumi" in msg:
    #Jeremy's code
    if "ping" in msg:
      await client.send_message(message.channel, 'pong!')
    elif "time" in msg:
      await client.send_message(message.channel, message.timestamp)
    elif ("flip" in msg) and ("coin" in msg):
      coin = random.randint(0, 1)
      if coin == 0:
        await client.send_message(message.channel, 'heads')
      elif coin == 1:
        await client.send_message(message.channel, 'tails')
      else:
        await client.send_message(message.channel, 'something\'s wrong here')
    elif("8ball" in msg):
      #trover helped me with the next line!
      o = (lambda x:{None:x[0]}[random.shuffle(x)])(open("Resources\MayumiYesNo.txt", "r").read().split("\n"))
      await client.send_message(message.channel, o)
      
    #Anissa's code
    elif "writing prompts" in msg():
      if"random" in msg:
        await client.send_message(message.channel, file.open("Writing Prompts.txt").readlines()[random.randint(0, 148)].split("|")[0])
      elif "humor" in msg:
        await client.send_message(message.channel, file.open("Writing Prompts.txt").readlines()[random.randint(0, 148)].split("|")[0])
      elif "fantasy" in msg:
        await client.send_message(message.channel, file.open("Writing Prompts.txt").readlines()[random.randint(0, 148)].split("|")[0])

    #Lukas' code

client.run(tokens['discord']) #insert way to find token here.
