from discord.ext.commands import Bot
from discord.ext import commands
import discord
import os

intents = discord.Intents.default()
bot = Bot(command_prefix='>', intents=intents) # The prefix used for the bot. 


@bot.event
async def on_ready():
	"""
 	This event tells us when the bot is online and ready, as well as set's a status on the bot. 
 	"""
	await bot.change_presence(activity = discord.Activity(type = discord.ActivityType.watching, name = 'you develop me.'))
	print('Up and running.')

	
@bot.command()
async def hi(ctx):
    await ctx.send("Oh, Hi there.")


if __name__ == "__main__":
	"""
  	This prevents replit from blocking us with too many requests.
	If the system gets req blocked, we kill the system and jump to a new IP
  	"""
	try:
		bot.run(os.environ["TOKEN"])
	except:
		os.system("kill 1")
