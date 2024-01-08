import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)
import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)