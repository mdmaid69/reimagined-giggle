import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)
import array
def set_array_item(array, i, item):
        array[i] = item