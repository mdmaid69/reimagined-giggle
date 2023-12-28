import random
def shuffle_list(my_list):
        random.shuffle(my_list)
        return my_list
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)