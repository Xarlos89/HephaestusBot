import discord
from discord import Member
from discord.ext import commands
from asyncio import sleep
from __main__ import bot

class logging(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.Cog.listener()
	async def on_member_join(self, member):
		await member.add_roles(member.guild.get_role(1043624460168728606))

		if 'Needs Approval' in [role.name for role in member.roles]:
			logs_channel = await bot.fetch_channel(1043621605940674580) # Welcome channel
			embed = discord.Embed(title=''
				, description=f'{member.mention} joined, but has not verified.'
				, color=discord.Color.yellow())
			await logs_channel.send(embed=embed)
			await sleep(10)
			if 'Needs Approval' in [role.name for role in member.roles]:
				await member.kick(reason="Did not verify.")

	@commands.Cog.listener()
	async def on_message_delete(self, message):
		author = message.author

		embed = discord.Embed(title=f'<:red_circle:1043616578744357085> Deletion'
			, description=f'Deleted by: {message.author.mention}'
			, color=discord.Color.red())
		embed.set_thumbnail(url=author.avatar)
		embed.add_field(name='Message: '
			, value=message.content
			, inline=True)

		logs_channel = await bot.fetch_channel(1043607758685089932)
		await logs_channel.send(embed=embed)

### Message Edits
	@commands.Cog.listener()
	async def on_message_edit(self, message_before, message_after):
		author = message_before.author

		embed=discord.Embed(title=f'<:orange_circle:1043616962112139264> Edit'
			, description=f'Edited by: {message_before.author.mention}.'
			, color=discord.Color.orange())
		embed.set_thumbnail(url=author.avatar)
		embed.add_field(name='Original message: '
			, value=message_before.content
			, inline=True)

		embed.add_field(name= "After editing: "
			, value=message_after.content
			, inline=True)

		logs_channel = await bot.fetch_channel(1043607758685089932)
		await logs_channel.send(embed=embed)

def setup(bot):
	bot.add_cog(logging(bot))