import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)
import random
def generate_random_sample(population, k):
        return random.sample(population, k)