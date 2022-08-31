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

import os

bity.run('MTAxMjM0NzE3ODQzNTQ4MTY0MA.Ggiijj.QLTEMzvuTlwB5DcZlRolploNb5BVveL5IebXVI')