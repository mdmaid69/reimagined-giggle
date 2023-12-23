import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)
import array
def set_array_slice(array, i, j, iterable):
        array[i:j] = iterable