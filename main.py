import random
def generate_random_sample(population, k):
        return random.sample(population, k)
import array
def get_array_from_bytes(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a