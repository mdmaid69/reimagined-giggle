import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)
import array
def remove_from_array(array, item):
        array.remove(item)