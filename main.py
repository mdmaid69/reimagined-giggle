import random
def roll_die():
        return random.randint(1, 6)
import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)