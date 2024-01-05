import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))
import array
def extend_array(array, iterable):
        array.extend(iterable)