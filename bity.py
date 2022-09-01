import discord
from discord.ext import commands
from events import event_apply
from commands import command_apply


intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='/', intents=intents)


command_apply(bot)
event_apply(bot)

from TokenFile import TOKEN

bot.run(TOKEN)
