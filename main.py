import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)
import random
def generate_random_choice(choices):
        return random.choice(choices)