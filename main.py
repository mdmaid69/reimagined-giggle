import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)
import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"