import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))
import random
def generate_random_choice(choices):
        return random.choice(choices)