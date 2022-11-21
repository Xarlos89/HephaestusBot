import discord
from discord import Member
from discord.ext import commands
from datetime import datetime
from asyncio import sleep
from __main__ import bot




class logging(commands.Cog):
	def __init__(self, bot):
		self.bot = bot


#################################								
#								#
#			Channel ID's		#
#								#
#################################

		# message_delete and message_edit
		channel_message_log = 954023390375710751

		# name_change and avatar_change
		channel_user_log_admin = 953552502937243679

		# on_join and on_remove
		channel_user_log_public = 953543179133665380

		# on_join_unverified and on_remove_unverified
		channel_verification_log = 1044302239616991242


#-------------------------------#
#								#
#   channel_verification_log	#
#								#
#-------------------------------#

	@commands.Cog.listener()
	async def on_member_join(self, member):
		if 'Needs Approval' in [role.name for role in member.roles]:
			logs_channel = await bot.fetch_channel(channel_verification_log) # ADMIN user log
			embed = discord.Embed(title=''
				, description=f'{member.mention} joined, but has not verified.'
				, color=discord.Color.yellow())
			await logs_channel.send(embed=embed)

			# Kick timer, in seconds.
			time_unverified_kick = 3600
			await sleep(time_unverified_kick)

			if 'Needs Approval' in [role.name for role in member.roles]:
				# Log the kick
				embed = discord.Embed(title=''
					, description=f'{member.mention} did not verify, auto-removed. ({time_unverified_kick*60} hour/s)'
					, color=discord.Color.red())
				await logs_channel.send(embed=embed)

				await member.kick(reason="Did not verify.")

#-------------------------------#
#								#
#    channel_user_log_admin	    #
#								#
#-------------------------------#

	@commands.Cog.listener()
	async def on_member_update(self, before, after):
		if before.nick != after.nick and before.nick is not None:

			embed=discord.Embed(title=f'<:grey_exclamation:1044305627201142880> Name Change'
				, description=f'Changed by: {before}.'
				, color=discord.Color.dark_grey()
				, timestamp=datetime.utcnow())
			embed.set_thumbnail(url=after.avatar)
			embed.add_field(name='Before', value=before.nick, inline=True)
			embed.add_field(name='After', value=after.mention, inline=True)

			logs_channel = await bot.fetch_channel(channel_user_log_admin) # ADMIN user log
			await logs_channel.send(embed=embed)

	@commands.Cog.listener()
	async def on_user_update(self, before, after):
		if before.avatar != after.avatar:

			embed=discord.Embed(title=f'<:grey_exclamation:1044305627201142880> {before.name}'
				, color=discord.Color.dark_grey()
				, timestamp=datetime.utcnow())
			embed.set_thumbnail(url=after.avatar)
			embed.add_field(name='Avatar Update: '
				, value=before.mention
				, inline=True)

			logs_channel = await bot.fetch_channel(channel_user_log_admin) # ADMIN user log
			await logs_channel.send(embed=embed)


#-------------------------------#
#								#
#      channel_message_log	    #
#								#
#-------------------------------#

	@commands.Cog.listener()
	async def on_message_delete(self, message):
		author = message.author

		embed = discord.Embed(title=f'<:red_circle:1043616578744357085> Deleted Message'
			, description=f'Deleted by {message.author.mention}\nIn {message_after.channel.mention}'
			, color=discord.Color.dark_red()
			, timestamp=datetime.utcnow())
		embed.set_thumbnail(url=author.avatar)
		embed.add_field(name='Message: '
			, value=message.content
			, inline=True)

		logs_channel = await bot.fetch_channel(channel_message_log) # ADMIN message log
		await logs_channel.send(embed=embed)

	@commands.Cog.listener()
	async def on_message_edit(self, message_before, message_after):
		if message_before.content != message_after.content:
			author = message_before.author

			embed=discord.Embed(title=f'<:orange_circle:1043616962112139264> Message Edit'
				, description=f'Edited by {message_before.author.mention}\nIn {message_after.channel.mention}'
				, color=discord.Color.dark_orange()
				, timestamp=datetime.utcnow())
			embed.set_thumbnail(url=author.avatar)
			embed.add_field(name='Original message: '
				, value=message_before.content
				, inline=True)

			embed.add_field(name= "After editing: "
				, value=message_after.content
				, inline=True)

			logs_channel = await bot.fetch_channel(channel_message_log) # ADMIN message log
			await logs_channel.send(embed=embed)




def setup(bot):
	bot.add_cog(logging(bot))