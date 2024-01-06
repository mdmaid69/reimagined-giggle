import random
def generate_random_number(start, end):
        return random.randint(start, end)
import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)