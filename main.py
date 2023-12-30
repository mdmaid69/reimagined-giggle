import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)
import array
def insert_into_array(array, i, item):
        array.insert(i, item)