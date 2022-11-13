import discord
from discord import Member
from discord.ext import commands
from discord.ext.commands import Bot

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
		await ctx.respond(f"You said '{message}'")








def setup(bot):
	bot.add_cog(Fun(bot))