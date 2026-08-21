import json

from constants import *

def save_state():
    with open(GAMESTATE_PATH, 'w', encoding='utf-8') as file:
        json.dump(state, file, ensure_ascii=True, indent=4)
        
# Load gamestate file
open(GAMESTATE_PATH, 'a', encoding='utf-8').close()
with open(GAMESTATE_PATH, 'r', encoding='utf-8') as file:
    state : dict = json.load(file)
    if "users" not in state:
        state["users"] = {}
    if "fake_ids" not in state:
        state["fake_ids"] = {}