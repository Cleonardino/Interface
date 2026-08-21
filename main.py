from typing import Final
import state_manager as sm
import os
from dotenv import load_dotenv
from discord import Client, Intents, Message
import clock
import signal
import sys
from constants import *

# Loading secret token
load_dotenv()
TOKEN : Final[str] = os.getenv('DISCORD_TOKEN')

## Setup
intents : Intents = Intents.default()
intents.message_content = True
client : Client = Client(intents=intents)

# Interrupt signal handler
def shutdown(signal, frame):
    '''Shutdown the bot properly.'''
    print('KeyboardInterrupt : starting shutdown process')
    sm.save_state()
    sys.exit(0)

signal.signal(signal.SIGINT, shutdown)

def print_log(text : str):
    with open(LOG_FILE, mode="a", encoding="utf-8") as file:
        file.write("\n" + + text)
        print(text)

async def message_received(message : Message, user_message : str) -> None:
    '''Message received event function.'''
    if message.channel.type.name != "private":
        # Not private message
        await message.author.send("The Interface will only answer to private message")
    if user_message == "":
        # Empty message
        print_log('Message was empty because intents were disabled')
        return
    print_log("Message received !")

# Bot startup
@client.event
async def on_ready() -> None:
    '''Callback function when bot is ready.'''
    print_log(str(client.user) + " is now running")

# Handle incoming messages
@client.event
async def on_message(message : Message) -> None:
    '''Callback function when message received.'''
    if message.author == client.user:
        # Message from bot itself, don't do anything
        return
    await message_received(message=message, user_message=message.content)

# Main entry point
def main() -> None:
    client.run(token=TOKEN)

if __name__ == '__main__':
    main()