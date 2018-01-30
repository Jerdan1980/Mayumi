import discord
import asyncio

client = discord.Client()

@client.event
async def on_ready():
  print('reafy!')

@client.event
async def on_message(message):
  if message.content.startswith('ping'):
    await client.sendmessage(message.channel, 'pong!')

client.run(token)
