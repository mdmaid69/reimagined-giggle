import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)
import random
def generate_random_number(start, end):
        return random.randint(start, end)