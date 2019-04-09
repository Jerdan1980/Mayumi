import discord
import asyncio
import random

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.content.startswith('|test'):
        counter = 0
        tmp = await client.send_message(message.channel, 'Calculating messages...')
        async for log in client.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1
        await client.edit_message(tmp, 'You have {} messages.'.format(counter))

    elif message.content.startswith('|coin'):
        await client.send_message(message.channel, 'heads or tails?')
        def check(msg):
            return msg.content.startswith('heads') or msg.content.startswith('tails')
        msg = await client.wait_for_message(author=message.author, channel=message.channel, check=check)
        coin = random.randint(0,1)
        if msg.content == 'heads' and coin == 1:
            await client.send_message(message.channel, 'you win!')
        elif msg.content == 'tails' and coin == 0:
            await client.send_message(message.channel, 'you win!')
        else:
            await client.send_message(message.channel, 'you lose...')

    
    elif message.content.startswith('|dm'): #for testing dms
        await client.send_message(message.author, 'hello~')
        def check(msg):
            return True
        msg = await client.wait_for_message(author=message.author, check=check)
        if message.author.nick is None:
            nam = message.author.name
        else:
            nam = message.author.nick
        await client.send_message(message.channel, '{} said \"{}\"'.format(nam, msg.content))

    elif message.content.startswith('|rps start'):
        #starts the match
        await client.send_message(message.channel, 'type `|rps join` to join match')
        plr1msg = await client.wait_for_message(channel=message.channel, content='|rps join')
        await client.send_message(message.channel, plr1msg.author.name + " has joined, 1 more player left")
        plr2msg = await client.wait_for_message(channel=message.channel, content='|rps join')
        await client.send_message(message.channel, plr2msg.author.name + ' has joined, game starting!')
        #the match
        await client.send_message(plr1msg.author, 'type `rock`, `paper`, or `scissors`')
        await client.send_message(plr2msg.author, 'type `rock`, `paper`, or `scissors`')
        def check(msg):
            return msg.content.startswith('rock') or msg.content.startswith('paper') or msg.content.startswith('scissors')
        msg1 = await client.wait_for_message(author=plr1msg.author, check=check)
        await client.send_message(plr1msg.author, 'recieved!')
        msg2 = await client.wait_for_message(author=plr2msg.author, check=check)
        await client.send_message(plr2msg.author, 'recieved!')
        #the winner
        p1 = msg1.content
        p2 = msg2.content
        await client.send_message(message.channel, 'player 1: `' + p1 + '`\n player 2: `' + p2)
        if p1 == p2:
            await client.send_message(message.channel, 'no winner')
        elif p1 == 'rock' and p2 == 'paper':
            await client.send_message(message.channel, plr2msg.author.nick + ' wins the match!')
        elif p1 == 'rock' and p2 == 'scissors':
            await client.send_message(message.channel, plr1msg.author.nick + ' wins the match!')
        elif p1 == 'paper' and p2 == 'rock':
            await client.send_message(message.channel, plr1msg.author.nick + ' wins the match!')
        elif p1 == 'paper' and p2 == 'scissors':
            await client.send_message(message.channel, plr2msg.author.nick + ' wins the match!')
        elif p1 == 'scissors' and p2 == 'paper':
            await client.send_message(message.channel, plr1msg.author.nick + ' wins the match!')
        elif p1 == 'scissors' and p2 == 'rock':
            await client.send_message(message.channel, plr2msg.author.nick + ' wins the match!')
        else:
            await client.send_message(message.channel, 'error')
        

client.run('MzI3MjU1MDg4NDc5NDY5NTY4.Dg1mow.uxii69OQNaP-7Rj5LHJMWnA0c6k')