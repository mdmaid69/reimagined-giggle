import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)
def is_even(n):
        return n % 2 == 0