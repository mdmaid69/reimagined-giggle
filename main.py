import array
def get_array_as_frozenset(array):
        return frozenset(array)
import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)