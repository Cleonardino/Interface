import state_manager as sm
from constants import *
from utils import print_log
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
    
	try:
		user = await client.fetch_user(true_id)
	except:
		print_log("Failure : user with id {true_id} does not seem to exist".format(true_id=true_id))
		return ("Well, it seems like this bot is completely bugged out. Contact the creator. This is not" +
		" part of the game, the creator just don't know how to code.")
    
	if user:
		await user.send(
		"`////////////STABILIZE==\nUSER {source} HAVE STABILIZED YOU,".format(source=source) +
            " YOU WILL NOW ENCOUNTER SHORTER DELAYS WHEN SENDING MESSAGES`"
		)
	return ("`////////////STABILIZE==\nUSER {target} IS NOW STABLE AND".format(target=target) +
            " WILL ENCOUNTER SHORTER DELAYS WHEN SENDING MESSAGES`")