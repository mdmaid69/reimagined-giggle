import random
def roll_die():
        return random.randint(1, 6)
import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))