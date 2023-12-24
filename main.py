import array
def iterate_over_array(array):
        for item in array:
        print(item)
import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))