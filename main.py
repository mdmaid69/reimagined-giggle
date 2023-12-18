import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))
def reverse_string(s):
        return s[::-1]