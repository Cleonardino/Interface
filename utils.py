import datetime
from random import sample

from constants import *

# Contain couples of loaded banword and on-the-fly generated replacement
banwords : list = []

with open(BANWORDS_PATH, mode="r",encoding="utf-8") as file:
	for line in file:
		word : str = line.strip()
		replacement : str = ""
		for i in range(len(word)):
			# Add a random clutter char
			replacement += sample(CLUTTER_CHARS, 1)[0]
		banwords.append((word,replacement))

# Apply transformations to a message
def process_message(text : str, clutter_proportion: float = 0.05):
	result : str = text.lower()
    
	# Replacing banwords
	for (banword,replacement) in banwords:
		result = result.replace(banword,replacement)

 
	# Adding clutter
	# Create list of indexes in message
	result_list : list = list(result)
	index_list : list = list(range(len(result)))
	index_list = sample(index_list, int(len(result) * clutter_proportion))
	for index in index_list:
		result_list[index] = sample(CLUTTER_CHARS, 1)[0]
	result = "".join(result_list)
    
	return result

def print_log(text : str):
    with open(LOG_FILE, mode="a", encoding="utf-8") as file:
        file.write("\n" + str(datetime.datetime.now()) + text)
        print(text)