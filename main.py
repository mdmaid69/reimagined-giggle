import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)
import array
def get_array_itemsize(array):
        return array.itemsize