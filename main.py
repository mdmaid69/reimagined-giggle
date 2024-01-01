import itertools
def get_permutations(iterable):
        return list(itertools.permutations(iterable))
import array
def get_array_buffer_info(array):
        return array.buffer_info()