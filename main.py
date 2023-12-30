import array
def get_bytes_from_array(array):
        return array.tobytes()
import random
def generate_random_sample(population, k):
        return random.sample(population, k)