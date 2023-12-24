import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
import array
def check_if_array_does_not_contain_item(array, item):
        return item not in array