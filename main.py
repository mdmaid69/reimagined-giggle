import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)
import array
def extend_array(array, iterable):
        array.extend(iterable)