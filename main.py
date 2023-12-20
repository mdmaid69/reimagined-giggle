import array
def get_array_as_memoryview(array):
        return memoryview(array)
import random
def generate_random_sample(population, k):
        return random.sample(population, k)