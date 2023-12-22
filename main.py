import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)
import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)