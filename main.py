from typing import Final
import state_manager as sm
import os
from dotenv import load_dotenv
from discord import Message
import signal
import sys
from constants import *
from utils import print_log
from clock import init_schedule
from message_manager import process_message
from setup import client

# Loading secret token
load_dotenv()
TOKEN : Final[str] = os.getenv('DISCORD_TOKEN')



# Interrupt signal handler
def shutdown(signal, frame):
    '''Shutdown the bot properly.'''
    print_log('KeyboardInterrupt : starting shutdown process')
    sm.save_state()
    sys.exit(0)

signal.signal(signal.SIGINT, shutdown)

async def message_received(message : Message) -> None:
    '''Message received event function.'''
    if message.content == "":
        # Empty message
        print_log('Message was empty because intents were disabled')
        return
    if message.channel.type.name != "private":
        # Not private message
        await message.author.send("The Interface will only answer to private message")
        return
    await process_message(message)

# Bot startup
@client.event
async def on_ready() -> None:
    '''Callback function when bot is ready.'''
    await init_schedule()
    print_log(str(client.user) + " is now running")

# Handle incoming messages
@client.event
async def on_message(message : Message) -> None:
    '''Callback function when message received.'''
    if message.author == client.user:
        # Message from bot itself, don't do anything
        return
    await message_received(message=message)

# Main entry point
def main() -> None:
    client.run(token=TOKEN)

if __name__ == '__main__':
    main()