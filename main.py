import array
def get_array_as_bytes(array):
        return bytes(array)
import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)