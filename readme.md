## HephaestusBot

HephaestusBot is a Py-Cord / Discord.py bot template, for use by anyone who wants to start their own bot.
- Supports slash commands
- Supports cogs
- Supports a safer "Tokenless" file. You run the file with a token as an arg. 

The bot is free, and open source. Anyone is welcome to fork this project.


Feel free to check out our other projects at https://xarlos89.github.io/PracticalPython/




## Using this bot

Install your discord.py libraries.

```
pip install discord.py
pip install py-cord
```

Open CMD and cd into the project directory. 

Now run this bot using the command

```
python main.py YOUR-BOT-TOKEN-GOES-HERE
```

The bot will automatically read all files in the "cogs" folder, and load them into the bot.
This bot also keeps your secret safe by passing it in as an argument, rather than placing it in the script itself.
