import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)
import array
def get_array_buffer_info(array):
        return array.buffer_info()