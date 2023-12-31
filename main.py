import random
def generate_random_sample(population, k):
        return random.sample(population, k)
import os
def change_working_directory(path):
        os.chdir(path)