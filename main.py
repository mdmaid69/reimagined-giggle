import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)
import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"