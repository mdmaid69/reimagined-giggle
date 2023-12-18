import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))
import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)