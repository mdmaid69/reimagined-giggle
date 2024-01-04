import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"
import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)