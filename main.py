import itertools
def get_permutations(iterable):
        return list(itertools.permutations(iterable))
import array
def set_array_slice(array, i, j, iterable):
        array[i:j] = iterable