import discord
from discord.ext import commands
import ultimateRandomLibrary as r
import random

intents = discord.Intents.default()
intents.message_content = True
token = ""
bot = commands.Bot(command_prefix="?",intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} is online!")
    if random.randint(0,100) > 50: 
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening,name=r.randomDadJoke()))
    else:
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing,name=r.randomWord(random.randint(1,30))))
@bot.command(description="Get random words.",usage="?randomword <(optional) number> <(optional) language>")
async def randomword(ctx,arg: int = 1,arg1: str = "en"):
    message = r.randomWord(arg,arg1)
    await ctx.send(message)
@bot.command(description="Get a random joke.",usage="?randomjoke <(optional) language>")
async def randomjoke(ctx,arg: str = "en"):
    message = r.randomJoke(arg)
    await ctx.send(message)
@bot.command(description="Get a random fun fact.",usage="?randomfact <(optional) language>")
async def randomfact(ctx,arg: str = "en"):
    message = r.randomFunFact(arg)
    await ctx.send(message)
@bot.command(description="Get a random techy quote.",usage="?randomtechyquote")
async def randomtechyquote(ctx):
    await ctx.send(r.randomTechyQuote())
@bot.command(description="Get a random Chuck Norris joke.",usage="?randomchucknorrisjoke")
async def randomchucknorrisjoke(ctx):
    await ctx.send(r.randomChuckNorrisJoke())
@bot.command(description="Get a random excuse.",usage="?randomexcuse")
async def randomexcuse(ctx):
    await ctx.send(r.randomExcuse())                
bot.run(token)            
