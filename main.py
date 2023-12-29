import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)
import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"