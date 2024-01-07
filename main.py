import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)
import array
def get_array_item_count(array, item):
        return array.count(item)