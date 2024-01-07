import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
import array
def reverse_array(array):
        array.reverse()