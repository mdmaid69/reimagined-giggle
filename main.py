import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))
import array
def get_bytes_from_array(array):
        return array.tobytes()