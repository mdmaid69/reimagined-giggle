import itertools
def get_permutations(iterable):
        return list(itertools.permutations(iterable))
import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)