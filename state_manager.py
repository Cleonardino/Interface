import json

from constants import *


def set_state(field : str, object):
        state[field] = object
        save_state()

def get_state(field : str):
        return state[field]

def save_state():
    with open(GAMESTATE_PATH, 'w', encoding='utf-8') as file:
        json.dump(state, file, ensure_ascii=True, indent=4)
        
# Load gamestate file
open(GAMESTATE_PATH, 'a', encoding='utf-8').close()
with open(GAMESTATE_PATH, 'r', encoding='utf-8') as file:
    state : dict = json.load(file)