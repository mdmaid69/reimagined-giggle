import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a
import random
def generate_random_sample(population, k):
        return random.sample(population, k)