from discord.ext import commands

class onStartup(commands.Cog, command_attrs=dict(hidden=True)):
    def __init__(self, bot):
        self.bot = bot



    """
    This is just a 'listener' that shows somehting in the CMD line
    when your bot is ready to go. 
    """
    @commands.Cog.listener()
    async def on_ready(self):
        print('Bot is now ready to receive commands.')




def setup(bot):
    bot.add_cog(onStartup(bot))