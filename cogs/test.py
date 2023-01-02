import discord
from discord import Member
from discord.ext import commands
from discord.ext.commands import Bot
from __main__ import bot

class testing(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.slash_command()
    async def emojis(self, ctx):
        for emoji in ctx.guild.emojis:
            print(f'<:{emoji.name}:{emoji.id}>')
        await ctx.respond("printing emoji list...")


def setup(bot):
    bot.add_cog(testing(bot))