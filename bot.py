import discord
from discord.ext import commands, tasks
import random

intents = discord.Intents.default()
intents.guilds = True
intents.members = True
intents.messages = True

bot = commands.Bot(command_prefix='!', intents=intents)

statuses = ["Ekipa Milonowic", "PlanetHC.pl", "MiłoszFF STYLE", "MiłoszFF Minecraft"]

@bot.event
async def on_ready():
    change_status.start()
    print('Bot is ready!')

@tasks.loop(seconds=20)  # Zmiana statusu co 60 sekund
async def change_status():
    new_status = random.choice(statuses)
    await bot.change_presence(activity=discord.Game(name=new_status))

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(1149237443577520170)  # ID kanału powitalnego
    if channel:
        await channel.send(f"Hej {member.mention}, witaj na naszym serwerze Ekipa MiłoszaFF!")
        await channel.send(member.avatar_url)  # Wysyła avatar użytkownika

bot.run('OTY3NzY4MzM0MjU2OTkyMjU2.GB-9nM.o8YcryT9c2mgAyw6e5zSUq98juBTjSqeEK00Fw') # Tutaj wstaw swój token bota Discord
