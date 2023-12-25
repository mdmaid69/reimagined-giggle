import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)
import array
def iterate_over_array(array):
        for item in array:
        print(item)