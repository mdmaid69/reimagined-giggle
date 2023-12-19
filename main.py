import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)
import random
def generate_random_sample(population, k):
        return random.sample(population, k)