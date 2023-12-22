import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)
import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))