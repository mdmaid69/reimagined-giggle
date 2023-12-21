import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)
def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)