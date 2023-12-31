import random
def shuffle_list(my_list):
        random.shuffle(my_list)
        return my_list
import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)