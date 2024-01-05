import array
def convert_array_to_bytes(array):
        return array.tobytes()
import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)