import array
def get_array_buffer_info(array):
        return array.buffer_info()
import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)