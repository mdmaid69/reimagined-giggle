import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))
def convert_to_hex(n):
        return hex(n)