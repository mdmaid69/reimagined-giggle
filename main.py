import array
def extend_array(array, iterable):
        array.extend(iterable)
import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))