import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
import array
def set_array_item(array, i, item):
        array[i] = item