import random
def generate_random_sample(population, k):
        return random.sample(population, k)
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)