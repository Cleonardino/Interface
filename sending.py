import state_manager as sm
from constants import *
from random import randint
from utils import process_message
from setup import client

# Try to create a send order for the target; checking if it exists and if content is not empty
def try_send_order(source : str, target : str, content : str, stabilized : bool = False) -> str:
    if target not in sm.state[sm.SM_FAKE_IDS]:
        return "`////////////SEND==\nERROR:USER {target} DOES NOT EXIST`".format(target=target)
    
    if not content:
        return "`////////////SEND==\nERROR:CANNOT SEND EMPTY MESSAGE`"
    
    time_to_send = sm.state[sm.SM_TIME] + 2
    message_id : int = sm.state[sm.SM_MSG_COUNTER]
    if not stabilized:
        # Not stabilized, add a random delay (in minutes)
        time_to_send += randint(1,4)
    sm.state[sm.SM_TO_SEND][message_id] = {
		sm.TS_TIME : time_to_send,
		sm.TS_SOURCE : source,
		sm.TS_TARGET : target,
		sm.TS_CONTENT : content
	}
    
    sm.state[sm.SM_MSG_COUNTER] += randint(3,12)
    return "`////////////SEND==\nMESSAGE#{message_id} SENT SUCCESSFULLY TO {target}`".format(
        message_id=message_id,target=target
        )

# Update the orders, sending messages if needed
async def update_orders():
    # Retrieve messages to send
    to_send : list[str] = []
    for id in sm.state[sm.SM_TO_SEND]:
        if sm.state[sm.SM_TO_SEND][id][sm.TS_TIME] <= sm.state[sm.SM_TIME]:
            to_send.append(id)
    
    # Send the messages, delete the order
    for id in to_send:
        true_id = sm.state[sm.SM_FAKE_IDS][sm.state[sm.SM_TO_SEND][id][sm.TS_TARGET]]
        source = sm.state[sm.SM_TO_SEND][id][sm.TS_SOURCE]
        content = sm.state[sm.SM_TO_SEND][id][sm.TS_CONTENT]
        user = await client.fetch_user(true_id)
        cur_message : str = "`////////////RECEIVED==\nMESSAGE#{message_id} FROM {source}`\n`".format(
						message_id=id,source=source
						)
        cur_message += "CONTENT:\n" + process_message(content) + "`"
        if user:
            await user.send(
				cur_message
			)
        del sm.state[sm.SM_TO_SEND][id]