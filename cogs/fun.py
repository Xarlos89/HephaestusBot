import discord
from discord import Member
from discord.ext import commands
from discord.ext.commands import Bot
from __main__ import bot

class Fun(commands.Cog):
	def __init__(self, bot):
		self.bot = bot





	"""
	Bot commands can go here. Theses are all the things your bot "does"
	"""
	@commands.slash_command()
	async def hello(self, ctx):
		await ctx.respond("Oh, Hi there.")


	@commands.slash_command()
	async def echo(self, ctx, message: discord.Option(str)):
		await ctx.respond(f"You said '{message.meantion}'")




	@bot.event
	async def on_command_error(ctx, error):
	    channel = bot.get_channel(1046099711188279389)
	    await channel.send(ctx.command) # I am trying to send the command with error here
	    await channel.send(error)
	    raise error




def setup(bot):
	bot.add_cog(Fun(bot))