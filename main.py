import random
def generate_random_sample(population, k):
        return random.sample(population, k)
import array
def convert_unicode_to_array(unicode, typecode):
        a = array.array(typecode)
        a.fromunicode(unicode)
        return a