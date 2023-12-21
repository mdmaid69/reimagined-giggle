import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"
import array
def get_array_slice(array, i, j):
        return array[i:j]