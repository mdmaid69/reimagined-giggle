import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)
import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)