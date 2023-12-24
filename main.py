import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))
import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)