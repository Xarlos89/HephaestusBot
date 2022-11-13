import discord
from discord import Member
from discord.ext import commands
from discord.ext.commands import Bot

"""

This area is for bot intents, which can be set in the discord Dev portal. 
We can also set the command prefix here, which is a prefix you can use for normal text commands. 

"""
bot = commands.Bot(command_prefix = '!', intents=discord.Intents.all())


"""
This function loads all cogs in the cog folder into the bot. 
Anything with a .py in the cog folder will be loaded. 

"""
def load_cogs():
        for f in os.listdir("./cogs"):
                if f.endswith(".py"):
                    bot.load_extension("cogs." + f[:-3])


"""
This function allows you to pass your Bot token into the command you use to run the file.
For example, you might run this bot using

python main.py BOT-TOKEN-GOES-HERE

"""
def load_key_and_run():
    if len(sys.argv) > 1:
        TOKEN = sys.argv[1]
        bot.run(TOKEN)
    else:
        print('ERROR: You must include a bot token.')



if __name__ == "__main__":
    load_cogs()
    load_key_and_run()



