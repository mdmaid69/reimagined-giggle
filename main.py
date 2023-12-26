import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))
def remove_duplicates(lst):
        return list(set(lst))