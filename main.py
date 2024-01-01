import array
def iterate_over_array(array):
        for item in array:
        print(item)
import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))