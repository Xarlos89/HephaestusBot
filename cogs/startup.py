import discord
from discord import Member
from discord.ext import commands
from discord.ext.commands import Bot



"""
This cog handles the startup of your bot. Any pre-start items can go here.
"""
class startup(commands.Cog):
	def __init__(self, bot):
		self.bot = bot


	@bot.event
	async def on_ready():
		await bot.change_presence(activity = discord.Activity(type = discord.ActivityType.watching, name = 'you develop me.'))
		print('Up and running.')








def setup(bot):
	bot.add_cog(startup(bot))