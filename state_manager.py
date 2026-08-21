import json

from constants import *


def save():
        '''Save gamestate with current variables to file. Used during the update loop.'''
        with open(GAMESTATE_PATH, 'w', encoding='utf-8') as file:
            json.dump(gamestate, file, ensure_ascii=True, indent=4)

# Load gamestate file
with open(GAMESTATE_PATH, 'r', encoding='utf-8') as file:
    gamestate : dict = json.load(file)