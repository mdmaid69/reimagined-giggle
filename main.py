import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()
import random
def generate_random_sample(population, k):
        return random.sample(population, k)