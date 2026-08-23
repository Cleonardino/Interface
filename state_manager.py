import json

from constants import *

# Define general game state field constants
SM_USERS = "users"
SM_FAKE_IDS = "fake_ids"
SM_TO_SEND = "to_send"
SM_TIME = "global_timer"
SM_MSG_COUNTER = "global_message_counter"

# User field constants
USR_FAKE_ID = "fake_id"
USR_SYNT_ROT = "synt_rot"
USR_SYNT_MAX = "synt_max"
USR_TARGET = "target"
USR_STABLE = "stable"
USR_TUNED = "tuned"

# To send message constants
TS_TIME = "time"
TS_SOURCE = "source"
TS_TARGET = "target"
TS_CONTENT = "content"

def save_state():
    with open(GAMESTATE_PATH, 'w', encoding='utf-8') as file:
        json.dump(state, file, ensure_ascii=True, indent=4)
        
# Load gamestate file
open(GAMESTATE_PATH, 'a', encoding='utf-8').close()
with open(GAMESTATE_PATH, 'r', encoding='utf-8') as file:
    state : dict = json.load(file)
    if SM_USERS not in state:
        state[SM_USERS] = {}
    if SM_FAKE_IDS not in state:
        state[SM_FAKE_IDS] = {}
    if SM_TO_SEND not in state:
            state[SM_TO_SEND] = {}
    if SM_MSG_COUNTER not in state:
            state[SM_MSG_COUNTER] = 12