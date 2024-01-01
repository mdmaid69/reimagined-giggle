import random
def generate_random_sample(population, k):
        return random.sample(population, k)
import os
def remove_directory(path):
        os.rmdir(path)