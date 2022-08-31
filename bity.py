import discord
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='/', intents=intents)


@bot.event
async def on_ready():
    print('\t\t-----------------')
    print(f"{bot.user}: I'm online")


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content.lower() == 'hi':
        await message.channel.send(f'hi {message.author.mention}')

@bot.command()
async def infos(ctx):
    await ctx.send(f'total of the members: {len(ctx.guild.users)}')

from TokenFile import TOKEN
bot.run(TOKEN)
