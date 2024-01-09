import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))
def calculate_work(force, distance):
        return force * distance