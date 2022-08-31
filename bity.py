import discord
from discord.ext import commands

intents = discord.Intents.all()

bity = commands.Bot(command_prefix='/', intents=intents)


@bity.event
async def on_ready():
    print('\t\t-----------------')
    print(f"{bity.user}: I'm online")

@bity.event()
async def on_message(message):
    if message.author == bity.user:
        return
    if message.lower() == 'hi':
        await message.channel.send(f'hi {message.author.mention}')

from TokenFile import TOKEN
bity.run(TOKEN)