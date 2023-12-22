import random
def generate_random_sample(population, k):
        return random.sample(population, k)
import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))