import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)
import random
def roll_die():
        return random.randint(1, 6)