import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))
import array
def insert_into_array(array, i, item):
        array.insert(i, item)