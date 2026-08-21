import random
from discord import Client
from discord.ext import tasks
import time

client : Client

@tasks.loop(seconds=60)
async def events_loop():
    # Updating gamestate
    # Current time in minutes since the epoch
    current_time = int(time.time() / 60)

    # Update global_timer
    gamestate.global_timer = current_time
    gamestate.save()

async def init_schedule(global_client):
    global client
    client = global_client
    events_loop.start()