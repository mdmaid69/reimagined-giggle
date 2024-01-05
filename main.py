import random
def roll_die():
        return random.randint(1, 6)
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)