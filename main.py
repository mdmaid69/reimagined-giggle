import array
def get_array_as_frozenset(array):
        return frozenset(array)
import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"