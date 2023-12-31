import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))
def calculate_area(radius):
        return 3.14 * radius * radius