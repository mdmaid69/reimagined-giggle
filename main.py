import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))
import array
def convert_array_to_bytes(array):
        return array.tobytes()