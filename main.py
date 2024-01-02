import random
def generate_random_choice(choices):
        return random.choice(choices)
import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))