import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)
import random
def generate_random_choice(choices):
        return random.choice(choices)