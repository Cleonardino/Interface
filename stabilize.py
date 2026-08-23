import state_manager as sm
from constants import *
from random import randint
from utils import process_message
from setup import client

# Try to create a send order for the target; checking if it exists and if content is not empty
async def try_stabilize(source : str, target : str) -> str:
	if target not in sm.state[sm.SM_FAKE_IDS]:
		return "`////////////STABILIZE==\nERROR:USER {target} DOES NOT EXIST`".format(target=target)
    
	true_id : str = sm.state[sm.SM_FAKE_IDS][target]
    
	if sm.state[sm.SM_USERS][true_id][sm.USR_STABLE]:
		return "`////////////STABILIZE==\nERROR:USER IS ALREADY STABLE`"
    
	if source == target:
		return "`////////////STABILIZE==\nERROR:CANNOT STABILIZE YOURSELF`"
    
    # Successfull stabilize
	sm.state[sm.SM_USERS][true_id][sm.USR_STABLE] = True
    
	user = await client.fetch_user(true_id)
    
	if user:
		await user.send(
		"`////////////STABILIZE==\nUSER {source} HAVE STABILIZED YOU,".format(source=source) +
            "YOU WILL NOW ENCOUNTER SHORTER DELAYS WHEN SENDING MESSAGES`"
		)
	return ("`////////////STABILIZE==\nUSER {target} IS NOW STABLE AND".format(target=target) +
            "WILL ENCOUNTER SHORTER DELAYS WHEN SENDING MESSAGES`")