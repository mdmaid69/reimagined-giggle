import platform
def get_python_version():
        return platform.python_version()
import random
def generate_random_sample(population, k):
        return random.sample(population, k)