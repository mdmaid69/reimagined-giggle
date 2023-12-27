import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)
import array
def pop_from_array(array, i=-1):
        return array.pop(i)