import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
import array
def insert_into_array(array, i, item):
        array.insert(i, item)