import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
import array
def pop_from_array(array, i=-1):
        return array.pop(i)