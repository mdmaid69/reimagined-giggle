import array
def get_array_as_tuple(array):
        return tuple(array)
import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))