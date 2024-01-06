import array
def get_array_slice(array, i, j):
        return array[i:j]
import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))