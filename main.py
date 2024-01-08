import random
def shuffle_list(my_list):
        random.shuffle(my_list)
        return my_list
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)