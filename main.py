import array
def extend_array(array, iterable):
        array.extend(iterable)
import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"