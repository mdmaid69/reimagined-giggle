import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
def calculate_perimeter_triangle(a, b, c):
        return a + b + c