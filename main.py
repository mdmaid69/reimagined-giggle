import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))
def calculate_area_triangle(b, h):
        return 0.5 * b * h