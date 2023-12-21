import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
import random
def generate_random_choice(choices):
        return random.choice(choices)