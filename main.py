import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))
def remove_duplicates(lst):
        return list(set(lst))