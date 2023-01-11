import discord
from discord import Member
from discord.ext import commands
from discord.ext.commands import Bot
from datetime import datetime
import os

class Fun(commands.Cog):
	def __init__(self, bot):
		self.bot = bot





	"""
	Bot commands can go here. Theses are all the things your bot "does"
	"""
	@commands.slash_command()
	async def hello(self, ctx):
		await ctx.respond(test)


		
	@commands.slash_command()
	async def echo(self, ctx, message: discord.Option(str)):
		await ctx.respond(f"You said '{message}'")

	async def cog_command_error(self, ctx, error):
		error_channel = await Bot.get_channel(1062754277543645324)

		embed = discord.Embed(title=f'<:red_circle:1043616578744357085> Error!'
				, description=f'{ctx.author} used /{ctx.command} in <#{ctx.channel}>'
				, color=discord.Color.dark_red()
				, timestamp=datetime.utcnow())
		embed.add_field(name='Error message: '
				, value=f'```py\n{error}```'
				, inline=True)

		await error_channel.send(embed=embed)








def setup(bot):
	bot.add_cog(Fun(bot))