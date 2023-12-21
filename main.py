import array
def get_string_from_array(array):
        return array.tobytes()
import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))