import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
import array
def check_if_array_contains_item(array, item):
        return item in array