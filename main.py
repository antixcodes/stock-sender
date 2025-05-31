import os
import discord
from discord.ext import commands, tasks

tkn = ""

###############################
CHANNEL_ID = 12912498235813534 # put your stock sender id
###############################


bot = commands.Bot(command_prefix='.', self_bot=True, help_command=None)

def idk():
    with open('stock.txt', 'r') as file:
        return '\n'.join(line.strip() for line in file.readlines())
    
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    send_message.start()

@tasks.loop(minutes=15)
async def send_message():
    channel = bot.get_channel(CHANNEL_ID)
    if channel is not None:
        message = idk()
        await channel.send(message)

@send_message.before_loop
async def before_send_message():
    await bot.wait_until_ready()

bot.run(tkn)