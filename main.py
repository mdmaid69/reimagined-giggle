import os
def list_files_in_directory(path):
        return os.listdir(path)
import random
def generate_random_sample(population, k):
        return random.sample(population, k)