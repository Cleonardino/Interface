from random import randint
import state_manager as sm

def random_letter():
    return "abcdefghijklmnopqrstuvwxyz"[randint(0,25)]

def generate_random_id():
    result = ""
    for i in range(5):
        result += random_letter()
    return result

def create_unique_fake_id():
	# User not in database, add it and associate a unique id
	unique_id = generate_random_id()
	while unique_id in sm.state[sm.SM_FAKE_IDS]:
		unique_id = generate_random_id()
	return unique_id