import os
import discord
from discord import Member
from discord.ext import commands
from discord.ext.commands import Bot

# intents = discord.Intents.default()
bot = Bot(command_prefix='>')
bot.remove_command("help")


@bot.event
async def on_ready():
	await bot.change_presence(activity = discord.Activity(type = discord.ActivityType.watching, name = 'you develop me.'))
	print('Up and running.')

	
@bot.command()
async def hi(ctx):
    await ctx.send("Oh, Hi there.")


if __name__ == "__main__":

	bot.run(os.environ["TOKEN"])

