import discord
from discord.ext import commands

intents = discord.Intents.all()
intents.members = True

bot = commands.Bot(command_prefix='/', intents=intents)


def event_apply(bot):
    @bot.event
    async def on_ready():
        await bot.get_channel(1010897174130855989).send(f"heyy @everyone, I'm online!")

    @bot.event
    async def on_message(message):
        if message.author == bot.user:
            return
        if message.content.lower() == 'hi':
            await message.channel.send(f'hi {message.author.mention}')

    @bot.event
    async def on_member_join(member):
        await member.guild.owner.send(f'{member} has joined the server at {member.joined_at}')
        welcome_channel = bot.get_channel(1014535045270208562)
        await welcome_channel.send(f'Welcome to the server {member.mention}!')

    @bot.event
    async def on_member_leave(member):
        await member.guild.owner.send(f'{member} has left the server at {member.leave_at}')
        welcome_channel = bot.get_channel(1014535045270208562)
        await welcome_channel.send(f'goodbye {member.name}!')
