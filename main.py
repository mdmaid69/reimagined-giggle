import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))
def add_numbers(a, b):
        return a + b