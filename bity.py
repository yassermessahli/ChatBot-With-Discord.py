import discord
from discord.ext import commands
from events import event_apply
from commands import command_apply

intents = discord.Intents.all()
intents.members = True

bot = commands.Bot(command_prefix='/', intents=intents)


event_apply(bot)
command_apply(bot)



from TokenFile import TOKEN

bot.run(TOKEN)
