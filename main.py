import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
import array
def append_to_array(array, item):
        array.append(item)