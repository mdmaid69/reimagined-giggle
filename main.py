import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))
def calculate_perimeter_triangle(a, b, c):
        return a + b + c