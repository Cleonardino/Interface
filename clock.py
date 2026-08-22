from discord.ext import tasks
import time
import state_manager as sm

@tasks.loop(seconds=60)
async def events_loop():
    # Updating gamestate
    # Current time in minutes since the epoch
    current_time = int(time.time() / 60)

    # Update global_timer
    sm.state[sm.SM_TIME] = current_time
    sm.save_state()

async def init_schedule():
    events_loop.start()