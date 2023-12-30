def remove_duplicates(lst):
        return list(set(lst))
import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)