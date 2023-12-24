import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)
import array
def get_bytes_from_array(array):
        return array.tobytes()