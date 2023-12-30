import random
def generate_random_sample(population, k):
        return random.sample(population, k)
import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))