import random
def generate_random_sample(population, k):
        return random.sample(population, k)
import os
def get_current_working_directory():
        return os.getcwd()