import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
def calculate_area_triangle(b, h):
        return 0.5 * b * h