import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
import array
def remove_from_array(array, item):
        array.remove(item)