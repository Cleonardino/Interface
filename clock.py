from discord.ext import tasks
import time
import state_manager as sm
from sending import update_orders

@tasks.loop(seconds=60)
async def events_loop():
    # Updating gamestate
    # Current time in minutes since the epoch
    current_time = int(time.time() / 60)

    # Update global_timer
    sm.state[sm.SM_TIME] = current_time
    sm.save_state()
    await update_orders()
    

async def init_schedule():
    events_loop.start()