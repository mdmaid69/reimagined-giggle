import array
def get_string_from_array(array):
        return array.tobytes()
import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)