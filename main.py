import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))
import array
def get_array_buffer_info(array):
        return array.buffer_info()