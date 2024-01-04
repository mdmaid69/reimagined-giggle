import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)
import itertools
print(list(itertools.permutations([1, 2, 3])))