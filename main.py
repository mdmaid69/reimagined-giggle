import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"
import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))