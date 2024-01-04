import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"
import array
def pop_from_array(array, i=-1):
        return array.pop(i)