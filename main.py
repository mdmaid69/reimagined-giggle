import random
def generate_random_sample(population, k):
        return random.sample(population, k)
import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)