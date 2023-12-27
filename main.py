import random
def generate_random_sample(population, k):
        return random.sample(population, k)
import array
def set_array_slice(array, i, j, iterable):
        array[i:j] = iterable