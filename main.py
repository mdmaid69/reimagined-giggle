import random
def generate_random_sample(population, k):
        return random.sample(population, k)
import array
def get_array_from_string(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a