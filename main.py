
from discord.ext.commands import Bot
import discord
from collections import defaultdict
import os
import json



bot = Bot('!')

points = defaultdict(int)

@bot.event
async def on_ready():
    print("Hello! I'm ready...")



@bot.command(pass_context=True)
async def leaderboard(ctx):
  await ctx.send("This is the Good Noodle Board")
amounts = {}


#id? 
#how to access commands when using bot? 

#get balance
@bot.command(pass_context=True)
async def balance(ctx):
    id = str(ctx.message.author.id)
    if id in amounts:
        await ctx.send("You have {} Gold Stars!".format(amounts[id]))
    else:
        await ctx.send("Register your info")    

#Register new person 
#amounts[id] = 100? 

@bot.command(pass_context=True)
async def register(ctx):
    id = str(ctx.message.author.id)
    if id not in amounts.keys:
        amounts[id] = 100
        await ctx.send("You are now registered")
        _save()
    else:
        await ctx.send("You already have an account")

@bot.command(pass_context=True)
async def transfer(ctx, amount: int, other: discord.Member):
    primary_id = str(ctx.message.author.id)
    other_id = str(other.id)
    if primary_id not in amounts:
        await ctx.send("You do not have an account")
    else:
        amounts[primary_id] -= amount
        amounts[other_id] += amount
        await ctx.send("Transaction complete")
    _save()
    
#not really sure what this part does (json)
def _save():
    with open('amounts.json', 'w+') as f:
        json.dump(amounts, f)

@bot.command()
async def save():
    _save()


@bot.command(pass_context=True)
async def give(ctx, member: discord.Member):
    points[member.id] += 1
    bot.say("{} now has {} Gold Stars".format(member.mention, points[member.id]))


  


bot.run(os.getenv('TOKEN'))


