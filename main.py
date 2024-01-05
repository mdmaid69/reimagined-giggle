import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))
def square_number(x):
        return x**2