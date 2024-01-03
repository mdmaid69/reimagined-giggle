import random
def generate_random_sample(population, k):
        return random.sample(population, k)
import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)