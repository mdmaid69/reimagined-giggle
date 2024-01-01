import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))
def calculate_perimeter_rectangle(l, w):
        return 2 * (l + w)