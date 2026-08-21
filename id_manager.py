from random import randint
import state_manager as st

def random_letter():
    return "abcdefghijklmnopqrstuvwxyz"[randint(0,25)]

def generate_random_id():
    result = ""
    for i in range(5):
        result += random_letter()

def create_unique_fake_id():
	# User not in database, add it and associate a unique id
	unique_id = generate_random_id()
	while unique_id in st.state["fake_ids"]:
		unique_id = generate_random_id()
	return unique_id