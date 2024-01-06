import random
def generate_random_sample(population, k):
        return random.sample(population, k)
import platform
def get_os_info():
        return platform.uname()