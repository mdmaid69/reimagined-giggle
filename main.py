import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))
def calculate_area(radius):
        return 3.14 * radius * radius