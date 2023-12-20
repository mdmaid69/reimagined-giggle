import random
def roll_die():
        return random.randint(1, 6)
import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)