import array
def get_string_from_array(array):
        return array.tobytes()
import random
def generate_random_sample(population, k):
        return random.sample(population, k)