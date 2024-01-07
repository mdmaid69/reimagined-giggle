import itertools
def get_permutations(iterable):
        return list(itertools.permutations(iterable))
import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"