import discord
from discord.ext import commands
import ultimateRandomLibrary as r
import random
import os
import json

intents = discord.Intents.default()
intents.message_content = True
token = ""
with open("settings.json","r") as f:
    data = json.load()
    token = data["token"]
    f.close()
bot = commands.Bot(command_prefix="?",intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} is online!")
    if random.randint(0,100) > 50: 
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening,name=r.randomDadJoke()))
    else:
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing,name=r.randomWord(random.randint(1,10))))
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
@bot.command(description="Get a random Yo Mamma joke.",usage="?randomyomammajoke")
async def randomyomammajoke(ctx):
    await ctx.send(r.randomYoMammaJoke())
@bot.command(description="Get a random dad joke.",usage="?randomdadjoke")
async def randomdadjoke(ctx):
    await ctx.send(r.randomDadJoke())
@bot.command(description="Find a cure to your boredom by getting a random activity idea.",usage="?randomactivity")
async def randomactivity(ctx):
    await ctx.send(r.randomActivity())
@bot.command(description="Get a random fox image.",usage="?randomfoximg")
async def randomfoximg(ctx):
    await ctx.send(r.randomFoxImage())
@bot.command(description="Get a random dog image.",usage="?randomdogimg")
async def randomdogimg(ctx):
    await ctx.send(r.randomDogImage())
@bot.command(description="Get a random cat image.",usage="?randomcatimg")
async def randomcatimg(ctx):
    await ctx.send(r.randomCatImage())
@bot.command(description="Get a random duck image.",usage="?randomduckimg")
async def randomduckimg(ctx):
    await ctx.send(r.randomDuckImage())
@bot.command(description="Get a random raccoon image.",usage="?randomraccoonimg")
async def randomraccoonimg(ctx):
    await ctx.send(r.randomRaccoonImage())
@bot.command(description="Get a random cat fact.",usage="?randomcatfact")
async def randomcatfact(ctx):
    await ctx.send(r.randomCatFact())
@bot.command(description="Get a random dog fact.",usage="?randomdogfact")
async def randomdogfact(ctx):
    await ctx.send(r.randomDogFact())
@bot.command(description="Get a random coffee image.",usage="?randomcoffeeimg")
async def randomcoffeeimg(ctx):
    await ctx.send(r.randomCoffeeImage())
@bot.command(description="Get a random quote.",usage="?randomquote")
async def randomquote(ctx):
    await ctx.send(r.randomQuote())
@bot.command(description="Get a random number.",usage="?randomnumber")
async def randomnumber(ctx):
    await ctx.send(r.randomNumber())
@bot.command(description="Get a random git commit message.",usage="?randomcommitmessage")
async def randomcommitmessage(ctx):
    await ctx.send(r.randomCommitMessage())
@bot.command(description="Get a photo of a person who doesn't exist.",usage="?randompersonwhodoesntexist")
async def randompersonwhodoesntexist(ctx):
    file = open("randomperson.jpg","wb")
    file.write(r.randomPersonWhoDoesntExist())
    file.close()
    await ctx.send(file=discord.File("randomperson.jpg"))
    os.remove("randomperson.jpg")
@bot.command(description="Get a random identity.",usage="?randomidentity")
async def randomidentity(ctx):
    await ctx.send(r.randomPersonIdentity())
@bot.command(description="Get yes or no.",usage="?yesorno")
async def yesorno(ctx):
    await ctx.send(r.randomYesOrNo())
@bot.command(description="Get a random time in hour.",usage="?randomhour")
async def randomhour(ctx):
    await ctx.send(r.randomHour())
@bot.command(description="Get a random letter from English alphabet.",usage="?randomletter")
async def randomletter(ctx):
    await ctx.send(r.randomLetter())
@bot.command(description="Get a random country.",usage="?randomcountry")
async def randomcountry(ctx):
    await ctx.send(r.randomCountry())
@bot.command(description="Get a random region from seven regions.",usage="?randomregion")
async def randomregion(ctx):
    await ctx.send(r.randomRegion())
@bot.command(description="Get a random image.",usage="?randomimg")
async def randomimg(ctx):
    await ctx.send(r.randomImage())
@bot.command(description="Get a random colour.",usage="?randomcolour")
async def randomcolour(ctx,arg : str = "rgb"):
    await ctx.send(r.randomColour(arg))                                                                                                            
bot.run(token)            
