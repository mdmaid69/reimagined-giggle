import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))
def calculate_average(lst):
        return sum(lst) / len(lst)