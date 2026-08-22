from discord import Message
import state_manager as sm
from constants import *
from links import *

SHUFFLE_LIST : list[int] = [4,1,0,2,3]

# Construct the message and manage synt rotation
def synthetize(user_id : str) -> str:
    # Create message
    out_message : str = "`////////////SYNT==\n"
    
    # Rotation is in range of target id discovery
    synt_rot : int = sm.state[sm.SM_USERS][user_id][sm.USR_SYNT_ROT]
    target : str = sm.state[sm.SM_USERS][user_id][sm.USR_TARGET]
    true_index : int = SHUFFLE_LIST[synt_rot]
    # Link corresponding to number
    out_message += NUMBERS_LINK[true_index] + "\n"
    # Link corresponding to telestic id
    out_message += TELESTIC_DICT[target[true_index]]
    out_message += "////////////`"
    return out_message