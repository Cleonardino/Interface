from typing import Final
import os
from dotenv import load_dotenv
from discord import Client, Intents, Message, User
import scheduler
import signal
import sys
import constants as cst

# Loading secret token
load_dotenv()
TOKEN : Final[str] = os.getenv('DISCORD_TOKEN')

## Setup
intents : Intents = Intents.default()
intents.message_content = True
client : Client = Client(intents=intents)

def shutdown():
    '''Shutdown the bot properly.'''
    print('KeyboardInterrupt : starting shutdown process')

    sys.exit(0)

# Interrupt signal handler
def signal_handler(signal, frame):
    '''Called when signal signal is raised.'''
    shutdown()

signal.signal(signal.SIGINT, signal_handler)

def print_log(text : str):
    with open(cst.LOG_FILE, mode="a", encoding="utf-8") as file:
        file.write(text)
        print(text)

async def message_received(message : Message, user_message : str) -> None:
    '''Message received event function.'''
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