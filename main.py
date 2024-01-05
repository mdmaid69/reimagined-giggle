import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)
import random
def generate_random_sample(population, k):
        return random.sample(population, k)