import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))
def calculate_pressure(force, area):
        return force / area