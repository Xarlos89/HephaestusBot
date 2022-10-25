import functions

import discord
from discord import Member
from discord.ext import commands
from discord.ext.commands import Bot

intents = discord.Intents().all()
bot = Bot(command_prefix='>>', intents=intents, help_command=None)

# @bot.slash_command(guild_ids=[900302240559018015], description="testing slash command")
# async def checkslash(ctx):
# 	await ctx.respond(content="slash command works.")

@bot.event
async def on_ready():
	await bot.change_presence(activity = discord.Activity(type = discord.ActivityType.watching, name = 'you develop me.'))
	print('Up and running.')

	
@bot.command()
async def hi(ctx):
    await ctx.send("Oh, Hi there.")

@bot.command()
async def imbored(ctx):	
	await ctx.send(functions.imbored())

@bot.command()
async def head(ctx, url):
	try:
		await ctx.send(
			embed=discord.Embed(
				title=f"Headers for {url}:",
				description=f"```{functions.head(url)}```",
				timestamp=ctx.message.created_at
			),
			reference=ctx.message
		)
	
	except functions.requests.exceptions.MissingSchema:
		await ctx.send("URL doesn't contain a **http scheme**", reference=ctx.message)

if __name__ == "__main__":
		bot.run("TOKEN")


