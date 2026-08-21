from typing import Final
import os
from dotenv import load_dotenv
from discord import Client, Intents, Message, User
from response import get_response
from response_utils import strip_reference
from data_function.constants import *
from data_function.usersdata import loaded_dimusers
import scheduler
import data_function.globaldata as gd
import signal
import sys

def shutdown():
    '''Shutdown the bot properly.'''
    print_log('KeyboardInterrupt : starting shutdown process')
    loaded_dimusers.save_all()
    sys.exit(0)

# Interrupt signal handler
def signal_handler(signal, frame):
    '''Called when signal signal is raised.'''
    shutdown()

signal.signal(signal.SIGINT, signal_handler)

# Loading secret token
load_dotenv()
TOKEN : Final[str] = os.getenv('DISCORD_TOKEN')

## Setup
intents : Intents = Intents.default()
intents.message_content = True
client : Client = Client(intents=intents)

async def message_received(message : Message, user_message : str) -> None:
    '''Message received event function.'''
    if user_message == "":
        # Empty message
        print_log('Message was empty because intents were disabled')
        return
    
    if user_message[0] != gd.cmd_symbol:
        # Not a command, ignore
        return
    
    user_message = user_message[1:]
    
    is_private = False
    
    target_user : User = message.author
    hashed_input : str = user_message.split(' ')
    cmd_id = hashed_input[0].lower()
    args = []
    if len(hashed_input) > 1:
        args = ' '.join(hashed_input[1:]).split(gd.config["sep_symbol"])
    if len(args) > 0:
        #If function callex with arguments, try to convert first argument to user id. If successfull, change target_user to
        #that user
        try:
            target_user = await client.fetch_user(strip_reference(args[0]))
        except Exception as e:
            pass
    responses, view, is_private = get_response(message, cmd_id, args, target_user)
    if is_private:
        for message_part_id in range(0,len(responses)):
            if message_part_id == len(responses) - 1:
                await message.author.send(responses[message_part_id], view=view)
            else:
                await message.author.send(responses[message_part_id], view=None)
    else:
        for message_part_id in range(0,len(responses)):
            if message_part_id == len(responses) - 1:
                await message.channel.send(responses[message_part_id], view=view)
            else:
                await message.channel.send(responses[message_part_id], view=None)

# Bot startup
@client.event
async def on_ready() -> None:
    '''Callback function when bot is ready.'''
    print_log(str(client.user) + " is now running")
    await scheduler.init_schedule(client)
        

# Handle incoming messages
@client.event
async def on_message(message : Message) -> None:
    '''Callback function when message received.'''
    if message.author == client.user:
        return
    await message_received(message=message, user_message=message.content)

# Main entry point
def main() -> None:
    client.run(token=TOKEN)

if __name__ == '__main__':
    main()