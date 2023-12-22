import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))
import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"