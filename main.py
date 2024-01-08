import random
def generate_random_number(start, end):
        return random.randint(start, end)
import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)