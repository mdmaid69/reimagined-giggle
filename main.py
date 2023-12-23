import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)
import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)