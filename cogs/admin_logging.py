import discord
from discord import Member
from discord.ext import commands
from datetime import datetime
from asyncio import sleep
from __main__ import bot

# ToDo: Add user pfp to message log titles. 
# ToDo: Add channel-name to message logging. 



class logging(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
# ADMIN ONLY
# Verification logs and kicking

	@commands.Cog.listener()
	async def on_member_join(self, member):
		if 'Needs Approval' in [role.name for role in member.roles]:
			logs_channel = await bot.fetch_channel(1043621605940674580) # ADMIN user log
			embed = discord.Embed(title=''
				, description=f'{member.mention} joined, but has not verified.'
				, color=discord.Color.yellow())
			await logs_channel.send(embed=embed)

			# Kick timer, in seconds.
			await sleep(10)
			if 'Needs Approval' in [role.name for role in member.roles]:
				await member.kick(reason="Did not verify.")

# ADMIN ONLY
# Log name changes

	@commands.Cog.listener()
	async def on_member_update(self, before, after):
		if before.nick != after.nick and before.nick is not None:

			embed=discord.Embed(title=f'<:blue_circle:1043970617994645654> Name Change'
				, description=f'Changed by: {before.mention}.'
				, color=discord.Color.blue()
				, timestamp=datetime.utcnow())
			embed.add_field(name='Before', value=before.nick)
			embed.add_field(name='After', value=after.nick)

			logs_channel = await bot.fetch_channel(1043967844934762556) # ADMIN user log
			await logs_channel.send(embed=embed)

# ADMIN ONLY
# Log avatar updates

	@commands.Cog.listener()
	async def on_user_update(self, before, after):
		if before.avatar != after.avatar:

			embed=discord.Embed(title=f'<:yellow_circle:1043965444387782687> {before.name}'
				, color=discord.Color.yellow()
				, timestamp=datetime.utcnow())
			embed.set_thumbnail(url=after.avatar)
			embed.add_field(name='Avatar Update: '
				, value=before.mention
				, inline=True)

			logs_channel = await bot.fetch_channel(1043967844934762556) # ADMIN user log
			await logs_channel.send(embed=embed)


# ADMIN ONLY
# Log message deletes

	@commands.Cog.listener()
	async def on_message_delete(self, message):
		author = message.author

		embed = discord.Embed(title=f'<:red_circle:1043616578744357085> Deletion'
			, description=f'Deleted by: {message.author.mention}'
			, color=discord.Color.red()
			, timestamp=datetime.utcnow())
		embed.set_thumbnail(url=author.avatar)
		embed.add_field(name='Message: '
			, value=message.content
			, inline=True)

		logs_channel = await bot.fetch_channel(1043607758685089932) # ADMIN message log
		await logs_channel.send(embed=embed)

# ADMIN ONLY
# Log message edits

	@commands.Cog.listener()
	async def on_message_edit(self, message_before, message_after):
		if message_before.content != message_after.content:
			author = message_before.author

			embed=discord.Embed(title=f'<:orange_circle:1043616962112139264> Edit'
				, description=f'Edited by: {message_before.author.mention}.'
				, color=discord.Color.orange()
				, timestamp=datetime.utcnow())
			embed.set_thumbnail(url=author.avatar)
			embed.add_field(name='Original message: '
				, value=message_before.content
				, inline=True)

			embed.add_field(name= "After editing: "
				, value=message_after.content
				, inline=True)

			logs_channel = await bot.fetch_channel(1043607758685089932) # ADMIN message log
			await logs_channel.send(embed=embed)





def setup(bot):
	bot.add_cog(logging(bot))