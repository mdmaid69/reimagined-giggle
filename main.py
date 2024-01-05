import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a
import random
def generate_random_sample(population, k):
        return random.sample(population, k)