import random
def generate_random_choice(choices):
        return random.choice(choices)
import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)