import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
import array
def get_array_item_count(array, item):
        return array.count(item)