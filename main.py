import random
def roll_die():
        return random.randint(1, 6)
import array
def set_array_slice(array, i, j, iterable):
        array[i:j] = iterable