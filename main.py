import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)
import random
def generate_random_choice(choices):
        return random.choice(choices)