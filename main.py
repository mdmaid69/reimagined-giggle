import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"
import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)