import array
def get_array_as_memoryview(array):
        return memoryview(array)
import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)