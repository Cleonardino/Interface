import json

from constants import *

# Define game state field constants
SM_USERS = "users"
SM_FAKE_IDS = "fake_ids"
SM_USERS = "users"
SM_USERS = "users"
USR_FAKE_ID = "fake_id"
USR_SYNT_ROT = "synt_rot"
USR_SYNT_MAX = "synt_max"
USR_TARGET = "target"

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