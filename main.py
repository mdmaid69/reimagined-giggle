import random
def generate_random_choice(choices):
        return random.choice(choices)
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)