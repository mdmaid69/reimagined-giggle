import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"
import array
def set_array_slice(array, i, j, iterable):
        array[i:j] = iterable