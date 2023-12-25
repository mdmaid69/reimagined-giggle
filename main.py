import array
def get_array_itemsize(array):
        return array.itemsize
import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))