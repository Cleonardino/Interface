# Setup
Create game_state.json, with inside only "{}" (an empty json object)
Create banwords.txt
Banwords need to have "interface" in it. Also enter, one word per line, each name, surname, and means of identification for each participant. Do not enter words too small as they may appear in other words. Word with at least 6 letters are possible.
Create .env, with the bot token as "DISCORD_TOKEN=your_token"


The main bot entrypoint is main.py
The .env file need the discord token of the bot
Everything takes place in private messages with the bot
When each participant has send at least one message to the bot for setup, trigger the start with "trigger_start" message
