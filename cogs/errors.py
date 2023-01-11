from discord.ext import commands
import traceback
import datetime
import sys

class errors(commands.Cog, command_attrs=dict(hidden=True)):
    def __init__(self, bot):
        self.bot = bot

    # @commands.Cog.listener()
    # async def cog_command_error(self, ctx, error, passed = False):
    #     if passed:
    #         channel = Bot.get_channel(1062754277543645324)
    #         sys.stderr = open('C:\\Users\\adam.miranda\\Desktop\\error.txt', 'w')

    #         with open('C:\\Users\\adam.miranda\\Desktop\\error.txt', 'r') as file:
    #             await channel.send(file)
    #     else:
    #         channel = Bot.get_channel(1062754277543645324)
    #         sys.stderr = open('C:\\Users\\adam.miranda\\Desktop\\error.txt', 'w')

    #         with open('C:\\Users\\adam.miranda\\Desktop\\error.txt', 'r') as file:
    #             await channel.send(file)


def setup(bot):
    bot.add_cog(errors(bot))