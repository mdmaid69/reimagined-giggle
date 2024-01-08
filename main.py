import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)
import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))