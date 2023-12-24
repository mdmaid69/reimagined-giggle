import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"
import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}