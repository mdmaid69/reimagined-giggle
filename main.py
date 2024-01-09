import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)
import random
def roll_die():
        return random.randint(1, 6)