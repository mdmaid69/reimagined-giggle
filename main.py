import random
def generate_random_sample(population, k):
        return random.sample(population, k)
import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)