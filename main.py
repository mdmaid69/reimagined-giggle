import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))
def convert_to_octal(n):
        return oct(n)