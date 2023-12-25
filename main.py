import random
def roll_die():
        return random.randint(1, 6)
import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))