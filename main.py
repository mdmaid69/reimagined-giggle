import os
def get_environment_variable(var):
        return os.getenv(var)
import random
def generate_random_sample(population, k):
        return random.sample(population, k)