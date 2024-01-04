import random
def generate_random_number(start, end):
        return random.randint(start, end)
import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))