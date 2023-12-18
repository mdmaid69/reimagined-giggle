import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)