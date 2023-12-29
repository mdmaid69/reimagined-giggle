import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)
import random
def generate_random_sample(population, k):
        return random.sample(population, k)