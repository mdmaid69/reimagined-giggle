import os
def get_file_size(filename):
        return os.path.getsize(filename)
import random
def generate_random_sample(population, k):
        return random.sample(population, k)