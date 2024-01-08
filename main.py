import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))
import random
def roll_die():
        return random.randint(1, 6)