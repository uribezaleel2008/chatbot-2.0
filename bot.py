import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 1000):
    await ctx.send("he" * count_heh)

@bot.command()
async def saludar(ctx, *, nombre=""):
    if nombre!="":
        await ctx.send(f"hola ,{nombre}, como estas?")
    else:
        await ctx.send(f"hola, {ctx.autor.name}")

bot.run("MTI2OTM1ODYwMjkwOTUxNTg0Nw.G2WmQJ.efuvA_vsQfv54f7WGy6f2-R8iQMJGzIWe9fUz4")
