import random
def roll_die():
        return random.randint(1, 6)
import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))