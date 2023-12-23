import json
def read_from_json(json_string):
        return json.loads(json_string)
import random
def shuffle_list(my_list):
        random.shuffle(my_list)
        return my_list