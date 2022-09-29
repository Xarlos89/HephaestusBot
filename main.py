import os
import discord
from discord import Member
from discord.ext import commands
from discord.ext.commands import Bot
import requests

intents = discord.Intents().all()
bot = Bot(command_prefix='>>', intents=intents, help_command=None)


@bot.event
async def on_ready():
	await bot.change_presence(activity = discord.Activity(type = discord.ActivityType.watching, name = 'you develop me.'))
	print('Up and running.')


@bot.slash_command(guild_ids=[900302240559018015], description="testing slash command")
async def checkslash(ctx):
	await ctx.respond(content="slash command works.")

@bot.command()
async def hi(ctx):
    await ctx.send("Oh, Hi there.")

@bot.command()
async def imbored(ctx):	
	data = requests.get('https://www.boredapi.com/api/activity/').json()
	activity = data["activity"]
	type = data["type"]
	participants = data["participants"]
	if data["price"] <0.5:
		price = 'and is not too expensive'
	else:
		price = 'and is a bit expensive'
	await ctx.send("I'm bored too, let's do this: " + activity + ". It's " + type + " and you could involve " + str(participants) + " people " + price)

if __name__ == "__main__":
	"""
  	This prevents replit from blocking us with too many requests.
	If the system gets req blocked, we kill the system and jump to a new IP
  	"""
	try:
		bot.run(os.environ["TOKEN"])
	except:
		os.system("kill 1")

