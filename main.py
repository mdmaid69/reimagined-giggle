import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
import array
def set_array_slice(array, i, j, iterable):
        array[i:j] = iterable