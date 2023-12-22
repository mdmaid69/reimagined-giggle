import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))
def find_difference(list1, list2):
        return set(list1) - set(list2)