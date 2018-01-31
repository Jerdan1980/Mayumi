import discord
import asyncio

client = discord.Client()

@client.event
async def on_ready():
  print('reafy!')

@client.event
async def on_message(message):
  if "mayumi" in message.content.toLower():
    if "ping" in message.content:
      await client.sendmessage(message.channel, 'pong!')

client.run(token) #insert way to find token here.
