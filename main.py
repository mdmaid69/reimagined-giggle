import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))
import array
def check_if_array_contains_item(array, item):
        return item in array