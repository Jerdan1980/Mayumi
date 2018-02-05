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

@client.event
async def on_ready():
  print('reafy!')

@client.event
async def on_message(message):
  if "mayumi" in message.content.lower():
    if "ping" in message.content.lower():
      await client.send_message(message.channel, 'pong!')
    elif "time" in message.content.lower():
      await client.send_message(message.channel, message.timestamp)
      
      
      
@client.event
async def on_message(message):    
  if "mayumi" in message.content.lower():
    elif "writing prompts" in message.content.lower():
      if"random" in message:
        await client.send_message(message.channel, file.open("Writing Prompts.txt").readlines()[random.rand(148)+1].split("|")[0])
      elif "humor" in message:
        await client.send_message(message.channel, file.open("Writing Prompts.txt").readlines()[humor.rand(148)+1].split("|")[0])
      elif "fantasy" in message
        await client.send_message(message.channel, file.open("Writing Prompts.txt").readlines()[humor.rand(148)+1].split("|")[0])
client.run(tokens['discord']) #insert way to find token here.
