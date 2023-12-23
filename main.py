import array
def get_array_as_frozenset(array):
        return frozenset(array)
import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))