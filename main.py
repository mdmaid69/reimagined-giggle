import itertools
def get_permutations(iterable):
        return list(itertools.permutations(iterable))
import random
def generate_random_sample(population, k):
        return random.sample(population, k)