import random
def generate_random_sample(population, k):
        return random.sample(population, k)
import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()