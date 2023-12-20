import collections
def count_elements(iterable):
        return collections.Counter(iterable)
import random
def generate_random_sample(population, k):
        return random.sample(population, k)